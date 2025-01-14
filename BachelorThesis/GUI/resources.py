'''
AUTHOR(S):
Michal Kirkegaard

This is a resource file used by the GUI created in "BachelorGUI.pyw". It also serves a a settings file.
'''
# General
FONT = 'monospace 10'
SHUTDOWNFLAG = 'cancel'
def ERROR_MSG(e,ex,step=""):
	return "Error loading file{0}\n\n{1}\n{2}".format(step if step=="" else " at step \"{0}\"".format(step[:-3]),str(e), ex)

# Sizes
ss_WIDTH	= 1500
ss_HEIGHT	= 720

ss_ENTRY_WIDTH = 100

ss_PLOT_DPI		= 70
ss_PLOT_WIDTH	= ss_WIDTH - 300
ss_PLOT_HEIGHT	= ss_HEIGHT - 60
ss_BUTTON_WIDTH = 24
ss_LABEL_WIDTH = 25

# File menu short cuts
fm_sc_NEW = 'Shift-N'
fm_sc_LOAD = 'Shift-L'
fm_sc_SAVE = 'Shift-S'
fm_sc_CLOSE = 'Shift-C'
fm_sc_EXIT = 'Shift-Escape'

# File Formattings
ff_FILETITLE_a = 'Arousal Plot'
ff_FILETAG_a = '.aplot'

ff_FILETITLE_e = 'European Data Format'
ff_FILETAG_e = '.edf'

ff_FILETITLE_s = 'NSRR-formatted Sleep Stage Annotation'
ff_FILETAG_s = '.xml'

# Help menu popup texts
hm_ABOUT_TEXT = [	"About",
					"-"*50,
					"Copyright (C) Michael Kirkegaard, Nicklas Hansen."
					]

hm_FORMAT_TEXT = [	"File Formats",
					"-"*50,
					"- PSG files must be in European Data Format (*.edf file extension) and must contain ECG and PPG signals.",
					"- Sleep stage annotation files must be formatted as per nsrr standards, and containted in an *.xml file.",
					"- Arousal Plots are saved with *.aplot file extension and must be created through this software."
					]
		
hm_COMMANDS_TEXT =	[	"Application Commands",
						"-"*50,
						"-"*20,
						"File Menu",
						"-"*20,
						["- New",	"<"+fm_sc_NEW+">:",		"Make new arousal plot from a PSG and annotation file."],
						["- Load",	"<"+fm_sc_LOAD+">:",	"Load an arousal plot file (i.e. an already analysed file)."],
						["- Save",	"<"+fm_sc_SAVE+">:",	"Save an arousal plot file."],
						["- Close",	"<"+fm_sc_CLOSE+">:",	"Close currently opened arousal plot file."],
						["- Exit",	"<"+fm_sc_EXIT+">:",	"Close application."],
						"",
						"-"*20,
						"Help Menu",
						"-"*20,
						"<Escape> or <Enter> or <Shift-C>:     Close popup windows shortcuts.",
						]

# Summary Text
st_dict = dict([	('aplot_path', 'Directory of aplot file'),
					('edf_path', 'Directory of edf file'),
					('anno_path', 'Directory of annotation file'),
					('rec_dur', 'Recording Duration'),
					('pct_wake', 'Percent time awake'),
					('pct_rem', 'Percent time in REM'),
					('n_arousals', 'Total amount of arousals'),
					('arousals_hr', 'Arousal intensity'),
					('avg_arousal', 'Average arousal duration'),
					('med_arousal', 'Median arousal duration'),
					('std_arousal', 'Standard Deviation')
	])