
import sys
import os
import platform
import pickle

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
from PySide6 import QtWidgets, QtGui
import numpy as np
from mpl_toolkits import mplot3d
import math
import stl as mesh
from SHABPy import Vehicle, SHABPy

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Super/Hypersonic Arbitrary Body Program"
        description = "S/HABP - Modified by UNSW Hypersonics Group"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # STL MESH Initialise
        # ///////////////////////////////////////////////////////////////
        widgets.stl_mesh = None
        widgets.fileName = None
        widgets.Vehicle  = None

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.open_stl_button.clicked.connect(self.buttonClick)
        widgets.btn_pressure.clicked.connect(self.buttonClick)
        widgets.btn_create_vehicle.clicked.connect(self.buttonClick)
        widgets.btn_plotpressure.clicked.connect(self.buttonClick)
        widgets.btn_plots.clicked.connect(self.buttonClick)
        widgets.btn_compareMethods.clicked.connect(self.buttonClick)
        widgets.btn_meshResizer.clicked.connect(self.buttonClick)
        widgets.Lock_scale.clicked.connect(self.ClickRadio)
        widgets.btn_scale.clicked.connect(self.ScaleMesh)
        widgets.x_rotate_right.clicked.connect(self.RotateXRight)
        widgets.x_rotate_left.clicked.connect(self.RotateXLeft)
        widgets.y_rotate_right.clicked.connect(self.RotateYRight)
        widgets.y_rotate_left.clicked.connect(self.RotateYLeft)
        widgets.z_rotate_right.clicked.connect(self.RotateZRight)
        widgets.z_rotate_left.clicked.connect(self.RotateZLeft)
        widgets.btn_translate.clicked.connect(self.Translate)
        widgets.btn_saveas.clicked.connect(self.SaveAs)
        widgets.compare_export_csv.clicked.connect(self.CompareExportPkl)
        widgets.btn_tables.clicked.connect(self.buttonClick)
        widgets.btn_export_lookup.clicked.connect(self.ExportLookupTable)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes/py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def isFloat(self, val):
        try:
            float(val)
            return True
        except ValueError:
            return False

    def RefreshPreview(self, plotwidget):
        plotwidget.axes.clear()

        face = widgets.stl_mesh.vectors
        xx = widgets.stl_mesh.x
        yy = widgets.stl_mesh.y
        zz = widgets.stl_mesh.z

        plotwidget.axes.add_collection(mplot3d.art3d.Poly3DCollection(face))

        rx = (np.max(xx) - np.min(xx))
        ry = (np.max(yy) - np.min(yy))
        rz = (np.max(zz) - np.min(zz))

        minx = np.min(xx)
        miny = np.min(yy)
        minz = np.min(zz)

        widgets.val_len.setText(str(rx))
        widgets.val_span.setText(str(ry))
        widgets.val_height.setText(str(rz))

        widgets.minx_val.setText(str(minx))
        widgets.miny_val.setText(str(miny))
        widgets.minz_val.setText(str(minz))

        cx = (np.max(xx) + np.min(xx)) / 2
        cy = (np.max(yy) + np.min(yy)) / 2
        cz = (np.max(zz) + np.min(zz)) / 2

        r = np.max([rx, ry, rz])

        plotwidget.axes.quiver(minx - r/6, cy, cz, r/6, 0, 0, color='red')

        plotwidget.axes.set_xbound(cx - r / 1.5, cx + r / 1.5)
        plotwidget.axes.set_ybound(cy - r / 1.5, cy + r / 1.5)
        plotwidget.axes.set_zbound(cz - r / 1.5, cz + r / 1.5)

        plotwidget.axes.set_xlabel('x axis (m)')
        plotwidget.axes.set_ylabel('y axis (m)')
        plotwidget.axes.set_zlabel('z axis (m)')

        plotwidget.canvas.draw_idle()

    def LoadPreview(self):
        if widgets.fileName:
            widgets.stl_mesh = mesh.Mesh.from_file(widgets.fileName)
        if widgets.stl_mesh:
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def PlotComparison(self, x_axis, y_axis, x_label, y_label, methods, legend):
        x_size = np.shape(x_axis)
        y_size = np.shape(y_axis)

        widgets.comparison_plot.axes.clear()

        if x_size[0] == y_size[0]:
            for i in range(len(methods)):
                widgets.comparison_plot.axes.plot(x_axis[i, :], y_axis[i, :])
        else:
            for i in range(len(methods)):
                widgets.comparison_plot.axes.plot(x_axis, y_axis[i, :])

        widgets.comparison_plot.axes.set_xlabel(x_label)
        widgets.comparison_plot.axes.set_ylabel(y_label)
        widgets.comparison_plot.axes.legend(legend)
        widgets.comparison_plot.axes.grid(True, color="gray")
        widgets.comparison_plot.canvas.draw_idle()

    def PlotPressureMap(self, alpha, beta):
        xx = widgets.stl_mesh.x
        yy = widgets.stl_mesh.y
        zz = widgets.stl_mesh.z
        face = widgets.stl_mesh.vectors
        [cp, cx, cy, cz, cmx, cmy, cmz, cl, cd, cyPrime] = SHABPy.RunSHABPy(alpha, beta, widgets.Vehicle)
        range = max(cp) - min(cp)
        cp = (cp - min(cp)) / range
        r = cp
        g = np.ones(len(cp)) * 0
        b = -cp + 1

        fcs = np.zeros((len(cp), 3))
        fcs[:, 0] = r
        fcs[:, 1] = g
        fcs[:, 2] = b

        widgets.cl_val.setText(str(cl))
        widgets.cd_val.setText(str(cd))
        widgets.cyprime_val.setText(str(cyPrime))
        widgets.cx_val.setText(str(cx))
        widgets.cy_val.setText(str(cy))
        widgets.cz_val.setText(str(cz))
        widgets.cmx_val.setText(str(cmx))
        widgets.cmy_val.setText(str(cmy))
        widgets.cmz_val.setText(str(cmz))

        widgets.pressureplot.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(face, facecolor=fcs))

        scale = widgets.Vehicle.mesh.points.flatten()
        widgets.pressureplot.axes.auto_scale_xyz(scale, scale, scale)

        rx = (np.max(xx) - np.min(xx))
        ry = (np.max(yy) - np.min(yy))
        rz = (np.max(zz) - np.min(zz))

        cx = (np.max(xx) + np.min(xx)) / 2
        cy = (np.max(yy) + np.min(yy)) / 2
        cz = (np.max(zz) + np.min(zz)) / 2

        r = np.max([rx, ry, rz])

        widgets.pressureplot.axes.set_xbound(cx - r / 1.5, cx + r / 1.5)
        widgets.pressureplot.axes.set_ybound(cy - r / 1.5, cy + r / 1.5)
        widgets.pressureplot.axes.set_zbound(cz - r / 1.5, cz + r / 1.5)

        widgets.pressureplot.canvas.draw_idle()


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_tables":
            widgets.stackedWidget.setCurrentWidget(widgets.lookup)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_meshResizer":
            widgets.stackedWidget.setCurrentWidget(widgets.MeshResizer)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_pressure":
            widgets.stackedWidget.setCurrentWidget(widgets.pressurepage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "open_stl_button":
            path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select STL file', '', 'Models (*.stl)')
            widgets.FileLocationText.setText(path)
            widgets.fileName = path
            self.LoadPreview()

        if btnName == "btn_create_vehicle":
            if widgets.stl_mesh:
                if self.isFloat(widgets.mean_aero_chord_val.text()) and self.isFloat(widgets.span_val.text()) and self.isFloat(widgets.reference_area_val.text()) and self.isFloat(widgets.cgx_val.text()) and self.isFloat(widgets.cgy_val.text()) and self.isFloat(widgets.cgz_val.text()) and self.isFloat(widgets.mass_val.text()):
                    widgets.vehicle_status.setText('Vehicle Successfully Loaded')
                    widgets.compare_vehiclestatus.setText('Vehicle Successfully Loaded')
                    widgets.vehicle_status.setStyleSheet('color: rgb(50,205,50)')
                    widgets.compare_vehiclestatus.setStyleSheet('color: rgb(50,205,50)')
                    widgets.Vehicle = Vehicle.Vehicle(5, 1.4, float(widgets.mean_aero_chord_val.text()), float(widgets.span_val.text()), float(widgets.reference_area_val.text()), float(widgets.cgx_val.text()), float(widgets.cgy_val.text()), float(widgets.cgz_val.text()), float(widgets.mass_val.text()), widgets.fileName, widgets.compression_method_box.currentIndex(), widgets.expansion_method_box.currentIndex(), 1, 1, 1, 1)
                    #M, gamma, cbar, span, sref, xref, yref, zref, m, stlfile, compression, expansion, Ixx, Iyy, Izz, Ixz
                else:
                    widgets.vehicle_status.setText('All Vehicle Values Must Be Set Correctly')
                    widgets.vehicle_status.setStyleSheet('color: rgb(255,127,80)')
            else:
                widgets.vehicle_status.setText('Please Load STL File')
                widgets.vehicle_status.setStyleSheet('color: rgb(255,127,80)')

        if btnName == "btn_plotpressure":
            if widgets.Vehicle:
                if self.isFloat(widgets.p_mach_val.text()) and self.isFloat(widgets.p_gamma_val.text()) and self.isFloat(widgets.p_alpha_val.text()) and self.isFloat(widgets.p_beta_val.text()):
                    widgets.Vehicle.UpdateCompression(widgets.p_compression_val.currentIndex())
                    widgets.Vehicle.UpdateExpansion(widgets.p_expansion_val.currentIndex())
                    self.PlotPressureMap(float(widgets.p_alpha_val.text())*math.pi/180, float(widgets.p_alpha_val.text())*math.pi/180)

        if btnName == "btn_plots":
            widgets.stackedWidget.setCurrentWidget(widgets.comparemethods)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == 'btn_compareMethods':
            if widgets.Vehicle:
                if widgets.comp_newtonian.isChecked() or widgets.comp_busemann.isChecked() or widgets.comp_hankey.isChecked() or widgets.comp_mn.isChecked() or widgets.comp_npm.isChecked() or widgets.comp_vandyke.isChecked():
                    methods = []
                    legend  = []
                    if widgets.comp_newtonian.isChecked():
                        methods.append(1)
                        legend.append('Newtonian')
                    if widgets.comp_npm.isChecked():
                        methods.append(2)
                        legend.append('Newtonian Prandtl Meyer')
                    if widgets.comp_mn.isChecked():
                        methods.append(3)
                        legend.append('Modified Newtonian')
                    if widgets.comp_hankey.isChecked():
                        methods.append(4)
                        legend.append('Hankey Flat Surface')
                    if widgets.comp_vandyke.isChecked():
                        methods.append(5)
                        legend.append('Van Dyke Unified')
                    if widgets.comp_busemann.isChecked():
                        methods.append(6)
                        legend.append('Busemann Second Order Theory')
                    if self.isFloat(widgets.compare_MachNumber.text()):
                        widgets.Vehicle.M = float(widgets.compare_MachNumber.text())
                    if self.isFloat(widgets.Compare_gamma.text()):
                        widgets.Vehicle.gamma = float(widgets.Compare_gamma.text())

                    aoa_values = widgets.aoa_slider.value()
                    steps    = 50
                    aoa_step = (aoa_values[1] - aoa_values[0])/steps
                    aoa_range = np.arange(aoa_values[0], aoa_values[1], aoa_step)
                    aoa_range = aoa_range*np.pi/180

                    side_values = widgets.sideslip_slider.value()
                    side_step = (side_values[1] - side_values[0]) / steps
                    side_range = np.arange(side_values[0], side_values[1], side_step)
                    side_range = side_range * np.pi / 180

                    cl = np.zeros((len(methods), len(aoa_range)))
                    cd = np.zeros((len(methods), len(aoa_range)))
                    cx = np.zeros((len(methods), len(aoa_range)))
                    cy = np.zeros((len(methods), len(aoa_range)))
                    cz = np.zeros((len(methods), len(aoa_range)))
                    cmx = np.zeros((len(methods), len(aoa_range)))
                    cmy = np.zeros((len(methods), len(aoa_range)))
                    cmz = np.zeros((len(methods), len(aoa_range)))
                    cyPrime = np.zeros((len(methods), len(aoa_range)))

                    cl_b = np.zeros((len(methods), len(side_range)))
                    cd_b = np.zeros((len(methods), len(side_range)))
                    cx_b = np.zeros((len(methods), len(side_range)))
                    cy_b = np.zeros((len(methods), len(side_range)))
                    cz_b = np.zeros((len(methods), len(side_range)))
                    cmx_b = np.zeros((len(methods), len(side_range)))
                    cmy_b = np.zeros((len(methods), len(side_range)))
                    cmz_b = np.zeros((len(methods), len(side_range)))
                    cyPrime_b = np.zeros((len(methods), len(side_range)))

                    for j in range(len(methods)):
                        widgets.Vehicle.UpdatePanelMethod(methods[j])
                        for i in range(len(aoa_range)):
                            [cp, cx[j, i], cy[j, i], cz[j, i], cmx[j, i], cmy[j, i], cmz[j, i], cl[j, i], cd[j, i], cyPrime[j, i]] = SHABPy.RunSHABPy(aoa_range[i], 0, widgets.Vehicle)
                        for k in range(len(side_range)):
                            [cp, cx_b[j, k], cy_b[j, k], cz_b[j, k], cmx_b[j, k], cmy_b[j, k], cmz_b[j, k], cl_b[j, k], cd_b[j, k], cyPrime_b[j, k]] = SHABPy.RunSHABPy(0, side_range[k], widgets.Vehicle)

                    plot_name = str(widgets.Compare_PlotName.currentText())

                    if plot_name == 'CL v CD':
                        self.PlotComparison(cl, cd, 'CL', 'CD', methods, legend)
                    if plot_name == 'AoA v CL':
                        self.PlotComparison(aoa_range*180/np.pi, cl, 'Angle of Attack (Degrees)', 'CL', methods, legend)
                    if plot_name == 'AoA v CD':
                        self.PlotComparison(aoa_range*180/np.pi, cd, 'Angle of Attack (Degrees)', 'CD', methods, legend)
                    if plot_name == 'AoA v Cy\'':
                        self.PlotComparison(aoa_range*180/np.pi, cyPrime, 'Angle of Attack (Degrees)', 'Cy\'', methods, legend)
                    if plot_name == 'AoA v Cx':
                        self.PlotComparison(aoa_range*180/np.pi, cx, 'Angle of Attack (Degrees)', 'Cx', methods, legend)
                    if plot_name == 'AoA v Cy':
                        self.PlotComparison(aoa_range*180/np.pi, cy, 'Angle of Attack (Degrees)', 'Cy', methods, legend)
                    if plot_name == 'AoA v Cz':
                        self.PlotComparison(aoa_range*180/np.pi, cz, 'Angle of Attack (Degrees)', 'Cz', methods, legend)
                    if plot_name == 'AoA v Cmx':
                        self.PlotComparison(aoa_range*180/np.pi, cmx, 'Angle of Attack (Degrees)', 'Cmx', methods, legend)
                    if plot_name == 'AoA v Cmy':
                        self.PlotComparison(aoa_range*180/np.pi, cmy, 'Angle of Attack (Degrees)', 'Cmy', methods, legend)
                    if plot_name == 'AoA v Cmz':
                        self.PlotComparison(aoa_range*180/np.pi, cmz, 'Angle of Attack (Degrees)', 'Cmz', methods, legend)
                    if plot_name == 'Sideslip v CL':
                        self.PlotComparison(side_range*180/np.pi, cl_b, 'Sideslip Angle (Degrees)', 'CL', methods, legend)
                    if plot_name == 'Sideslip v CD':
                        self.PlotComparison(side_range*180/np.pi, cd_b, 'Sideslip Angle (Degrees)', 'CD', methods, legend)
                    if plot_name == 'Sideslip v Cy\'':
                        self.PlotComparison(side_range*180/np.pi, cyPrime_b, 'Sideslip Angle (Degrees)', 'Cy\'', methods, legend)
                    if plot_name == 'Sideslip v Cx':
                        self.PlotComparison(side_range*180/np.pi, cx_b, 'Sideslip Angle (Degrees)', 'Cx', methods, legend)
                    if plot_name == 'Sideslip v Cy':
                        self.PlotComparison(side_range*180/np.pi, cy_b, 'Sideslip Angle (Degrees)', 'Cy', methods, legend)
                    if plot_name == 'Sideslip v Cz':
                        self.PlotComparison(side_range*180/np.pi, cz_b, 'Sideslip Angle (Degrees)', 'Cz', methods, legend)
                    if plot_name == 'Sideslip v Cmx':
                        self.PlotComparison(side_range*180/np.pi, cmx_b, 'Sideslip Angle (Degrees)', 'Cmx', methods, legend)
                    if plot_name == 'Sideslip v Cmy':
                        self.PlotComparison(side_range*180/np.pi, cmy_b, 'Sideslip Angle (Degrees)', 'Cmy', methods, legend)
                    if plot_name == 'Sideslip v Cmz':
                        self.PlotComparison(side_range*180/np.pi, cmz_b, 'Sideslip Angle (Degrees)', 'Cmz', methods, legend)

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        #if event.buttons() == Qt.LeftButton:
            #print('Mouse click: LEFT CLICK')
        #if event.buttons() == Qt.RightButton:
            #print('Mouse click: RIGHT CLICK')

    def ClickRadio(self):
        if widgets.Lock_scale.isChecked():
            widgets.y_scale.clear()
            widgets.z_scale.clear()
            widgets.y_scale.setEnabled(False)
            widgets.z_scale.setEnabled(False)
        else:
            widgets.y_scale.setEnabled(True)
            widgets.z_scale.setEnabled(True)

    def UpdateMesh(self):
        widgets.stl_mesh.update_areas()
        widgets.stl_mesh.update_units()
        widgets.stl_mesh.update_centroids()
        widgets.stl_mesh.update_normals()
        widgets.stl_mesh.update_max()
        widgets.stl_mesh.update_min()

    def UpdateVehicle(self):
        widgets.Vehicle.mesh = widgets.stl_mesh

    def ScaleMesh(self):
        if widgets.stl_mesh:
            if widgets.lock_scale_radio.isChecked():
                scale_x = widgets.x_scale.text()
                if self.isFloat(scale_x):
                    scale_x = float(scale_x)
                    widgets.stl_mesh.points  = widgets.stl_mesh.points*scale_x
                    self.UpdateMesh()
                    self.RefreshPlot()
                    widgets.x_scale.clear()
            else:
                scale_x = widgets.x_scale.text()
                scale_y = widgets.y_scale.text()
                scale_z = widgets.z_scale.text()
                if self.isFloat(scale_x) and self.isFloat(scale_y) and self.isFloat(scale_z):
                    scale_x = float(scale_x)
                    scale_y = float(scale_y)
                    scale_z = float(scale_z)
                    widgets.stl_mesh.x = widgets.stl_mesh.x*scale_x
                    widgets.stl_mesh.y = widgets.stl_mesh.y*scale_y
                    widgets.stl_mesh.z = widgets.stl_mesh.z*scale_z
                    self.UpdateMesh()
                    self.RefreshPreview(widgets.MplWidget)
                    self.RefreshPreview(widgets.MeshEditorPreview)
                    if widgets.Vehicle:
                        self.UpdateVehicle()

                    widgets.x_scale.clear()
                    widgets.y_scale.clear()
                    widgets.z_scale.clear()

    def RotateXRight(self):
        if widgets.stl_mesh:
            widgets.stl_mesh.rotate([0.5, 0.0, 0.0], math.radians(90))
            self.UpdateMesh()
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def RotateXLeft(self):
        if widgets.stl_mesh:
            widgets.stl_mesh.rotate([0.5, 0.0, 0.0], math.radians(-90))
            self.UpdateMesh()
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def RotateYRight(self):
        if widgets.stl_mesh:
            widgets.stl_mesh.rotate([0.0, 0.5, 0.0], math.radians(90))
            self.UpdateMesh()
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def RotateYLeft(self):
        if widgets.stl_mesh:
            widgets.stl_mesh.rotate([0.0, 0.5, 0.0], math.radians(-90))
            self.UpdateMesh()
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def RotateZRight(self):
        if widgets.stl_mesh is not None:
            widgets.stl_mesh.rotate([0.0, 0.0, 0.5], math.radians(90))
            self.UpdateMesh()
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def RotateZLeft(self):
        if widgets.stl_mesh is not None:
            widgets.stl_mesh.rotate([0.0, 0.0, 0.5], math.radians(-90))
            self.UpdateMesh()
            self.RefreshPreview(widgets.MplWidget)
            self.RefreshPreview(widgets.MeshEditorPreview)

    def Translate(self):
        if widgets.stl_mesh is not None:
            tx = widgets.x_translate.text()
            ty = widgets.y_translate.text()
            tz = widgets.z_translate.text()

            if self.isfloat(tx) and self.isfloat(ty) and self.isfloat(tz):
                tx = float(tx)
                ty = float(ty)
                tz = float(tz)

                widgets.stl_mesh.x += tx
                widgets.stl_mesh.y += ty
                widgets.stl_mesh.z += tz

                self.UpdateMesh()
                self.RefreshPreview(widgets.MplWidget)
                self.RefreshPreview(widgets.MeshEditorPreview)

    def SaveAs(self):
        if widgets.stl_mesh:
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Mesh As", "",
                                                  "All Files (*);;Stl Files (*.stl)")
            if fileName:
                if len(fileName) > 4:
                    extension = fileName[-4:].lower()
                    if extension == '.stl':
                        widgets.stl_mesh.save(fileName)
                        widgets.fileName = fileName
                        widgets.FileLocationText.setText(widgets.fileName)
                    else:
                        fileName += '.stl'
                        widgets.stl_mesh.save(fileName)
                        widgets.fileName = fileName
                        widgets.FileLocationText.setText(widgets.fileName)
                else:
                    fileName += '.stl'
                    widgets.stl_mesh.save(fileName)
                    widgets.fileName = fileName
                    widgets.FileLocationText.setText(widgets.fileName)

    def CompareExportPkl(self):
        if widgets.Vehicle:
            if widgets.comp_newtonian.isChecked() or widgets.comp_busemann.isChecked() or widgets.comp_hankey.isChecked() or widgets.comp_mn.isChecked() or widgets.comp_npm.isChecked() or widgets.comp_vandyke.isChecked():
                methods = []
                if widgets.comp_newtonian.isChecked():
                    methods.append(1)
                if widgets.comp_npm.isChecked():
                    methods.append(2)
                if widgets.comp_mn.isChecked():
                    methods.append(3)
                if widgets.comp_hankey.isChecked():
                    methods.append(4)
                if widgets.comp_vandyke.isChecked():
                    methods.append(5)
                if widgets.comp_busemann.isChecked():
                    methods.append(6)
                if self.isFloat(widgets.compare_MachNumber.text()):
                    widgets.Vehicle.M = float(widgets.compare_MachNumber.text())
                if self.isFloat(widgets.Compare_gamma.text()):
                    widgets.Vehicle.gamma = float(widgets.Compare_gamma.text())

                aoa_values = widgets.aoa_slider.value()
                steps = 50
                aoa_step = (aoa_values[1] - aoa_values[0]) / steps
                aoa_range = np.arange(aoa_values[0], aoa_values[1], aoa_step)
                aoa_range = aoa_range * np.pi / 180

                side_values = widgets.sideslip_slider.value()
                side_step = (side_values[1] - side_values[0]) / steps
                side_range = np.arange(side_values[0], side_values[1], side_step)
                side_range = side_range * np.pi / 180

                results = np.zeros((len(methods), len(aoa_range), len(side_range), 9))

                total_steps = (len(methods))*(len(aoa_range))*(len(side_range))

                for i in range(len(methods)):
                    for j in range(len(aoa_range)):
                        for k in range(len(side_range)):
                            step = i * len(aoa_range)*len(side_range) + j*len(side_range) + k
                            val  = round(100*step/total_steps)
                            widgets.exportcompare_progress.setValue(val)
                            QtGui.QGuiApplication.processEvents()
                            [cp, results[i, j, k, 0], results[i, j, k, 1], results[i, j, k, 2], results[i, j, k, 3], results[i, j, k, 4], results[i, j, k, 5], results[i, j, k, 6], results[i, j, k, 7], results[i, j, k, 8]] = SHABPy.RunSHABPy(aoa_range[j], side_range[k], widgets.Vehicle)

                with open('comparison_data.pkl', 'wb') as f:
                    pickle.dump(results, f)

                widgets.compare_vehiclestatus.setText('comparison_data.pkl Created')
                widgets.vehicle_status.setStyleSheet('color: rgb(50,205,50)')
                widgets.exportcompare_progress.setValue(0)

    def getExpComp(self):
        compression = []
        expansion = []
        if widgets.lookup_newtonian_check.isChecked():
            compression.append(1)
        if widgets.lookup_npm_check.isChecked():
            compression.append(2)
        if widgets.lookup_mn_check.isChecked():
            compression.append(3)
        if widgets.lookup_hankey_check.isChecked():
            compression.append(4)
        if widgets.lookup_vandyke_check.isChecked():
            compression.append(5)
        if widgets.lookup_busemann_check.isChecked():
            compression.append(6)
        if widgets.lookup_exp_newtonian_check.isChecked():
            expansion.append(1)
        if widgets.lookup_exp_npm_check.isChecked():
            expansion.append(2)
        if widgets.lookup_exp_mn_check.isChecked():
            expansion.append(3)
        if widgets.lookup_exp_hankey_check.isChecked():
            expansion.append(4)
        if widgets.lookup_exp_vandyke_check.isChecked():
            expansion.append(5)
        if widgets.lookup_exp_busemann_check.isChecked():
            expansion.append(6)
        return [compression, expansion]

    def ExportLookupTable(self):
        if widgets.Vehicle:
            if widgets.lookup_newtonian_check.isChecked() or widgets.lookup_npm_check.isChecked() or widgets.lookup_mn_check.isChecked() or widgets.lookup_hankey_check.isChecked() or widgets.lookup_vandyke_check.isChecked() or widgets.lookup_busemann_check.isChecked():
                if widgets.lookup_exp_newtonian_check.isChecked() or widgets.lookup_exp_npm_check.isChecked() or widgets.lookup_exp_mn_check.isChecked() or widgets.lookup_exp_hankey_check.isChecked() or widgets.lookup_exp_vandyke_check.isChecked() or widgets.lookup_exp_busemann_check.isChecked():
                    fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Mesh As", "",
                                                                        "All Files (*);;pkl Files (*.pkl)")
                    if fileName:
                        if len(fileName) > 4:
                            extension = fileName[-4:].lower()
                            if extension != '.pkl':
                                fileName += '.pkl'
                        else:
                            fileName += '.pkl'
                        [compression, expansion] = self.getExpComp()
                        M_range = widgets.mach_slider_lookup.value()
                        gamma_range = widgets.gamma_slider_lookup.value()
                        aoa_range = widgets.aoa_slider_lookup.value()
                        beta_range = widgets.beta_slider_lookup.value()

                        M = np.arange(M_range[0], M_range[1], 0.01)
                        gamma = np.arange(gamma_range[0], gamma_range[1], 0.01)
                        aoa = np.arange(aoa_range[0], aoa_range[1], 0.5)*math.pi/180
                        beta = np.arange(beta_range[0], beta_range[1], 0.5)*math.pi/180

                        table = np.zeros((len(compression), len(expansion), len(M), len(gamma), len(aoa), len(beta), 9))
                        total_steps = len(compression) * len(expansion) * len(M) * len(gamma) * len(aoa) * len(beta)

                        for i in range(len(compression)):
                            widgets.Vehicle.UpdateCompression(compression[i])
                            for j in range(len(expansion)):
                                widgets.Vehicle.UpdateExpansion(expansion[i])
                                for k in range(len(M)):
                                    widgets.Vehicle.M = M[k]
                                    for ii in range(len(gamma)):
                                        widgets.Vehicle.gamma = gamma[ii]
                                        for jj in range(len(aoa)):
                                            for kk in range(len(beta_range)):
                                                step = i  * len(expansion) * len(M) * len(gamma) * len(aoa) * len(beta) \
                                                       + j * len(M) * len(gamma) * len(aoa) * len(beta) \
                                                       + k * len(gamma) * len(aoa) * len(beta) \
                                                       + ii * len(aoa) * len(beta) \
                                                       + jj * len(beta) \
                                                       + kk
                                                val = round(100 * step / total_steps)
                                                widgets.lookup_table_progress.setValue(val)
                                                QtGui.QGuiApplication.processEvents()
                                                [cp, table[i, j, k, ii, jj, kk, 0], table[i, j, k, ii, jj, kk, 1], table[i, j, k, ii, jj, kk, 2],
                                                 table[i, j, k, ii, jj, kk, 3], table[i, j, k, ii, jj, kk, 4], table[i, j, k, ii, jj, kk, 5],
                                                 table[i, j, k, ii, jj, kk, 6], table[i, j, k, ii, jj, kk, 7],
                                                 table[i, j, k, ii, jj, kk, 8]] = SHABPy.RunSHABPy(aoa[jj], beta[kk], widgets.Vehicle)

                        with open(fileName, 'wb') as f:
                            pickle.dump(table, f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
