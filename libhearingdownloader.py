import configparser
from tqdm import tqdm
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import requests
import sys

just_fix_windows_console()
winVer = sys.getwindowsversion()

try:
    import wx
    guiType = "wxpython"
except:
    try:
        from tkinter import filedialog as tkfiledialog
        from tkinter import Tk
        guiType = "tkinter"
    except:
        guiType = None

import time
import math
import os


###
# libhearingdownloader - A useful library for the downloader scripts
###

downloaderVersion = "Pre-release"
#downloaderVersion = "v2025.06.10"
updaterRetries = 3
# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
verboseDebug = config.getboolean('General', 'Verbose', fallback='False')

def normalizePath(path, correctWindowsChars=True):
    if (path[-1] != "/"):
        path += "/"

    if (correctWindowsChars):
        return (path.replace("|", "-").replace("<", "-").replace(">", "-").replace(":", "-").replace('"', "-").replace("?", "-").replace("*", "-"))
    else:
        return path

def printWaranty():
    warantyDisclaimer = [
        "This isn't the usual blah-blah, please read it:",
        "",
        "ANYTHING CAME FROM THE HEARING FITTING SOFTWARE UPDATE CHECKERS (\"THE CHECKER\") IS PROVIDED \"AS IS\",",
        "WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,",
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE",
        "FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,",
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.",
        "",
        "THE CHECKER IS NOT IN ANY AFFILIATED WITH THE AUTHORS OR COPYRIGHT HOLDERS OF ANY SOFTWARE ASSOCIATED WITH THE USE",
        "OF THE CHECKER. THEY HAVE NO REQUIREMENT TO PROVIDE ANY SUPPORT OR WARANTY TO ANY SOFTWARE ASSOCIATED WITH THE USE",
        "OF THE CHECKER. THE AUTHORS AND COPYRIGHT HOLDERS OF ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER RESERVE",
        "THE RIGHT TO TERMINATE ANY USAGE OF SOFTWARE ASSOCIATED WITH THE CHECKER."
    ]
    printDisclaimer(warantyDisclaimer)

def printDisclaimer(disclaimer, disclaimerWidth = 150):
    print("\n\n")
    print (Style.DIM + Fore.RED + "="*disclaimerWidth + Style.RESET_ALL)
    for line in disclaimer:
        leftPad = (disclaimerWidth-len(line))/2
        rightPad = (disclaimerWidth-len(line))/2

        if (leftPad % 1 != 0):
            leftPad = math.floor(leftPad) + 1
            rightPad = math.floor(rightPad)
        
        leftPad = int(leftPad)
        rightPad = int(rightPad)

        print(Style.DIM + Fore.RED + "=" + Style.RESET_ALL + " "*(leftPad-1) + line + " "*(rightPad-1) + Style.DIM + Fore.RED + "=" + Style.RESET_ALL)
    print (Style.DIM + Fore.RED + "="*disclaimerWidth + Style.RESET_ALL)
    
    if (winVer[0] < 10):
        input("\nPress Enter to continue...")
    else:
        input("\nPress " + Fore.GREEN + "Enter" + Style.RESET_ALL + " to continue...")

