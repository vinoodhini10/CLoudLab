import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import datetime
dt = datetime.datetime.today()
TOKEN ='sl.BKvaOS3F0pNi2_M2VOcriWt3n-DcgImHCi2w_gQYZpO-wbAggV6oz0FvIZ58fPr2Xo1JVOVSzc0IV4HeZ5YyeDKxzbHOCMtc3byChS5xJbvU5rrHyzssyifTaBa9-7kUPFHvBIU'
LOCALFILE = 'D:\\6th SEM\CLOUD COMPUTING\\LAB TERMINAL\\KVM COMMANDS.txt'
BACKUPPATH = f"/KVM COMMANDS.txt"
def backup(localFile, backupPath):
    with open(localFile, 'rb') as f:
        print("Uploading " + localFile + " to Dropbox as " + backupPath + "...")
        try:
            dbx.files_upload(f.read(), backupPath, mode=WriteMode('overwrite'))
        except ApiError as err:
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()
if __name__ == '__main__':
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)
    try:
        dbx.users_get_current_account()
    except AuthError:
        sys.exit("ERROR: Invalid access token; try re-generating an "
                 "access token from the app console on the web.")
    backup(LOCALFILE, BACKUPPATH)
    print("Done!")


#python -u "your file pathalong with the python file.py"
