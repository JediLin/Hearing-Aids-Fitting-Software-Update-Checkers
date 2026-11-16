# How-To: Switch Unitron TrueFit software into custom variations of Aura:fit

> Online version: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/wiki/Cust_aurafit

1. Get and install Unitron [TrueFit](https://www.unitron.com/global/en_us/professionals/truefit.html)
2. Make sure you close TrueFit completely (check system tray too!)
3. Backup `C:\Program Files (x86)\Unitron\Unitron TrueFit\config\app.xml` file just in case
4. Open `C:\Program Files (x86)\Unitron\Unitron TrueFit\config\app.xml` file with elevated administrator privileges (so you can save the changes) using your preferred XML/Text editor (Microsoft Notepad will do if you don't want to install anything else. Microsoft [XML Notepad](https://microsoft.github.io/XmlNotepad/) is free too and highly recommended.)
5. Locate `appDistributor` attribute in the `appSettings` element (XPath: `/configuration/appSettings/@appDistributor`) which should have default value `Unitron`
6. Modify its value as needed (see table below) and save, that's it:

|Value of `appDistributor` attribute|Variation|
|-----------------------------------|---------|
|Unitron|Unitron TrueFit|
|AudioNova|Aura:fit AudioNova|
|UnitronGenericPL|Vista Aura:fit|
|UHCH|Aura:fit Relate|
|SpecSaver|Specsavers Advance|
|Balance|Hansaton|
