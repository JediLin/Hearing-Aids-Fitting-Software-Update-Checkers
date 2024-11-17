# Hearing Aids Fitting Software Update Checkers
![GitHub all releases](https://img.shields.io/github/downloads/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/total?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?label=LATEST%20RELEASE&style=for-the-badge)
<br/>
![GitHub commits since tagged version](https://img.shields.io/github/commits-since/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/latest?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)

A collection of scripts which check hearing aids fitting software directly from their company's servers.

## What does it do?
This repository contains scripts which can check hearing aids fitting software (such as Phonak Target) directly from the software's servers, avoiding the need to distribute copyrighted files. (I am not a lawyer, this is not legal advice, this is merely my opinion.)

## Currently supported software
The script currently supports:
- Sonova
  - Phonak Target
    - Phonak Target Media
    - Phonak Target Sounds
  - Unitron TrueFit
  - Hansaton scout
- Demant
  - Oticon Genie 2 (v2024+, previous verson is hide from default menu)
  - Oticon Genie (hide from default menu)
  - Bernafon OasisNXT (v2024+, previous verson is hide from default menu)
  - Sonic ExpressFit (v2024+, previous verson is hide from default menu)
  - Philips HearSuite (v2024+, previous verson is hide from default menu)
- GN
  - ReSound Smart Fit
  - ReSound Aventa
  - ReSound Pro-Counsel
  - Beltone Solus Max
  - Beltone Solus
  - Beltone SelectaFit
  - Interton Fitting
  - Interton Appraise
  - Interton CompuFit
- WS Audiology
  - Signia Connexx
  - Rexton Connexx
  - Audio Service Connexx
  - A&M Connexx
  - Widex Compass GPS (Currently broken. See [related issue](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/1#issue-2624522881) for more information and follow up.)
- Starkey
  - Starkey Pro Fit
  - Starkey Inspire OS

## Where to get it
The script is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest

Note: You need to have the latest version of Python installed for this to work.

### Pre-release version
If you don't want to wait for the proper release, the fresh work-in-progress version of script is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/archive/refs/heads/main.zip

## How to use it
1. [Install Python](#pre-requirment-install-python) (and reboot your computer) if you don't have it yet
2. Download the script from here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest<br/>
   Click on the link and then click on the `Hearing-Aids-Fitting-Software-Update-Checkers.zip` link to download it
3. Extract the ZIP to a folder
4. Go to the extracted folder, double-click the `start-Windows.bat` file and follow the instructions on-screen

NOTE: If the script looks like it has frozen, then try disabling `quickEdit` by running the `fixQuickedit.reg` file before running `start-Windows.bat`

**WARNING**: This script always tries to upgrade pip and some used Python packages. If you are using Python for other reasons and need to keep particular version, be advised to make your own backup or prepare a seperate environment.

### Pre-requirment: Install Python
The following steps only need to be done **ONCE** on each system:
1. Go to: https://www.python.org/downloads/
2. Click on the yellow `Download Python` button and run the installer
3. Make sure you select `Add python.exe to PATH` in the start of the installer, and then click on `Install Now`
4. **Reboot your computer**

## Credits
- [@Bluebotlabz](https://bluebotlaboratories.com): Original author of this script
- [@pvc](https://forum.hearingtracker.com/u/tenkan): Assisting with testing of the script and finding software links
- [@tenkan](https://forum.hearingtracker.com/u/tenkan): Finding the Genie (2) download page links

## Changelog
### Next version (work-in-progress)
- Python: always try to upgrade pip

### v2024.11.16
- Self Update Checker: automatically and manually check for latest release version of this script itself from GitHub
- README: better instruction on installing Python

### v2024.11.12
- Menu: fix version number display
- Phonak: automatically query for latest version number of Target software while checking Target Media and Sounds, manually input required no more

### v2024.11.11
- Checkers: better provide the latest version information so users can skip the download process without breaking the menu loop
- Widex: better handle server responses
- Remove unused batch file
- Tweak Linux/macOS shell script

### v2024.11.07
- Display: set CMD window/buffer size to 160x30
- Display: fix menu layout for script version number
- Menu: better handle menu loop
- Menu: present Phonak Target Media and Sounds Update Checkers
- Python: check Python first and open its download page if not installed yet
- Python: Require rot-codec to store API keys
- Python: automatically install/upgrade packages
- Oticon/Bernafon/Sonici/Philips: clean-up unnecessary request content
- Oticon/Bernafon/Sonici/Philips: comments on base version required to get further (newer) updates and how to set them if needed in the future
- Widex: show update server responses
- Starkey: using geoIP, baseVer, and baseOS variables for easier updating scripts in the future if needed
- Starkey: better handle null update response
- Phonak: fix version numbering for its scheme changed since v10.0.0

### v2024.08.31
- Name changes
- Versoning scheme changes to date-based
- Add support for A&M Connexx
- Add support for Audio Services Connexx
- Add support for Bernafon OasisNXT v2024+
- Add support for Hansaton scout
- Add support for Oticon Genie 2 v2024+
- Add support for Philips HearSuite v2024+
- Add support for Phonak Target Media
- Add support for Phonak Target Sounds
- Add support for Sonic ExpressFit v2024+
- Add support for Starkey Pro Fit
- Add support for Starkey Inspire
- Fix Starkey intermediate SSL Certificate error
- Fix bugs
- Add exit script
- Pausing after requirement-checks
- Update README

### v1.8.0
- Add native Linux and MacOS Support

### v1.7.6
- Fix debug logging utility bug

### v1.7.5
- Add debug logging utility

### v1.7.4
- Fixed Widex Compass GPS Localisation Errors
- Fixed Typos

### v1.7.3
- Fix bugs

### v1.7.2
- Fix library bug

### v1.7.1
- Fix typos

### v1.7.0
- Add folder selection GUI
- Add support for GN Resound Smart Fit
- Add support for GN Resound Aventa
- Add catch for server index download errors
- Fix download location bugs in Bernafon Oasis & Oticon Genie 2 checkers

### v1.6.3
- Fix folder path selection bug

### v1.6.2
- Fix Unitron checker Bug

### v1.6.1
- Fix Phonak Target checker Bug
- Fix script name mistake

### v1.6.0
- Add support for Rexton Connexx

### v1.5.0
- Add support for OasisNXT
- Fix bugs

### v1.4.0
- Split up the Genie checkers into separate versions
- Update Genie 2 checker to also use updater
- Fix bugs

### v1.3.0
- Add support for Widex Compass GPS

### v1.2.0
- Add support for Unitron TrueFit
- Add downloading progress bar
- Reduce RAM usage when running the script

### v1.1.2
- Fix bugs with selecting download version

### v1.1.0
- Add support for Oticon Genie & Oticon Genie 2

### v1.0.0
- Add support for Phonak Target & Signia Connexx
- Release it publically


## Copyright & DMCA
Since these scripts download data which is publically available online directly from software servers, it does not directly distribute any copyrighted content. If you are a company and are still unhappy with the way one of these scripts works, please open an issue describing how exactly the script violates your software's copyright and it will be modified immediately. (I am not a lawyer, this is not legal advice, this is merely my opinion.)

## WARANTY/SUPPORT
THE SOFTWARE PROVIDED BY THIS SCRIPT IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

THIS SCRIPT UNOFFICIAL AND IS NOT IN ANY AFFILIATED WITH THE AUTHORS OR COPYRIGHT HOLDERS OF ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT. THEY HAVE NO REQUIREMENT TO PROVIDE ANY SUPPORT OR WARANTY TO ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT. THE AUTHORS AND COPYRIGHT HOLDERS OF ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT RESERVE THE RIGHT TO TERMINATE ANY USAGE OF SOFTWARE DOWNLOADED VIA THIS SCRIPT.

## DISCLAIMER
Bluebotlabz and any contributor of these scripts do not take any responsability for what you do using this software. All rights and credit go to their rightful owners. No copyright infringement intended.

Bluebotlabz, any contributor of these scripts, and these checkers are not affiliated with or endorsed by any of the companies mentioned in this repository. Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software. This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited. (I am not a lawyer, this is not legal advice, this is merely my opinion.)

## Appendix
- Modern hearing aids fitting softwares usually work with Noahlink Wireless device. Please check its device driver and firmware update manually at https://www.himsa.com/himsa_download/noahlink-wireless-downloads/
- Starkey fitting softwares (Pro Fit or Inspire OS) need PatientBase to work with. Please check manually at https://patientbase.starkeyhearingtechnologies.com
- Some less common hearing aid brands can be checked via their official websites:
  - [Audina ezFIT](https://www.audina.net/en/professional/software)
  - [AUSTAR Fit](https://www.austar-hearing.net/Fitting+Software) and older software can be found [here](https://www.austar-hearing.com/soft-40.html) or [here](https://soft.austar-hearing.com:4431/software-center/#/)
  - [NewSound Fit](https://www.newsound.cn/软件下载)
  - [Persona Medical ProFit](https://personamedical.com/downloads/)

Note: these software WON'T be included in the checker scripts.
