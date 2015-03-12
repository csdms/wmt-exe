#
# File:          Heat_Impl.py
# Symbol:        csdms.examples.py.Heat-v0.0
# Symbol Type:   class
# Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
# Description:   Implementation of sidl class csdms.examples.py.Heat in Python.
# 
# WARNING: Automatically generated; changes will be lost
# 
#


# DO-NOT-DELETE splicer.begin(_initial)
# Insert-Code-Here {_initial} ()
# DO-NOT-DELETE splicer.end(_initial)

import csdms.core.Bmi
import csdms.examples.py.Heat
import sidl.BaseClass
import sidl.BaseInterface
import sidl.ClassInfo
import sidl.RuntimeException
import sidl.NotImplementedException

# DO-NOT-DELETE splicer.begin(_before_type)
import sys
from ${bmi_package} import ${bmi_class} as Model

# DO-NOT-DELETE splicer.end(_before_type)

class Heat:

# All calls to sidl methods should use __IORself

# Normal Babel creation pases in an IORself. If IORself == None
# that means this Impl class is being constructed for native delegation
  def __init__(self, IORself = None):
    if (IORself == None):
      self.__IORself = csdms.examples.py.Heat.Heat(impl = self)
    else:
      self.__IORself = IORself
# DO-NOT-DELETE splicer.begin(__init__)

    # Put your code here...
    self._model = Model()

    # Bocca generated code. bocca.protected.begin(csdms.examples.py.Heat._init) 
    self.bocca_print_errs = True
    # Bocca generated code. bocca.protected.end(csdms.examples.py.Heat._init) 

# DO-NOT-DELETE splicer.end(__init__)

# Returns the IORself (client stub) of the Impl, mainly for use
# with native delegation
  def _getStub(self):
    return self.__IORself

  def boccaForceUsePortInclude(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # None
    #

    """\
 This function should never be called, but helps babel generate better code. 
"""
    # DO-NOT-DELETE splicer.begin(boccaForceUsePortInclude)
    # DO-NOT-EDIT-BOCCA
    # Bocca generated code. bocca.protected.begin(boccaForceUsePortInclude)
    return
    # Bocca generated code. bocca.protected.end(boccaForceUsePortInclude)
    # DO-NOT-DELETE splicer.end(boccaForceUsePortInclude)

  def initialize(self, config_file):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string config_file
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # bool _return
    #

# DO-NOT-DELETE splicer.begin(initialize)
    return self._model.initialize(config_file)
# DO-NOT-DELETE splicer.end(initialize)

  def update(self, time_interval):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # double time_interval
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # bool _return
    #

# DO-NOT-DELETE splicer.begin(update)
    return self._model.update(time_interval)
# DO-NOT-DELETE splicer.end(update)

  def finalize(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # bool _return
    #

# DO-NOT-DELETE splicer.begin(finalize)
    return self._model.finalize()
# DO-NOT-DELETE splicer.end(finalize)

  def get_start_time(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # double _return
    #

# DO-NOT-DELETE splicer.begin(get_start_time)
    return self._model.get_start_time()
# DO-NOT-DELETE splicer.end(get_start_time)

  def get_current_time(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # double _return
    #

# DO-NOT-DELETE splicer.begin(get_current_time)
    return self._model.get_current_time()
# DO-NOT-DELETE splicer.end(get_current_time)

  def get_end_time(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # double _return
    #

# DO-NOT-DELETE splicer.begin(get_end_time)
    return self._model.get_end_time()
# DO-NOT-DELETE splicer.end(get_end_time)

  def get_component_name(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # string _return
    #

# DO-NOT-DELETE splicer.begin(get_component_name)
    return self._model.get_component_name()
# DO-NOT-DELETE splicer.end(get_component_name)

  def get_input_item_count(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # int _return
    #

# DO-NOT-DELETE splicer.begin(get_input_item_count)
    return self._model.get_input_item_count()
# DO-NOT-DELETE splicer.end(get_input_item_count)

  def get_input_item_list(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<string> _return
    #

# DO-NOT-DELETE splicer.begin(get_input_item_list)
    return self._model.get_input_item_list()
# DO-NOT-DELETE splicer.end(get_input_item_list)

  def get_output_item_count(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # int _return
    #

# DO-NOT-DELETE splicer.begin(get_output_item_count)
    return self._model.get_output_item_count()
# DO-NOT-DELETE splicer.end(get_output_item_count)

  def get_output_item_list(self):
    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<string> _return
    #

# DO-NOT-DELETE splicer.begin(get_output_item_list)
    return self._model.get_output_item_list()
# DO-NOT-DELETE splicer.end(get_output_item_list)

  def get_grid_rank(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # int _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_rank)
    return self._model.get_grid_rank(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_rank)

  def get_grid_spacing(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<double> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_spacing)
    return self._model.get_grid_spacing(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_spacing)

  def get_grid_origin(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<double> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_origin)
    return self._model.get_grid_origin(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_origin)

  def get_grid_shape(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<int> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_shape)
    return self._model.get_grid_shape(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_shape)

  def get_grid_x(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<double> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_x)
    return self._model.get_grid_x(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_x)

  def get_grid_y(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<double> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_y)
    return self._model.get_grid_y(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_y)

  def get_grid_z(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<double> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_z)
    return self._model.get_grid_z(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_z)

  def get_grid_connectivity(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<int> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_connectivity)
    return self._model.get_grid_connectivity(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_connectivity)

  def get_grid_offset(self, long_var_name):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<int> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_offset)
    return self._model.get_grid_offset(long_var_name)
# DO-NOT-DELETE splicer.end(get_grid_offset)

  def get_grid_values(self, long_var_name, values):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    # array<> values
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # array<> _return
    #

# DO-NOT-DELETE splicer.begin(get_grid_values)
    return self._model.get_grid_values(long_var_name, values)
# DO-NOT-DELETE splicer.end(get_grid_values)

  def set_grid_values(self, long_var_name, vals):
    #
    # sidl EXPECTED INCOMING TYPES
    # ============================
    # string long_var_name
    # array<double> vals
    #

    #
    # sidl EXPECTED RETURN VALUE(s)
    # =============================
    # None
    #

# DO-NOT-DELETE splicer.begin(set_grid_values)
    return self._model.set_grid_values(long_var_name, values)
# DO-NOT-DELETE splicer.end(set_grid_values)

# DO-NOT-DELETE splicer.begin(_final)
# Insert-Code-Here {_final} ()
# DO-NOT-DELETE splicer.end(_final)
