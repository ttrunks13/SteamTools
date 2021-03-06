// Netcode Illuminati Gui
// Created by Ethos_
// Last Modified                               _____________
//___________________________________________.(ş 9/20/2011 ş)
//ŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻŻ
// Credit: Scholle for his work on the ESL GUI helped me figure this out and was the inspiration for it.
"Resource/LoadingDialog.res"
{
	"LoadingDialog"
	{
		"ControlName"		"Frame"
		"fieldName"		"LoadingDialog"
		"xpos"		"322"
		"ypos"		"260"
		"wide"		"548"
		"tall"		"290"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
	}
	
	"PureServerLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"PureServerLabel"
		"xpos"			"24"
		"ypos"			"65"
		"wide"			"512"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"font"			"Verdana"
		"labelText"		"Banner hidden due to the sv_pure settings"
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
	}	
	"NCIBanner"
	{
		"ControlName"		"ImagePanel"
		"fieldName"		"NCIBanner"
		"xpos"			"18"
		"ypos"			"55"
		"wide"			"512"
		"tall"			"64"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"image"			"gfx/vgui/ncibanner"
		"scaleImage"		"0"
	}
	
	"NCIBannerURLLabel"
	{
		"ControlName"		"URLLabel"
		"fieldName"		"NCIBannerURLLabel"
		"xpos"			"18"
		"ypos"			"55"
		"wide"			"512"
		"tall"			"64"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"labelText"		""
		"URLText"		"http://www.netcodeilluminati.com/"
		"textAlignment"		"center"
		"dulltext"		"0"
		"wrap"			"1"
		"brighttext"		"0"
	}
	
	"InfoLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"InfoLabel"
		"xpos"		"20"
		"ypos"		"135"
		"wide"		"512"
		"tall"		"24"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"labelText"		"#GameUI_ParseBaseline"
		"textAlignment"		"west"
		"dulltext"		"0"
		"brighttext"		"0"
	}
	"progress"
	{
		"ControlName"		"ProgressBar"
		"fieldName"		"Progress"
		"xpos"		"20"
		"ypos"		"155"
		"wide"		"430"
		"tall"		"24"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
	}
	"CancelButton"
	{
		"ControlName"		"Button"
		"fieldName"		"CancelButton"
		"xpos"		"460"
		"ypos"		"155"
		"wide"		"72"
		"tall"		"24"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"labelText"		"#GameUI_Cancel"
		"textAlignment"		"west"
		"dulltext"		"0"
		"brighttext"		"0"
		"command"		"Cancel"
		"Default"		"0"
	}
	"TimeRemainingLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"TimeRemainingLabel"
		"xpos"		"20"
		"ypos"		"210"
		"wide"		"260"
		"tall"		"24"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"tabPosition"		"0"
		"labelText"		""
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
	}
	"VACInfoLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"VACInfoLabel"
		"xpos"		"90"
		"ypos"		"200"
		"wide"		"512"
		"tall"		"60"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"wrap"			"0"
		"tabPosition"		"0"
		"labelText"		"#VAC_ConnectingToSecureServer"
		"textAlignment"		"west"
		"dulltext"		"0"
		"brighttext"		"0"
	}
	"VACImage"
	{
		"ControlName"		"ImagePanel"
		"fieldName"		"VACImage"
		"xpos"		"30"
		"ypos"		"210"
		"wide"		"64"
		"tall"		"64"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"border"		""
		"scaleimage"	"1"
		"image"		"resource/icon_vac"
	}
}
