import os
infile = 'ui_main.py'
outfile = 'modules/ui_main.py'

badlines         = ['import resources_rc', 'self.aoa_slider = QSlider(self.comparemethods)', 'self.aoa_slider.setSliderPosition(0)',
                    'self.sideslip_slider = QSlider(self.comparemethods)', 'self.sideslip_slider.setObjectName(u"sideslip_slider")',
                    'self.mach_slider_lookup = QSlider(self.row_1)', 'self.mach_slider_lookup.setValue(5)',
                    'self.gamma_slider_lookup = QSlider(self.row_1)', 'self.gamma_slider_lookup.setMinimum(11)',
                    'self.gamma_slider_lookup.setMaximum(14)',
                    'self.gamma_slider_lookup.setValue(13)', 'self.gamma_slider_lookup.setSliderPosition(130)',
                    'self.aoa_slider_lookup = QSlider(self.row_1)', 'self.beta_slider_lookup = QSlider(self.row_1)']
replacementlines = ['from . resources_rc import *\nfrom superqt import QLabeledRangeSlider, QLabeledDoubleRangeSlider', 'self.aoa_slider = QLabeledRangeSlider(self.comparemethods)',
                    'self.aoa_slider.setSliderPosition([0, 25])', 'self.sideslip_slider = QLabeledRangeSlider(self.comparemethods)',
                    'self.sideslip_slider.setObjectName(u"sideslip_slider")\n        self.sideslip_slider.setSliderPosition([0, 25])',
                    'self.mach_slider_lookup = QLabeledDoubleRangeSlider(self.row_1)', 'self.mach_slider_lookup.setSliderPosition([2, 5])',
                    'self.gamma_slider_lookup = QLabeledDoubleRangeSlider(self.row_1)','self.gamma_slider_lookup.setSliderPosition([1.3, 1.4])',
                    'self.gamma_slider_lookup.setMinimum(1.1)', 'self.gamma_slider_lookup.setMaximum(1.4)', '',
                    'self.aoa_slider_lookup = QLabeledRangeSlider(self.row_1)\n        self.aoa_slider_lookup.setSliderPosition([0, 25])',
                    'self.beta_slider_lookup = QLabeledRangeSlider(self.row_1)\n        self.beta_slider_lookup.setSliderPosition([0, 25])']

with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for i in range(len(badlines)):
            line = line.replace(badlines[i], replacementlines[i])
        fout.write(line)

os.remove(infile)