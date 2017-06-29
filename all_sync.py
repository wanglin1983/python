#!/usr/bin/python
import os
import sys

# Import log module
sys.path.append('/home/wanglin0408/WorkDir/python')
import logger

# First Param : branch name
branch = ''
if len(sys.argv) > 1:
    branch = sys.argv[1]

# P4 enviroment
p4Env = 'export P4USER="linus.wang"\n'
p4Env += 'export P4PASSWD="1q2w3e4r"\n'
p4Env += 'export P4CLIENT="DEV-CHROMIUM-LINUS"\n'
p4Env += 'export P4PORT="10.103.211.119:1888"\n'

# P4 branchs
P4ROOT_LOCAL = '/home/wanglin0408/WorkDir/P4'
P4ROOT = "//TIZEN_3.0/[Product2017]/[%s]/[INT]/COMMON/Profile/platform/framework/web/chromium-efl/..."
P4ROOT_MAIN = "//TIZEN_3.0/[MAIN2017]/[PROD2017_Prj]/[INT]/COMMON/Profile/platform/framework/web/chromium-efl/..."

mapBranchs = {}
mapBranchs['MAIN'] = P4ROOT_MAIN
mapBranchs['ATSC'] = P4ROOT %'KantM_ATSC_MP_Prj'
mapBranchs['DVB'] = P4ROOT %'KantM_DVB_MP_Prj'
mapBranchs['ISDB'] = P4ROOT %'KantM_ISDB_MP_Prj'
mapBranchs['AV'] = P4ROOT %'KantM_AV_MP_Prj'
mapBranchs['DTMB'] = P4ROOT %'KantM_DTMB_MP_Prj'
mapBranchs['HAWKA'] = P4ROOT %'HawkA_2017_MP_Prj'
mapBranchs['KANTS'] = P4ROOT %'KantS_MP_Prj'
mapBranchs['TRUNK'] = P4ROOT %'Trunk_2017_MP_Prj'

SYNCFLAG='SYNCING'

# Perforce
def sync_branch(branch):
    if mapBranchs.has_key(branch) == False:
        logger.error("No such branch in Tizen3.0 : [%s]" %branch)
        return

    # Prepare
    curBranch = mapBranchs[branch]
    p4BranchName = "[KantM_%s_MP_Prj]" %branch
    branchDir = P4ROOT_LOCAL + "/Tizen3.0_" + branch
    needInit = 0
    if os.path.exists(branchDir) == False:
        logger.debug(branchDir + " Not exist!")
        needInit = 1
        os.makedirs(branchDir)
    os.chdir(branchDir)

    # Get local CL from Git
    if needInit == 0:
        command = "git log | awk -F '@' '{print $2}'"
        gitLogs = os.popen(command).read()
        result = gitLogs.replace('\n', '')
        result = result.split('samsung.com>')
        if (len(result) > 1):
            localCL = result[1]
        else:
            localCL = ""
    else:
        localCL = ""
    print(p4BranchName + " local CL : "),
    logger.info(localCL)

    # Get Latest CL from p4 server
    command = p4Env
    command += "p4 changes -m 1 " + curBranch + " | awk '{print $2}'"
    latestCL = os.popen(command).read()
    latestCL = latestCL.replace('\n', '')
    print(p4BranchName + " latest CL : "),

    if localCL == latestCL:
        logger.info(latestCL)
        logger.info(p4BranchName + " already updated to latest CL.")
        return

    logger.debug(latestCL)

    # Check syncing status
    if os.path.exists(SYNCFLAG):
        logger.error(p4BranchName + ' is under syncing...')
        return
    else:
        os.system('touch ' + SYNCFLAG)

    # Begin p4 sync
    logger.debug("Sync " + p4BranchName + "...")
    command = p4Env
    command += "p4 sync -f -q " + curBranch + "#head"
    ret = os.system(command)

    # Reset syncing status
    os.remove(SYNCFLAG)

    if ret != 0:
        logger.error('Error occurs when sync ' + p4BranchName)
    else:
        # Commit changes to git
        if needInit == 1:
            command = 'git init'
            os.system(command)
        commit_branch(branch, latestCL)

# Git
def commit_branch(branch, strCL):
    # os.system('pwd')
    p4BranchName = "[KantM_%s_MP_Prj]" %branch
    logger.debug("Commit " + p4BranchName + "...")
    command = 'rm -f .gitignore\ngit add .\n'
    command += 'git commit -a -m "$(date +"%Y-%m-%d ...@' + strCL + '")"'
    os.system(command)

# Main
if len(branch) > 0:
    sync_branch(branch)
else:
    sync_branch('MAIN')
    sync_branch('ATSC')
    sync_branch('DVB')
    sync_branch('ISDB')
    sync_branch('AV')
    sync_branch('DTMB')
    sync_branch('HAWKA')
    sync_branch('KANTS')
    sync_branch('TRUNK')
