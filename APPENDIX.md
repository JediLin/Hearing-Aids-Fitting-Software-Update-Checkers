# Hearing Aids Fitting Software Update Checkers
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

### Note on Starkey / GN server error

Both Starkey and GN (ReSound, Beltone, Interton, Danavox) has problem making their server's certificate chain complete. This causes server error while checking updates due to verification fail. In order to workaround this issue, The Checker has to update certification paths file manually from time to time, releasing new working versions.

In case of such error and for reasons unable to get the new version of The Checker, you can manually update such file by yourself. Simply browse to [SSL Report of Starkey's update server](https://www.ssllabs.com/ssltest/analyze.html?d=inspireupdater.com) and [SSL Report of GN's update server](https://www.ssllabs.com/ssltest/analyze.html?d=www.gnhearing.com), wait for test complete if in progress, from one of the Certificate marked `Trusted: Yes`, show (expand) its Certification Paths, click on `Download chain` from any of its Trusted Path (see screenshot below), save as `inspireupdater-com-chain.pem` and `www-gnhearing-com-chain.pem` respectly to replace the old ones. This will do the trick.

<img width="1721" height="634" alt="image" src="https://github.com/user-attachments/assets/e21e8358-943d-4d5a-9f69-4669ad368f45" />
