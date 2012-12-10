//             ______________________
//___________.( h0lmGUI�v4.1 by h0lm ).___________
//������������������������������������������������
// Command Menu Definition
// 
// "filename.res"
// {
//    "menuitem1"
//    {
//      "label"		"#GoToB"          // lable name shown in game, # = localized string
//      "command"	"echo hallo"      // a command string
//      "toggle"	"sv_cheats" 	  // a 0/1 toggle cvar 
//      "rule"		"map"             // visibility rules : "none", "team", "map","class"	
//      "ruledata"	"de_dust"	  // rule data, eg map name or team number
//    }
//   
//   "menuitem2"
//   {
//	...
//   }
//
//   ...
//
// }
//
//--------------------------------------------------------
// Everything below here is editable

"spectatormenu.res"
{
	"menuitem1"
	{
		"label"		"#Valve_Close"	// name shown in game
		"command"	"spec_menu 0"	// type data
	}
	
	"menuitem2"
	{
		"label"		"Overview Settings"
		
		"menuitem21"
		{
			"label"		"#Valve_Overview_Locked"
			"toggle"	"overview_locked"
		}
		
		"menuitem22"
		{
			"label"		"#Valve_Overview_Names"
			"toggle"	"overview_names"
		}
		
		"menuitem23"
		{
			"label"		"#Valve_Overview_Health"
			"toggle"	"overview_health"
		}
		
		"menuitem24"
		{
			"label"		"#Valve_Overview_Tracks"
			"toggle"	"overview_tracks"
		}
	}
	
	"menuitem3"
	{
		"label"		"Overview Mode"
						
		"menuitem31"
		{
			"label"		"#Valve_Overview_Off"
			"command"	"overview_mode 0"
		}
		
		"menuitem32"
		{
			"label"		"#Valve_Overview_Small"
			"command"	"overview_mode 1"
		}
		
		"menuitem33"
		{
			"label"		"#Valve_Overview_Large"
			"command"	"overview_mode 2"
		}
		
		"menuitem34"
		{
			"label"		"#Valve_Overview_ZoomIn"
			"command"	"overview_zoom 1.1 0.1 rel"
		}
		
		"menuitem35"
		{
			"label"		"#Valve_Overview_ZoomOut"
			"command"	"overview_zoom 0.9 0.1 rel"
		}
	}
	
	"menuitem4"
	{
		"label"		"General Settings"
		
		"menuitem41"
		{
			"label"		"#Valve_Auto_Director"
			"toggle"	"spec_autodirector"
		}
		
		"menuitem42"
		{
			"label"		"Net_Graph"
			"toggle"	"net_graph"
		}
		
		"menuitem43"
		{
			"label"		"#Valve_Show_Scores"
			"command"	"togglescores"
		}
		
		"menuitem53"
		{
			"label"		"Wait, what server am I on?"
			"command"	"spec_help"
		}
		
	}

}

//________________________________________________
//�����������'( h0lmGUI�v4.1 by h0lm )'�����������
//             ����������������������