from tqdm import tqdm
import requests

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

downloaderVersion = "v2024.11.11"
updaterRetries = 3
verboseDebug = False

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
        ""
        "THE SOFTWARE PROVIDED BY THIS SCRIPT (AND THE SCRIPT ITSELF) IS PROVIDED \"AS IS\"",
        "WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,",
        "INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.",
        "IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,",
        "WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH",
        "THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.",
        "",
        "THIS SCRIPT UNOFFICIAL AND IS NOT IN ANY AFFILIATED WITH THE AUTHORS OR COPYRIGHT HOLDERS OF ANY SOFTWARE DOWNLOADED",
        "VIA THE USE OF THIS SCRIPT. THEY HAVE NO REQUIREMENT TO PROVIDE ANY SUPPORT OR WARANTY TO ANY SOFTWARE DOWNLOADED",
        "VIA THE USE OF THIS SCRIPT. THE AUTHORS AND COPYRIGHT HOLDERS OF ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT",
        "RESERVE THE RIGHT TO TERMINATE ANY USAGE OF SOFTWARE DOWNLOADED VIA THIS SCRIPT"
    ]
    printDisclaimer(warantyDisclaimer)

def printDisclaimer(disclaimer, disclaimerWidth = 150):
    print("\n\n")
    print ("="*disclaimerWidth)
    for line in disclaimer:
        leftPad = (disclaimerWidth-len(line))/2
        rightPad = (disclaimerWidth-len(line))/2

        if (leftPad % 1 != 0):
            leftPad = math.floor(leftPad) + 1
            rightPad = math.floor(rightPad)
        
        leftPad = int(leftPad)
        rightPad = int(rightPad)

        print("=" + " "*(leftPad-1) + line + " "*(rightPad-1) + "=")
    print ("="*disclaimerWidth)
    input("Press enter to continue...")

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

                print(str(strSelectionNumber) + numberSeperator + " " + selection[0] + seperator + selection[1])
                indexMap[selectionNumber] = listIndex
                selectionNumber += 1 # Increment displayed index
            else:
                print(headerSeperator + selection[0]) # Header
            listIndex += 1 # Increment list index
        
        try:
            targetIndex = int(input("Please select a " + prompt + ": "))
        except ValueError:
            targetIndex = -1
        
        if (targetIndex >= 0 and targetIndex < selectionNumber):
            if (not confirmationCheck):
                return indexMap[targetIndex]

            if (input("You have selected " + prompt + " (" + selectionList[indexMap[targetIndex]][0] + ") are you sure you want to download it? [Y/n] ") == "n"):
                targetIndex = ''
            else:
                return indexMap[targetIndex]
        else:
            print("The " + prompt + " you have selected is invalid.\nPlease try again.")
            targetIndex = ''

def selectOutputFolder():
    if (guiType == "wxpython"):
        print("Please select a download location")
        time.sleep(2)

        wxApp = wx.App(redirect=False, useBestVisual=True, clearSigInt=True)
        wxDirDialog = wx.DirDialog(None, "Choose a download folder", "")
        dialogReturn = wxDirDialog.ShowModal()

        if (dialogReturn == wx.ID_CANCEL):
            print("No valid directory selected, exiting")
            exit()
        else:
            outputDir = wxDirDialog.GetPath()

        wxApp.Destroy()
    elif (guiType == "tkinter"):
        print("Please select a download location")
        time.sleep(2)

        tkRoot = Tk()
        tkRoot.withdraw()
        tkRoot.focus()
        tkRoot.focus_force()
        tkRoot.wm_attributes('-topmost', True)

        outputDir = tkfiledialog.askdirectory( parent=tkRoot, title="Choose a download folder")
        if (not outputDir):
            print("No valid directory selected, exiting")
            exit()

        tkRoot.destroy()
    elif (guiType == None):
        outputDir = ''
        while not outputDir:
            print("\n\n")
            outputDir = input("Enter an output directory: ")
            if (outputDir != ""):
                if (input("Confirm download path (" + normalizePath(outputDir, False) + ") [Y/n] ") == "n"):
                    outputDir = ''
            else:
                print("The directory you have selected is invalid.\nPlease try again.")
                outputDir = ''
    
    return normalizePath(outputDir, False)

def downloadFile(url, saveLocation, downloadDescription):
    os.makedirs('/'.join(saveLocation.split("/")[:-1]), exist_ok=True) # Create path if it doesn't exist
    fileData = requests.get(url, stream=True) # Get file stream

    chunkSize = 2048
    
    if (str(fileData.status_code)[0] != '2'):
        print("Error downloading file: [" + str(fileData.status_code) + "]")
        exit(1)

    fileSize = int(fileData.headers['content-length'])
    if (fileSize < chunkSize and fileSize > 0):
        chunkSize = fileSize

    if (fileData.status_code == 200):
        with open(saveLocation, 'wb') as fd:
            for chunk in tqdm(fileData.iter_content(chunk_size=chunkSize), desc=downloadDescription, total=int(int(fileData.headers['content-length'])/chunkSize), unit="B", unit_scale=chunkSize):
                fd.write(chunk)
    else:
        print("\n\nERROR: " + str(fileData.status_code))
        exit(1)