def selectFromList(selectionList, prompt = "version", headerSeperator='', seperator='\t', numberSeperator='.', confirmationCheck=True):
    targetIndex = ''

    # Selection format in list is:
    # ("displayed text", "description")
    # Use list of tuples over dict just bc
    # Also, you can add more elements to tuple and function ignores them, allowing extra data storage
    # If description is "--", the selection is treated as a header and does not have a number
    while not targetIndex:
        print("")
        indexMap = {} # Map displayed selection numbers with their selections via a dict
        listIndex = 0 # The current index in the list
        selectionNumber = 0 # The current DISPLAYED index in the list (for headers and stuff)

        for selection in selectionList:
            if (selection[1] != "--"):
                strSelectionNumber = str(selectionNumber)
                while len(strSelectionNumber) < len(str(len(selectionList))):
                    strSelectionNumber = " " + strSelectionNumber

                print(Fore.GREEN + str(strSelectionNumber) + Style.RESET_ALL + numberSeperator + " " + Back.BLUE + selection[0] + Style.RESET_ALL + seperator + selection[1])
                indexMap[selectionNumber] = listIndex
                selectionNumber += 1 # Increment displayed index
            else:
                print(headerSeperator + selection[0]) # Header
            listIndex += 1 # Increment list index
        
        try:
            if (winVer[0] < 10):
                targetIndex = int(input("\nPlease select a " + prompt + ": "))
            else:
                targetIndex = int(input("\nPlease select a " + Fore.GREEN + prompt + Style.RESET_ALL + ": "))
        except ValueError:
            targetIndex = -1
        
        if (targetIndex >= 0 and targetIndex < selectionNumber):
            if (not confirmationCheck):
                return indexMap[targetIndex]

            if (winVer[0] < 10):
                if (input("\nYou have selected " + prompt + " (" + selectionList[indexMap[targetIndex]][0] + ") are you sure you want to download it? [(Y)/n] ") == "n"):
                    targetIndex = ''
                else:
                    return indexMap[targetIndex]
            else:
                if (input("\nYou have selected " + prompt + " (" + Fore.YELLOW + selectionList[indexMap[targetIndex]][0] + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
                    targetIndex = ''
                else:
                    return indexMap[targetIndex]
        else:
            print("\nThe " + prompt + " you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again.")
            targetIndex = ''

def selectOutputFolder():
    if (guiType == "wxpython"):
        print("Please select a " + Fore.GREEN + "download location" + Style.RESET_ALL + ", or " + Fore.YELLOW + "Cancel" + Style.RESET_ALL + " to skip")
        time.sleep(2)

        wxApp = wx.App(redirect=False, useBestVisual=True, clearSigInt=True)
        wxDirDialog = wx.DirDialog(None, "Choose a download folder", "")
        dialogReturn = wxDirDialog.ShowModal()

        if (dialogReturn == wx.ID_CANCEL):
            print("\n" + Fore.RED + "No valid directory selected" + Style.RESET_ALL + ", exiting")
            exit()
        else:
            outputDir = wxDirDialog.GetPath()

        wxApp.Destroy()
    elif (guiType == "tkinter"):
        print("Please select a " + Fore.GREEN + "download location" + Style.RESET_ALL + ", or " + Fore.YELLOW + "Cancel" + Style.RESET_ALL + " to skip")
        time.sleep(2)

        tkRoot = Tk()
        tkRoot.withdraw()
        tkRoot.focus()
        tkRoot.focus_force()
        tkRoot.wm_attributes('-topmost', True)

        outputDir = tkfiledialog.askdirectory( parent=tkRoot, title="Choose a download folder")
        if (not outputDir):
            print("\n" + Fore.RED + "No valid directory selected" + Style.RESET_ALL + ", exiting")
            exit()

        tkRoot.destroy()
    elif (guiType == None):
        outputDir = ''
        while not outputDir:
            print("\n\n")
            if (winVer[0] < 10):
            	outputDir = input("Enter an output directory: ")
            else:
                outputDir = input("Enter an " + Fore.GREEN + "output directory" + Style.RESET_ALL + ": ")

            if (outputDir != ""):
                if (winVer[0] < 10):
                    if (input("Confirm download path (" + normalizePath(outputDir, False) + ") [(Y)/n] ") == "n"):
                        outputDir = ''
                else:
                    if (input("Confirm download path (" + Fore.YELLOW + normalizePath(outputDir, False) + Style.RESET_ALL + ") [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
                        outputDir = ''
            else:
                print("The directory you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again.")
                outputDir = ''
    
    return normalizePath(outputDir, False)

def downloadFile(url, saveLocation, downloadDescription):
    os.makedirs('/'.join(saveLocation.split("/")[:-1]), exist_ok=True) # Create path if it doesn't exist
    # Workaround something like 'Akamai-Cache-Status': 'Miss from child'
    streamRetries = updaterRetries
    while streamRetries > 0:
        if(verboseDebug):
            print("\nCounter: " + str(streamRetries) + "\n")
        try:
            fileData = requests.get(url, stream=True) # Get file stream
            chunkSize = 2048

            if (str(fileData.status_code)[0] != '2'):
                print(Fore.RED + "Error downloading file" + Style.RESET_ALL + ": [" + str(fileData.status_code) + "]")
                if streamRetries > 1:
                    print("Try again...")
                exit(1)

            fileSize = int(fileData.headers['content-length'])
            if (fileSize < chunkSize and fileSize > 0):
                chunkSize = fileSize

            if (fileData.status_code == 200):
                with open(saveLocation, 'wb') as fd:
                    for chunk in tqdm(fileData.iter_content(chunk_size=chunkSize), desc=downloadDescription, total=int(int(fileData.headers['content-length'])/chunkSize), unit="B", unit_scale=chunkSize):
                        fd.write(chunk)
            else:
                print("\n\n" + Fore.RED + "ERROR" + Style.RESET_ALL + ": " + str(fileData.status_code))
                if streamRetries > 1:
                    print("Try again...")
                exit(1)

            break
        except:
            pass

        streamRetries -= 1
    if (streamRetries == 0):
        print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Can not get proper file data stream from " + Fore.GREEN + url + Style.RESET_ALL + "\nYou can try to open this URI manually with web browsers. It might work.")
        exit(1)

