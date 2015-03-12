/*
 * File:          csdms_examples_c_Heat_Impl.h
 * Symbol:        csdms.examples.c.Heat-v0.0
 * Symbol Type:   class
 * Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
 * Description:   Server-side implementation for csdms.examples.c.Heat
 * 
 * WARNING: Automatically generated; only changes within splicers preserved
 * 
 */

#ifndef included_csdms_examples_c_Heat_Impl_h
#define included_csdms_examples_c_Heat_Impl_h

#ifndef included_sidl_header_h
#include "sidl_header.h"
#endif
#ifndef included_csdms_core_Bmi_h
#include "csdms_core_Bmi.h"
#endif
#ifndef included_csdms_examples_c_Heat_h
#include "csdms_examples_c_Heat.h"
#endif
#ifndef included_sidl_BaseClass_h
#include "sidl_BaseClass.h"
#endif
#ifndef included_sidl_BaseInterface_h
#include "sidl_BaseInterface.h"
#endif
#ifndef included_sidl_ClassInfo_h
#include "sidl_ClassInfo.h"
#endif
#ifndef included_sidl_RuntimeException_h
#include "sidl_RuntimeException.h"
#endif
/* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._hincludes) */
/* Insert-Code-Here {csdms.examples.c.Heat._hincludes} (include files) */
${bmi_includes}
${bmi_defines}

#define _CALL_BMI(prefix, func, ...) { \
  int status = prefix##_##func(__VA_ARGS__); \
  if (status != 0) { \
    fprintf(stderr, "Error running " #func "\n"); \
    SIDL_THROW(*_ex, sidl_NotImplementedException, "Error running " #func " "); \
  } \
}

#define _GET_PRIVATE_DATA(clazz, var) \
  struct clazz##__data *var = clazz##__get_data(self);

#define CALL_BMI(func, ...) _CALL_BMI(${bmi_prefix}, func, __VA_ARGS__)
#define GET_PRIVATE_DATA(var) _GET_PRIVATE_DATA(csdms_examples_c_Heat, var)

/* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._hincludes) */

/*
 * Private data for class csdms.examples.c.Heat
 */

struct csdms_examples_c_Heat__data {
  /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._data) */
  /* Insert-Code-Here {csdms.examples.c.Heat._data} (private data members) */
  void *state;
  int ignore; /* dummy to force non-empty struct; remove if you add data */
  /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._data) */
};

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Access functions for class private data and built-in methods
 */

extern struct csdms_examples_c_Heat__data*
csdms_examples_c_Heat__get_data(
  csdms_examples_c_Heat);

extern void
csdms_examples_c_Heat__set_data(
  csdms_examples_c_Heat,
  struct csdms_examples_c_Heat__data*);

extern
void
impl_csdms_examples_c_Heat__load(
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_csdms_examples_c_Heat__ctor(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_csdms_examples_c_Heat__ctor2(
  /* in */ csdms_examples_c_Heat self,
  /* in */ void* private_data,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_csdms_examples_c_Heat__dtor(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

/*
 * User-defined object methods
 */

#ifdef WITH_RMI
extern struct sidl_BaseInterface__object* 
  impl_csdms_examples_c_Heat_fconnect_sidl_BaseInterface(const char* url, 
  sidl_bool ar, sidl_BaseInterface *_ex);
#endif /*WITH_RMI*/
extern
void
impl_csdms_examples_c_Heat_boccaForceUsePortInclude(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
sidl_bool
impl_csdms_examples_c_Heat_initialize(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* config_file,
  /* out */ sidl_BaseInterface *_ex);

extern
sidl_bool
impl_csdms_examples_c_Heat_update(
  /* in */ csdms_examples_c_Heat self,
  /* in */ double time_interval,
  /* out */ sidl_BaseInterface *_ex);

extern
sidl_bool
impl_csdms_examples_c_Heat_finalize(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
double
impl_csdms_examples_c_Heat_get_start_time(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
double
impl_csdms_examples_c_Heat_get_current_time(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
double
impl_csdms_examples_c_Heat_get_end_time(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl__array*
impl_csdms_examples_c_Heat_get_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_csdms_examples_c_Heat_set_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<> */ struct sidl__array* in_values,
  /* out */ sidl_BaseInterface *_ex);

extern
char*
impl_csdms_examples_c_Heat_get_component_name(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_csdms_examples_c_Heat_get_input_item_count(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_string__array*
impl_csdms_examples_c_Heat_get_input_item_list(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_csdms_examples_c_Heat_get_output_item_count(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_string__array*
impl_csdms_examples_c_Heat_get_output_item_list(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl__array*
impl_csdms_examples_c_Heat_get_values_at_indices(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<int> */ struct sidl_int__array* indices,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_csdms_examples_c_Heat_set_values_at_indices(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<int> */ struct sidl_int__array* indices,
  /* in array<> */ struct sidl__array* in_values,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_csdms_examples_c_Heat_get_grid_rank(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_spacing(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_origin(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_int__array*
impl_csdms_examples_c_Heat_get_grid_shape(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_x(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_y(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_z(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_int__array*
impl_csdms_examples_c_Heat_get_grid_connectivity(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_int__array*
impl_csdms_examples_c_Heat_get_grid_offset(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_csdms_examples_c_Heat_set_grid_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<double> */ struct sidl_double__array* vals,
  /* out */ sidl_BaseInterface *_ex);

#ifdef WITH_RMI
extern struct sidl_BaseInterface__object* 
  impl_csdms_examples_c_Heat_fconnect_sidl_BaseInterface(const char* url, 
  sidl_bool ar, sidl_BaseInterface *_ex);
#endif /*WITH_RMI*/

/* DO-NOT-DELETE splicer.begin(_hmisc) */
/* Insert-Code-Here {_hmisc} (miscellaneous things) */
/* DO-NOT-DELETE splicer.end(_hmisc) */

#ifdef __cplusplus
}
#endif
#endif
