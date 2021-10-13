# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutElec.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutElec
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutElec.get_I_fund import get_I_fund
except ImportError as error:
    get_I_fund = error

try:
    from ..Methods.Output.OutElec.get_I_harm import get_I_harm
except ImportError as error:
    get_I_harm = error

try:
    from ..Methods.Output.OutElec.get_Is import get_Is
except ImportError as error:
    get_Is = error

try:
    from ..Methods.Output.OutElec.get_Nr import get_Nr
except ImportError as error:
    get_Nr = error

try:
    from ..Methods.Output.OutElec.get_Us import get_Us
except ImportError as error:
    get_Us = error

try:
    from ..Methods.Output.OutElec.store import store
except ImportError as error:
    store = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .OutInternal import OutInternal


class OutElec(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutElec.get_I_fund
    if isinstance(get_I_fund, ImportError):
        get_I_fund = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_I_fund: " + str(get_I_fund))
            )
        )
    else:
        get_I_fund = get_I_fund
    # cf Methods.Output.OutElec.get_I_harm
    if isinstance(get_I_harm, ImportError):
        get_I_harm = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_I_harm: " + str(get_I_harm))
            )
        )
    else:
        get_I_harm = get_I_harm
    # cf Methods.Output.OutElec.get_Is
    if isinstance(get_Is, ImportError):
        get_Is = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Is: " + str(get_Is))
            )
        )
    else:
        get_Is = get_Is
    # cf Methods.Output.OutElec.get_Nr
    if isinstance(get_Nr, ImportError):
        get_Nr = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Nr: " + str(get_Nr))
            )
        )
    else:
        get_Nr = get_Nr
    # cf Methods.Output.OutElec.get_Us
    if isinstance(get_Us, ImportError):
        get_Us = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Us: " + str(get_Us))
            )
        )
    else:
        get_Us = get_Us
    # cf Methods.Output.OutElec.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method store: " + str(store))
            )
        )
    else:
        store = store
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        axes_dict=None,
        Is=None,
        Ir=None,
        angle_rotor=None,
        N0=None,
        angle_rotor_initial=0,
        logger_name="Pyleecan.Electrical",
        Tem_av_ref=None,
        Id_ref=None,
        Iq_ref=None,
        felec=None,
        Ud_ref=None,
        Uq_ref=None,
        Pj_losses=None,
        Pem_av_ref=None,
        Us=None,
        internal=None,
        slip_ref=0,
        U0_ref=None,
        Us_harm=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "Pj_losses" in list(init_dict.keys()):
                Pj_losses = init_dict["Pj_losses"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
            if "Us" in list(init_dict.keys()):
                Us = init_dict["Us"]
            if "internal" in list(init_dict.keys()):
                internal = init_dict["internal"]
            if "slip_ref" in list(init_dict.keys()):
                slip_ref = init_dict["slip_ref"]
            if "U0_ref" in list(init_dict.keys()):
                U0_ref = init_dict["U0_ref"]
            if "Us_harm" in list(init_dict.keys()):
                Us_harm = init_dict["Us_harm"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.axes_dict = axes_dict
        self.Is = Is
        self.Ir = Ir
        self.angle_rotor = angle_rotor
        self.N0 = N0
        self.angle_rotor_initial = angle_rotor_initial
        self.logger_name = logger_name
        self.Tem_av_ref = Tem_av_ref
        self.Id_ref = Id_ref
        self.Iq_ref = Iq_ref
        self.felec = felec
        self.Ud_ref = Ud_ref
        self.Uq_ref = Uq_ref
        self.Pj_losses = Pj_losses
        self.Pem_av_ref = Pem_av_ref
        self.Us = Us
        self.internal = internal
        self.slip_ref = slip_ref
        self.U0_ref = U0_ref
        self.Us_harm = Us_harm

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutElec_str = ""
        if self.parent is None:
            OutElec_str += "parent = None " + linesep
        else:
            OutElec_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutElec_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        OutElec_str += "Is = " + str(self.Is) + linesep + linesep
        OutElec_str += "Ir = " + str(self.Ir) + linesep + linesep
        OutElec_str += (
            "angle_rotor = "
            + linesep
            + str(self.angle_rotor).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutElec_str += "N0 = " + str(self.N0) + linesep
        OutElec_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        OutElec_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutElec_str += "Tem_av_ref = " + str(self.Tem_av_ref) + linesep
        OutElec_str += "Id_ref = " + str(self.Id_ref) + linesep
        OutElec_str += "Iq_ref = " + str(self.Iq_ref) + linesep
        OutElec_str += "felec = " + str(self.felec) + linesep
        OutElec_str += "Ud_ref = " + str(self.Ud_ref) + linesep
        OutElec_str += "Uq_ref = " + str(self.Uq_ref) + linesep
        OutElec_str += "Pj_losses = " + str(self.Pj_losses) + linesep
        OutElec_str += "Pem_av_ref = " + str(self.Pem_av_ref) + linesep
        OutElec_str += "Us = " + str(self.Us) + linesep + linesep
        if self.internal is not None:
            tmp = self.internal.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutElec_str += "internal = " + tmp
        else:
            OutElec_str += "internal = None" + linesep + linesep
        OutElec_str += "slip_ref = " + str(self.slip_ref) + linesep
        OutElec_str += "U0_ref = " + str(self.U0_ref) + linesep
        OutElec_str += "Us_harm = " + str(self.Us_harm) + linesep + linesep
        return OutElec_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.axes_dict != self.axes_dict:
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if not array_equal(other.angle_rotor, self.angle_rotor):
            return False
        if other.N0 != self.N0:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.Tem_av_ref != self.Tem_av_ref:
            return False
        if other.Id_ref != self.Id_ref:
            return False
        if other.Iq_ref != self.Iq_ref:
            return False
        if other.felec != self.felec:
            return False
        if other.Ud_ref != self.Ud_ref:
            return False
        if other.Uq_ref != self.Uq_ref:
            return False
        if other.Pj_losses != self.Pj_losses:
            return False
        if other.Pem_av_ref != self.Pem_av_ref:
            return False
        if other.Us != self.Us:
            return False
        if other.internal != self.internal:
            return False
        if other.slip_ref != self.slip_ref:
            return False
        if other.U0_ref != self.U0_ref:
            return False
        if other.Us_harm != self.Us_harm:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.axes_dict is None and self.axes_dict is not None) or (
            other.axes_dict is not None and self.axes_dict is None
        ):
            diff_list.append(name + ".axes_dict None mismatch")
        elif self.axes_dict is None:
            pass
        elif len(other.axes_dict) != len(self.axes_dict):
            diff_list.append("len(" + name + "axes_dict)")
        else:
            for key in self.axes_dict:
                diff_list.extend(
                    self.axes_dict[key].compare(
                        other.axes_dict[key], name=name + ".axes_dict"
                    )
                )
        if (other.Is is None and self.Is is not None) or (
            other.Is is not None and self.Is is None
        ):
            diff_list.append(name + ".Is None mismatch")
        elif self.Is is not None:
            diff_list.extend(self.Is.compare(other.Is, name=name + ".Is"))
        if (other.Ir is None and self.Ir is not None) or (
            other.Ir is not None and self.Ir is None
        ):
            diff_list.append(name + ".Ir None mismatch")
        elif self.Ir is not None:
            diff_list.extend(self.Ir.compare(other.Ir, name=name + ".Ir"))
        if not array_equal(other.angle_rotor, self.angle_rotor):
            diff_list.append(name + ".angle_rotor")
        if other._N0 != self._N0:
            diff_list.append(name + ".N0")
        if other._angle_rotor_initial != self._angle_rotor_initial:
            diff_list.append(name + ".angle_rotor_initial")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if other._Tem_av_ref != self._Tem_av_ref:
            diff_list.append(name + ".Tem_av_ref")
        if other._Id_ref != self._Id_ref:
            diff_list.append(name + ".Id_ref")
        if other._Iq_ref != self._Iq_ref:
            diff_list.append(name + ".Iq_ref")
        if other._felec != self._felec:
            diff_list.append(name + ".felec")
        if other._Ud_ref != self._Ud_ref:
            diff_list.append(name + ".Ud_ref")
        if other._Uq_ref != self._Uq_ref:
            diff_list.append(name + ".Uq_ref")
        if other._Pj_losses != self._Pj_losses:
            diff_list.append(name + ".Pj_losses")
        if other._Pem_av_ref != self._Pem_av_ref:
            diff_list.append(name + ".Pem_av_ref")
        if (other.Us is None and self.Us is not None) or (
            other.Us is not None and self.Us is None
        ):
            diff_list.append(name + ".Us None mismatch")
        elif self.Us is not None:
            diff_list.extend(self.Us.compare(other.Us, name=name + ".Us"))
        if (other.internal is None and self.internal is not None) or (
            other.internal is not None and self.internal is None
        ):
            diff_list.append(name + ".internal None mismatch")
        elif self.internal is not None:
            diff_list.extend(
                self.internal.compare(other.internal, name=name + ".internal")
            )
        if other._slip_ref != self._slip_ref:
            diff_list.append(name + ".slip_ref")
        if other._U0_ref != self._U0_ref:
            diff_list.append(name + ".U0_ref")
        if (other.Us_harm is None and self.Us_harm is not None) or (
            other.Us_harm is not None and self.Us_harm is None
        ):
            diff_list.append(name + ".Us_harm None mismatch")
        elif self.Us_harm is not None:
            diff_list.extend(
                self.Us_harm.compare(other.Us_harm, name=name + ".Us_harm")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Is)
        S += getsizeof(self.Ir)
        S += getsizeof(self.angle_rotor)
        S += getsizeof(self.N0)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.Tem_av_ref)
        S += getsizeof(self.Id_ref)
        S += getsizeof(self.Iq_ref)
        S += getsizeof(self.felec)
        S += getsizeof(self.Ud_ref)
        S += getsizeof(self.Uq_ref)
        S += getsizeof(self.Pj_losses)
        S += getsizeof(self.Pem_av_ref)
        S += getsizeof(self.Us)
        S += getsizeof(self.internal)
        S += getsizeof(self.slip_ref)
        S += getsizeof(self.U0_ref)
        S += getsizeof(self.Us_harm)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        OutElec_dict = dict()
        if self.axes_dict is None:
            OutElec_dict["axes_dict"] = None
        else:
            OutElec_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    OutElec_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutElec_dict["axes_dict"][key] = None
        if self.Is is None:
            OutElec_dict["Is"] = None
        else:
            OutElec_dict["Is"] = self.Is.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Ir is None:
            OutElec_dict["Ir"] = None
        else:
            OutElec_dict["Ir"] = self.Ir.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.angle_rotor is None:
            OutElec_dict["angle_rotor"] = None
        else:
            if type_handle_ndarray == 0:
                OutElec_dict["angle_rotor"] = self.angle_rotor.tolist()
            elif type_handle_ndarray == 1:
                OutElec_dict["angle_rotor"] = self.angle_rotor.copy()
            elif type_handle_ndarray == 2:
                OutElec_dict["angle_rotor"] = self.angle_rotor
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OutElec_dict["N0"] = self.N0
        OutElec_dict["angle_rotor_initial"] = self.angle_rotor_initial
        OutElec_dict["logger_name"] = self.logger_name
        OutElec_dict["Tem_av_ref"] = self.Tem_av_ref
        OutElec_dict["Id_ref"] = self.Id_ref
        OutElec_dict["Iq_ref"] = self.Iq_ref
        OutElec_dict["felec"] = self.felec
        OutElec_dict["Ud_ref"] = self.Ud_ref
        OutElec_dict["Uq_ref"] = self.Uq_ref
        OutElec_dict["Pj_losses"] = self.Pj_losses
        OutElec_dict["Pem_av_ref"] = self.Pem_av_ref
        if self.Us is None:
            OutElec_dict["Us"] = None
        else:
            OutElec_dict["Us"] = self.Us.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.internal is None:
            OutElec_dict["internal"] = None
        else:
            OutElec_dict["internal"] = self.internal.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutElec_dict["slip_ref"] = self.slip_ref
        OutElec_dict["U0_ref"] = self.U0_ref
        if self.Us_harm is None:
            OutElec_dict["Us_harm"] = None
        else:
            OutElec_dict["Us_harm"] = self.Us_harm.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        OutElec_dict["__class__"] = "OutElec"
        return OutElec_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.axes_dict = None
        self.Is = None
        self.Ir = None
        self.angle_rotor = None
        self.N0 = None
        self.angle_rotor_initial = None
        self.logger_name = None
        self.Tem_av_ref = None
        self.Id_ref = None
        self.Iq_ref = None
        self.felec = None
        self.Ud_ref = None
        self.Uq_ref = None
        self.Pj_losses = None
        self.Pem_av_ref = None
        self.Us = None
        if self.internal is not None:
            self.internal._set_None()
        self.slip_ref = None
        self.U0_ref = None
        self.Us_harm = None

    def _get_axes_dict(self):
        """getter of axes_dict"""
        if self._axes_dict is not None:
            for key, obj in self._axes_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._axes_dict

    def _set_axes_dict(self, value):
        """setter of axes_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "axes_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_dict", value, "{Data}")
        self._axes_dict = value

    axes_dict = property(
        fget=_get_axes_dict,
        fset=_set_axes_dict,
        doc=u"""Dict containing axes data used for Electrical

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Is"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Is", value, "DataND")
        self._Is = value

    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents DataTime object

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Ir"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Ir", value, "DataND")
        self._Ir = value

    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle_rotor", value, "ndarray")
        self._angle_rotor = value

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr)

        :Type: ndarray
        """,
    )

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        check_var("N0", value, "float")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotor speed

        :Type: float
        """,
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0

        :Type: float
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_Tem_av_ref(self):
        """getter of Tem_av_ref"""
        return self._Tem_av_ref

    def _set_Tem_av_ref(self, value):
        """setter of Tem_av_ref"""
        check_var("Tem_av_ref", value, "float")
        self._Tem_av_ref = value

    Tem_av_ref = property(
        fget=_get_Tem_av_ref,
        fset=_set_Tem_av_ref,
        doc=u"""Theorical Average Electromagnetic torque

        :Type: float
        """,
    )

    def _get_Id_ref(self):
        """getter of Id_ref"""
        return self._Id_ref

    def _set_Id_ref(self, value):
        """setter of Id_ref"""
        check_var("Id_ref", value, "float")
        self._Id_ref = value

    Id_ref = property(
        fget=_get_Id_ref,
        fset=_set_Id_ref,
        doc=u"""d-axis current rms value

        :Type: float
        """,
    )

    def _get_Iq_ref(self):
        """getter of Iq_ref"""
        return self._Iq_ref

    def _set_Iq_ref(self, value):
        """setter of Iq_ref"""
        check_var("Iq_ref", value, "float")
        self._Iq_ref = value

    Iq_ref = property(
        fget=_get_Iq_ref,
        fset=_set_Iq_ref,
        doc=u"""q-axis current rms value

        :Type: float
        """,
    )

    def _get_felec(self):
        """getter of felec"""
        return self._felec

    def _set_felec(self, value):
        """setter of felec"""
        check_var("felec", value, "float")
        self._felec = value

    felec = property(
        fget=_get_felec,
        fset=_set_felec,
        doc=u"""Electrical Frequency

        :Type: float
        """,
    )

    def _get_Ud_ref(self):
        """getter of Ud_ref"""
        return self._Ud_ref

    def _set_Ud_ref(self, value):
        """setter of Ud_ref"""
        check_var("Ud_ref", value, "float")
        self._Ud_ref = value

    Ud_ref = property(
        fget=_get_Ud_ref,
        fset=_set_Ud_ref,
        doc=u"""d-axis voltage rms value

        :Type: float
        """,
    )

    def _get_Uq_ref(self):
        """getter of Uq_ref"""
        return self._Uq_ref

    def _set_Uq_ref(self, value):
        """setter of Uq_ref"""
        check_var("Uq_ref", value, "float")
        self._Uq_ref = value

    Uq_ref = property(
        fget=_get_Uq_ref,
        fset=_set_Uq_ref,
        doc=u"""q-axis voltage rms value

        :Type: float
        """,
    )

    def _get_Pj_losses(self):
        """getter of Pj_losses"""
        return self._Pj_losses

    def _set_Pj_losses(self, value):
        """setter of Pj_losses"""
        check_var("Pj_losses", value, "float")
        self._Pj_losses = value

    Pj_losses = property(
        fget=_get_Pj_losses,
        fset=_set_Pj_losses,
        doc=u"""Electrical Joule losses

        :Type: float
        """,
    )

    def _get_Pem_av_ref(self):
        """getter of Pem_av_ref"""
        return self._Pem_av_ref

    def _set_Pem_av_ref(self, value):
        """setter of Pem_av_ref"""
        check_var("Pem_av_ref", value, "float")
        self._Pem_av_ref = value

    Pem_av_ref = property(
        fget=_get_Pem_av_ref,
        fset=_set_Pem_av_ref,
        doc=u"""Theorical Average Electromagnetic Power

        :Type: float
        """,
    )

    def _get_Us(self):
        """getter of Us"""
        return self._Us

    def _set_Us(self, value):
        """setter of Us"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Us"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Us", value, "DataND")
        self._Us = value

    Us = property(
        fget=_get_Us,
        fset=_set_Us,
        doc=u"""Stator voltage as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_internal(self):
        """getter of internal"""
        return self._internal

    def _set_internal(self, value):
        """setter of internal"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "internal"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = OutInternal()
        check_var("internal", value, "OutInternal")
        self._internal = value

        if self._internal is not None:
            self._internal.parent = self

    internal = property(
        fget=_get_internal,
        fset=_set_internal,
        doc=u"""OutInternal object containg outputs related to a specific model

        :Type: OutInternal
        """,
    )

    def _get_slip_ref(self):
        """getter of slip_ref"""
        return self._slip_ref

    def _set_slip_ref(self, value):
        """setter of slip_ref"""
        check_var("slip_ref", value, "float")
        self._slip_ref = value

    slip_ref = property(
        fget=_get_slip_ref,
        fset=_set_slip_ref,
        doc=u"""Rotor mechanical slip

        :Type: float
        """,
    )

    def _get_U0_ref(self):
        """getter of U0_ref"""
        return self._U0_ref

    def _set_U0_ref(self, value):
        """setter of U0_ref"""
        check_var("U0_ref", value, "float")
        self._U0_ref = value

    U0_ref = property(
        fget=_get_U0_ref,
        fset=_set_U0_ref,
        doc=u"""stator voltage (phase to neutral)

        :Type: float
        """,
    )

    def _get_Us_harm(self):
        """getter of Us_harm"""
        return self._Us_harm

    def _set_Us_harm(self, value):
        """setter of Us_harm"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "SciDataTool.Classes", value.get("__class__"), "Us_harm"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = DataND()
        check_var("Us_harm", value, "DataND")
        self._Us_harm = value

    Us_harm = property(
        fget=_get_Us_harm,
        fset=_set_Us_harm,
        doc=u"""Harmonic stator voltage as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )
