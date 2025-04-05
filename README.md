# Hearing Aids Fitting Software Update Checkers
A collection of scripts which check hearing aids fitting software directly from their own update servers.

![Total downloads](https://img.shields.io/github/downloads/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/total?label=Total%20downloads&style=for-the-badge)
![Latest release](https://img.shields.io/github/v/release/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?label=Latest%20release&style=for-the-badge)
![Latest release downloads)](https://img.shields.io/github/downloads/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/latest/total?label=Latest%20release%20downloads&style=for-the-badge)
<br/>
![Commits since tagged version](https://img.shields.io/github/commits-since/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/latest?style=for-the-badge)
![Last commit](https://img.shields.io/github/last-commit/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)
![Open issues](https://img.shields.io/github/issues/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)

## What does it do?
This project (\"The Checker\") contains scripts which can check hearing aids fitting software (such as Phonak Target) directly from each own update servers with APIs, so that you can easily know if there is a newer version available, and check corresponding files.

## Currently supported software
This project currently supports:
- Sonova
  - Phonak [Target](https://www.phonak.com/en-int/professionals/innovations/target)
    - Phonak Target Media
    - Phonak Target Sounds
  - Unitron [TrueFit](https://www.unitron.com/global/en_us/professionals/truefit.html)
  - Hansaton [scout](https://www.hansaton.com/en-int/professionals/support/instr.html)
- Demant
  - Oticon [Genie 2](https://www.oticon.com/professionals/tools-and-support/fitting)
  - Oticon Genie
  - Oticon Genie Medical
  - Bernafon [OasisNXT](https://www.bernafon.com/for-professionals/fitting-software)
  - Bernafon OasisNXT Custom
  - Sonic [ExpressFit Pro](https://www.sonici.com/professional-center/professional-support/software-download)
  - Philips [HearSuite](https://www.hearingsolutions.philips.com/for-professionals/hearsuite)
- GN
  - ReSound [Smart Fit](https://pro.resound.com/en-us/products/resound/fsw-2)
  - ReSound [Aventa](https://www.gnhearing.com/en/products/support-materials/fsw-support)
  - ReSound Pro-Counsel
  - Beltone [Solus Max](https://www.gnhearing.com/en/products/beltone/fsw-2)
  - Beltone Solus Pro
  - Beltone Solus
  - Beltone SelectaFit
  - Interton [Fitting](https://www.interton.com/en/professionals/hearing-aid-fitting)
  - Interton Appraise
  - Interton CompuFit
- WS Audiology
  - Signia [Connexx](https://www.signia-pro.com/en/business-support/connexx/)
  - Rexton [Connexx](https://www.rexton.com/en/professional/connexx/)
  - Audio Service Connexx
  - A&M Connexx
  - Widex [Compass GPS](https://www.widexpro.com/en/business-support/compass/) (limited function. See [related issue](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/1#issue-2624522881) for more information and follow up.)
- Starkey
  - Starkey [Pro Fit](https://www.starkeypro.com/products/other-products/software/pro-fit)
  - Starkey [Inspire OS](https://www.starkeypro.com/products/other-products/software/inspire)
  - Starkey [PatientBase](https://patientbase.starkeyhearingtechnologies.com) (limited function. See [related issue](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/5) for more information and follow up.)
- HIMSA: [Noahlink Wireless 2 (NW2)](https://www.himsa.com/products/noahlink-wireless-2/) and [Noahlink Wireless (NW1)](https://www.himsa.com/products/noahlink-wireless/)
  - Driver (limited function. See [related issue](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/6#issue-2966085887) for more information and follow up.)
  - Firmware Upgrader (limited function. See [related issue](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/6#issue-2966085887) for more information and follow up.)
- [Hearing Aids Fitting Software Update Checkers](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/) (\"The Checker\" itself)

## Where to get it
The latest release version of The Checker is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest

NOTE: You need to have the latest version of Python installed for this to work.

You can also get the latest release version via The Checker's built-in \"*Self Update Checker*\" option.

### Pre-release version
If you don't want to wait for the proper release, the fresh pre-release work-in-progress version is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/archive/refs/heads/main.zip

NOTE: You can also get the pre-release version via The Checker's \"*Extra & Legacy Software Update Checkers*\" option.

## How to use it
1. [Install Python](#pre-requirement-install-python) (and reboot your computer) if you don't have it yet
2. Download The Checker from here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest<br/>
   Click on the link and then click on the `Hearing-Aids-Fitting-Software-Update-Checkers.zip` link to download it
3. Extract the ZIP to a folder
4. Go to the extracted folder, double-click the `start-Windows.bat` file and follow the instructions on-screen

NOTE: If The Checker looks like it has frozen, then try disabling `quickEdit` by running the `fixQuickedit.reg` file before running `start-Windows.bat`

**WARNING**: The Checker always tries to upgrade `pip` and some used Python packages. If you are using Python for other reasons and need to keep particular version, be advised to make your own backup or prepare a seperate environment.

### Pre-requirement: Install Python
The following steps only need to be done **ONCE** on each system:
1. Go to: https://www.python.org/downloads/
2. Click on the yellow `Download Python` button and run the installer
3. Make sure you select `Add python.exe to PATH` in the start of the installer, and then click on `Install Now`
4. **Reboot your computer**

NOTE: If you run The Checker (on Windows OS) without Python installed yet, The Checker will refuse to run and bring you to Python download page instead.

## Credits
- [@Blue](https://forum.hearingtracker.com/u/blue/summary): Original author of this project (up to v1.8.0)
- [@pvc](https://forum.hearingtracker.com/u/pvc/summary): Assisting with testing of the script and finding software links
- [@tenkan](https://forum.hearingtracker.com/u/tenkan/summary): Finding the Genie (2) download page links
- [@labuwx](https://github.com/labuwx): Provide [vital information](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/3) about rebranded private label variations of Bernafon OasisNXT
- [@tux-mania](https://github.com/tux-mania): Report bugs and help testing

## Changelog
### v2025.04.05
- Rexton: fix Connexx checker for v9.13.0.1436 by changing target market
- Audio Service: fix Connexx checker for v9.13.0.1420 by changing target market
- Signia/Rexton/Audio Service/A&M: script tweak for easy changing target market and base version

### v2025.04.04
- HIMSA: update Noahlink Wireless firmware upgrader to v3.3.0.0

### v2025.04.02
- Starkey: detailed message if no update available
- Starkey: add checker for PatientBase in the Extra Menu
- Sonic: `ExpressFit` should be `ExpressFit Pro`
- HIMSA: add checker for driver and firmware upgrader in the Extra Menu
- Documents improved

### v2025.03.04
- Starkey: move Inspire OS Checker into Extra Menu
- Oticon: add checker for Genie 2 2025+ and move previous checker (for 2024+) into Extra Menu

### v2025.01.29
- Windows: using code page 65001 (UTF-8)
- Extra Menu: option to show version changes

### v2025.01.28
- Extra Menu: option to check Custom version of Bernafon OasisNXT for private label variations such as `Delight`, `ProAkustik`, `Lisound`, `Specsavers`, `Meditrend`, `GPL`, `Maico`, `Audilab`, `RITM`, `Hoerex`, and `Sonic`
- Audio Service: fix Connexx checker for v9.12.0.1550

### v2024.12.22
- Phonak: fix Target checker for v10.0.1
- Phonak: failsafe for Target Media checker
- Document (README) update

### v2024.12.06
- Fix display on older Windows versions (such as Windows 7 or Windows 8)
- Messages tweak

### v2024.11.27
- Extra Menu: option to download the pre-release version of \"The Checker\" (this project)
- Unlockable achievement (secret)

### v2024.11.26
- Colorful
- Phonak/Unitron/Hansaton: fix manual version re-prompting while format error
- Extra Menu: option to open GitHub page of this project with default web browser
- Self Update Checker: the pre-release version mechanism is not working, reverted

### v2024.11.20
- Turbo mode (secret)
- Checkers: layout adjustment and name alignment

### v2024.11.19
- Menu: Extra menu contains Phonak Target Media and Sounds, and legacy software of Demant brands (Oticon/Bernafon/Sonic/Philips)
- Menu: option names change and layout adjustment
- Self Update Checker: better display new version information
- Fix typo and terms
- Minor display layout adjustment

### v2024.11.18
- Signia/Rexton/Audio Service/A&M: better version info display
- Minor display layout adjustment

### v2024.11.17
- Python: always try to upgrade pip
- Self Update Checker: offer the ability to fetch the latest release version, and the pre-release work-in-progress version
- Self Update Checker: better version info display
- Starkey: better version info display

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
The Hearing Aids Fitting Software Update Checkers (\"The Checker\") checks software update from associated update servers using associated APIs. The Checker does not contain or distribute any hearing aids fitting software or associated content, nor bypass any DRM protection if there is one. If anyone presents an associated company and believes that there are violations of copyright, please open an issue describing how exactly, so there will be a chance to make all parties happy with the resolve.

## WARANTY/SUPPORT
ANYTHING CAME FROM THE HEARING FITTING SOFTWARE UPDATE CHECKERS (\"THE CHECKER\") IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

THE CHECKER IS NOT IN ANY AFFILIATED WITH THE AUTHORS OR COPYRIGHT HOLDERS OF ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER. THEY HAVE NO REQUIREMENT TO PROVIDE ANY SUPPORT OR WARANTY TO ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER. THE AUTHORS AND COPYRIGHT HOLDERS OF ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER RESERVE THE RIGHT TO TERMINATE ANY USAGE OF SOFTWARE ASSOCIATED WITH THE CHECKER.

## DISCLAIMER
The contributors of the Hearing Aids Fitting Software Update Checkers (\"The Checker\") do not take any responsability for what you do with The Checker. All rights and credit go to their rightful owners. No copyright infringement intended.

The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by any of the companies mentioned in The Checker. Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software. The Checker is an UNOFFICIAL project and the use of associated software may be limited.

## Appendix
- Check our [Wiki](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/wiki)!
- Some less common hearing aids software can be checked via their official websites:
  - [Audina ezFIT](https://www.audina.net/en/professional/software)
  - [AUSTAR Fit](https://www.austar-hearing.net/Fitting+Software) and older software can be found [here](https://www.austar-hearing.com/soft-40.html) or [here](https://soft.austar-hearing.com:4431/software-center/#/)
  - [NewSound Fit](https://www.newsound.cn/软件下载)
  - [Persona Medical ProFit](https://personamedical.com/downloads/)
- Widex lunched a new cloud-based fitting software, [Compass Cloud](https://www.widexpro.com/en/business-support/compass-cloud/), for its new hearing aids using Allure platform. Cloud-based software usually updates only at the server (cloud) side.

Note: these software WILL NOT be included in The Checker.

Modern hearing aids fitting software which supports [Noahlink Wireless](https://www.himsa.com/products/noahlink-wireless/) and/or [Noahlink Wireless 2](https://www.himsa.com/products/noahlink-wireless-2/) programming interface should be certified *BEFORE* release. This means one can check [Certified Noahlink Wireless and Noahlink Wireless 2 Modules](https://www.himsa.com/products/noahlink-wireless-2/certified-noahlink-wireless-modules/) for upcoming version of fitting software before its release.
