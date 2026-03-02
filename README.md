# Colorful v2

A lightweight, colorful EmulationStation theme adapted for small-screen handheld devices like the **R36S** (640x480 resolution) and other 1:1 aspect ratio screens. It brings the vibrant, modern aesthetic of the popular **COLORFUL BigBox Theme** to retro handhelds running EmulationStation.

This theme is designed to be fully compatible with:
- **ArkOS**
- **AmberELEC**
- **Pan4ELEC**
- **DarkOS support coming by way of running a script on the device that modifies the theme for compatibility**

## Original Inspiration

This is an adaptation/port of the **COLORFUL BigBox Theme** originally created by **Viking** (with contributions from the LaunchBox community, including code work by @faeran and others).

- Original project page: [COLORFUL BigBox Theme on LaunchBox Forums](https://forums.launchbox-app.com/files/file/2081-colorful-bigbox-theme/)
- Made with love in France – thanks to Viking for the amazing original work and for making it open source/community-accessible!

All assets and design elements from the original are used under **Fair Use** principles for non-commercial, transformative adaptation purposes (porting to a different frontend/resolution/platform with significant modifications for low-res handhelds). No trademarked logos or assets are claimed as original; they are retained only where necessary for the adapted experience and fall under fair use in this context.

## Key Adaptations for Handhelds

- Optimized for **640x480** resolution (native R36S screen) and 1:1 aspect ratios – no stretching or black bars issues
- Scaled down fonts, layouts, and assets to remain readable and performant on small/low-res screens
- Retained the core colorful, elegant style with vibrant platform/system highlights
- Adjusted views (system select, game list, details) to fit handheld navigation

## Screenshots

- **System Selection Screen**

</a>
<a href="screenshots/Arcade_system.png">
  <img src="screenshots/Arcade_system.png" alt="System Selection" width="300" />
</a>
<a href="screenshots/ss_system.png">
  <img src="screenshots/ss_system.png" alt="System Selection2" width="300" />
</a>
<a href="screenshots/PSP_system.png">
  <img src="screenshots/PSP_system.png" alt="System Selection3" width="300" />
</a>  
<br><br><br>

- **Game List View**

</a>
<a href="screenshots/Arcade_gamelist.png">
  <img src="screenshots/Arcade_gamelist.png" alt="Game Selection" width="300" />
</a>
<a href="screenshots/ss_gamelist.png">
  <img src="screenshots/ss_gamelist.png" alt="Game Selection2" width="300" />
</a>
<a href="screenshots/PS_gamelist.png">
  <img src="screenshots/PS_gamelist.png" alt="Game Selection3" width="300" />
</a>
<br><br><br>

- **Customizable Tools Screen**
  
</a>
<a href="screenshots/u_screenshot_022.png">
  <img src="screenshots/u_screenshot_022.png" alt="Game Selection" width="300" />
</a>
<a href="screenshots/u_screenshot_023.png">
  <img src="screenshots/u_screenshot_023.png" alt="Game Selection2" width="300" />
</a>
<a href="screenshots/u_screenshot_024.png">
  <img src="screenshots/u_screenshot_024.png" alt="Game Selection3" width="300" />
</a>
<a href="screenshots/u_screenshot_025.png">
  <img src="screenshots/u_screenshot_025.png" alt="Game Selection2" width="300" />
</a>
<a href="screenshots/u_screenshot_026.png">
  <img src="screenshots/u_screenshot_026.png" alt="Game Selection3" width="300" />
</a>
<br><br><br>

**Game List UI Options**</a>

<a href="screenshots/dc_gamelist.png">
&nbsp;&nbsp;<img src="screenshots/dc_gamelist.png" alt="Game Selection" width="300" />
</a>
<a href="screenshots/Mangmi_PSP.png">
&nbsp;&nbsp;<img src="screenshots/Mangmi_PSP.png" alt="Game Selection2" width="300" />
</a>
<a href="screenshots/Standard_PSP.png">
&nbsp;&nbsp;<img src="screenshots/Standard_PSP.png" alt="Game Selection3" width="300" />
</a>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Glass&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mangmi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard
<br><br><br>

**Description Size Options**</a>

<a href="screenshots/small.png">
&nbsp;&nbsp;<img src="screenshots/small.png" alt="Game Selection" width="300" />
</a>
<a href="screenshots/med.png">
&nbsp;&nbsp;<img src="screenshots/med.png" alt="Game Selection2" width="300" />
</a>
<a href="screenshots/large.png">
&nbsp;&nbsp;<img src="screenshots/large.png" alt="Game Selection3" width="300" />
</a>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Small&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Medium&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Large
<br><br><br>

## Pan4ELEC Specific Features

- Scrollbars
- Storyboards which make element animations possible. For example, the "Dynamic Description" feature in P4E uses storyboards to expand the description and move it further up the screen when the box art fades out video plays. The ensures that there is no empty space on the screen at any point (of course some system views have different size box art and video resolutions, so it does not work perfectly for those. Consider your Favorites folder which could contain many different consoles). This is not available in ArkOS.

## Contributing

Pull requests welcome! Especially for:
- Bug fixes
- Additional system views (or improve exisiting as I have not updated every system view from the original modified Colorful Theme)
- Devices for Tools screen

## License

This adaptation follows the spirit of the original COLORFUL theme (community/open sharing). Use, modify, and distribute freely for personal/non-commercial use. Credit Viking and the original contributors where possible.

Original COLORFUL BigBox Theme © Viking & LaunchBox community.

If you enjoy this, consider supporting the original creator on the LaunchBox forums!

Made for the retro handheld community – enjoy!
