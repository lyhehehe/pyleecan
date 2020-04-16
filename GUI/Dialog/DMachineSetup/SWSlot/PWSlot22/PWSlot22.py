# -*- coding: utf-8 -*-

import PyQt5.QtCore
from numpy import pi
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from ......Classes.SlotW22 import SlotW22
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot22.Gen_PWSlot22 import Gen_PWSlot22
from ......Methods.Slot.Slot.check import SlotCheckError

translate = PyQt5.QtCore.QCoreApplication.translate


class PWSlot22(Gen_PWSlot22, QWidget):
    """Page to set the Slot Type 22
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for Slot combobox
    slot_name = "Slot Type 22"
    slot_type = SlotW22

    def __init__(self, lamination=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        # Set FloatEdit unit
        self.lf_H0.unit = "m"
        self.lf_H2.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [self.unit_H0, self.unit_H2]
        for wid in wid_list:
            wid.setText(gui_option.unit.get_m_name())

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_W2.setValue(self.slot.W2)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H2.setValue(self.slot.H2)

        self.c_W0_unit.setCurrentIndex(0)  # rad
        self.c_W2_unit.setCurrentIndex(0)  # rad

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal/slot
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.c_W0_unit.currentIndexChanged.connect(self.set_W0_unit)
        self.c_W2_unit.currentIndexChanged.connect(self.set_W2_unit)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        if self.c_W0_unit.currentIndex() == 0:  # Rad
            self.slot.W0 = self.lf_W0.value()
        else:
            self.slot.W0 = self.lf_W0.value() / 180 * pi
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        if self.c_W2_unit.currentIndex() == 0:  # Rad
            self.slot.W2 = self.lf_W2.value()
        else:
            self.slot.W2 = self.lf_W2.value() / 180 * pi
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W0_unit(self, value):
        """Signal to convert the value of W0 according to the combobox unit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        value : int
            Current index of combobox
        """
        if self.lf_W0.text() != "":
            self.set_W0()  # Update for deg if needed and call comp_output
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2_unit(self, value):
        """Signal to convert the value of W2 according to the combobox unit

        Parameters
        ----------
        self : PWSlot22
            A PWSlot22 object
        value : int
            Current index of combobox
        """
        if self.lf_W2.text() != "":
            self.set_W2()  # Update for deg if needed and call comp_output
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.Zs is None:
            return translate("You must set Zs !", "PWSlot22 check")
        elif lam.slot.W0 is None:
            return translate("You must set W0 !", "PWSlot22 check")
        elif lam.slot.W2 is None:
            return translate("You must set W2 !", "PWSlot22 check")
        elif lam.slot.H0 is None:
            return translate("You must set H0 !", "PWSlot22 check")
        elif lam.slot.H2 is None:
            return translate("You must set H2 !", "PWSlot22 check")

        # Check that everything is set right
        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PWSlot22 check") + str(
                error
            )
        if yoke_height <= 0:
            return translate(
                "The slot height is greater than the lamination !", "PWSlot22 check"
            )
