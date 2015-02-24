/*
 * File:          csdms_examples_c_Heat_Impl.c
 * Symbol:        csdms.examples.c.Heat-v0.0
 * Symbol Type:   class
 * Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
 * Description:   Server-side implementation for csdms.examples.c.Heat
 * 
 * WARNING: Automatically generated; only changes within splicers preserved
 * 
 */

/*
 * DEVELOPERS ARE EXPECTED TO PROVIDE IMPLEMENTATIONS
 * FOR THE FOLLOWING METHODS BETWEEN SPLICER PAIRS.
 */

/*
 * Symbol "csdms.examples.c.Heat" (version 0.0)
 */

#include "csdms_examples_c_Heat_Impl.h"
#include "sidl_NotImplementedException.h"
#include "sidl_Exception.h"
#ifndef included_sidl_MemAllocException_h
#include "sidl_MemAllocException.h"
#endif

/* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._includes) */

/* Insert-UserCode-Here {csdms.examples.c.Heat._includes} (includes and arbitrary code) */

/* Bocca generated code. bocca.protected.begin(csdms.examples.c.Heat._includes) */
#include <stdlib.h>
#include <string.h>
#include "sidl_SIDLException.h"

#define _BOCCA_CTOR_MESSAGES 0

#ifdef _BOCCA_STDERR

#define BOCCA_FPRINTF fprintf
#include <stdio.h>
#include "sidl_String.h"
#ifdef _BOCCA_CTOR_PRINT
#undef _BOCCA_CTOR_MESSAGES
#define _BOCCA_CTOR_MESSAGES 1
#endif /* _BOCCA_CTOR_PRINT */

#else /* _BOCCA_STDERR */
#define BOCCA_FPRINTF boccaPrintNothing
#endif /* _BOCCA_STDERR */

static int
boccaPrintNothing(void *v, const char * s, ...)
{
  (void)v; (void)s;
  return 0;
}
/* Bocca generated code. bocca.protected.end(csdms.examples.c.Heat._includes) */

/* Insert-UserCode-Here {csdms.examples.c.Heat._includes} (includes and arbitrary code) */

/* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._includes) */

#define SIDL_IOR_MAJOR_VERSION 2
#define SIDL_IOR_MINOR_VERSION 0
/*
 * Static class initializer called exactly once before any user-defined method is dispatched
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat__load"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat__load(
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._load) */
    /* Insert-Code-Here {csdms.examples.c.Heat._load} (static class
      initializer method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat._load) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat._load) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._load) */
  }
}
/*
 * Class constructor called when the class is created.
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat__ctor"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat__ctor(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._ctor) */

  /* Insert-UserDecl-Here {csdms.examples.c.Heat._ctor} (constructor method) */

  /* bocca-default-code. User may edit or delete.begin(csdms.examples.c.Heat._ctor) */
   struct csdms_examples_c_Heat__data *dptr =
       (struct csdms_examples_c_Heat__data*)malloc(sizeof(struct csdms_examples_c_Heat__data));
   if (dptr) {
      memset(dptr, 0, sizeof(struct csdms_examples_c_Heat__data));
   }
   csdms_examples_c_Heat__set_data(self, dptr);
   #if _BOCCA_CTOR_MESSAGES
     BOCCA_FPRINTF(stderr,
        "CTOR csdms.examples.c.Heat: %s constructed data %p in self %p\n",
        __FUNC__, dptr, self);
   #endif /* _BOCCA_CTOR_MESSAGES */
  /* bocca-default-code. User may edit or delete.end(csdms.examples.c.Heat._ctor) */

  /* initialize user elements of dptr here */
  /* Insert-UserCode-Here {csdms.examples.c.Heat._ctor} (constructor method) */

    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._ctor) */
  }
}

/*
 * Special Class constructor called when the user wants to wrap his own private data.
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat__ctor2"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat__ctor2(
  /* in */ csdms_examples_c_Heat self,
  /* in */ void* private_data,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._ctor2) */
    /* Insert-Code-Here {csdms.examples.c.Heat._ctor2} (special constructor
      method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat._ctor2) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat._ctor2) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._ctor2) */
  }
}
/*
 * Class destructor called when the class is deleted.
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat__dtor"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat__dtor(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat._dtor) */

  /* deinitialize user elements of dptr here */
  /* Insert-UserCode-Here {csdms.examples.c.Heat._dtor} (destructor method) */

  /* bocca-default-code. User may edit or delete.begin(csdms.examples.c.Heat._dtor) */
   struct csdms_examples_c_Heat__data *dptr =
                csdms_examples_c_Heat__get_data(self);
   if (dptr) {
      free(dptr);
      csdms_examples_c_Heat__set_data(self, NULL);
   }
   #if _BOCCA_CTOR_MESSAGES
     BOCCA_FPRINTF(stderr, "DTOR csdms.examples.c.Heat: %s freed data %p in self %p\n",
                   __FUNC__, dptr, self);
   #endif /* _BOCCA_CTOR_MESSAGES */
  /* bocca-default-code. User may edit or delete.end(csdms.examples.c.Heat._dtor) */

    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat._dtor) */
  }
}

/*
 *  This function should never be called, but helps babel generate better code. 
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_boccaForceUsePortInclude"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat_boccaForceUsePortInclude(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.boccaForceUsePortInclude) */
/* DO-NOT-EDIT-BOCCA */
  /* Bocca generated code. bocca.protected.begin(csdms.examples.c.Heat.boccaForceUsePortInclude) */
    (void)self;

  /* Bocca generated code. bocca.protected.end(csdms.examples.c.Heat.boccaForceUsePortInclude) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.boccaForceUsePortInclude) */
  }
}

/*
 * Method:  initialize[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_initialize"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_csdms_examples_c_Heat_initialize(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* config_file,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.initialize) */
    GET_PRIVATE_DATA(this);
    CALL_BMI(Initialize, config_file, &(this->state));

    return 0;

  EXIT:;
    return 1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.initialize) */
  }
}

/*
 * Method:  update[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_update"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_csdms_examples_c_Heat_update(
  /* in */ csdms_examples_c_Heat self,
  /* in */ double time_interval,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.update) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    CALL_BMI(Update_until, this->state, time_interval);
    return 0;

  EXIT:;

    return 1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.update) */
  }
}

/*
 * Method:  finalize[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_finalize"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_csdms_examples_c_Heat_finalize(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.finalize) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    CALL_BMI(Finalize, this->state);
    return 0;
  EXIT:;
    return 1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.finalize) */
  }
}

/*
 * Method:  get_start_time[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_start_time"

#ifdef __cplusplus
extern "C"
#endif
double
impl_csdms_examples_c_Heat_get_start_time(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_start_time) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    double time;

    CALL_BMI(Get_start_time, this->state, &time);
    return time;

  EXIT:;
    return -1.;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_start_time) */
  }
}

/*
 * Method:  get_current_time[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_current_time"

#ifdef __cplusplus
extern "C"
#endif
double
impl_csdms_examples_c_Heat_get_current_time(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_current_time) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    double time;

    CALL_BMI(Get_current_time, this->state, &time);

    return time;
  EXIT:;
    return -1.;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_current_time) */
  }
}

/*
 * Method:  get_end_time[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_end_time"

#ifdef __cplusplus
extern "C"
#endif
double
impl_csdms_examples_c_Heat_get_end_time(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_end_time) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    double time;

    CALL_BMI(Get_end_time, this->state, &time);
    return time;
  EXIT:;
    return -1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_end_time) */
  }
}

/*
 * Method:  get_values[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_values"

#ifdef __cplusplus
extern "C"
#endif
struct sidl__array*
impl_csdms_examples_c_Heat_get_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_values) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_values} (get_values method)
      */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_values) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_values) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_values) */
  }
}

/*
 * Method:  set_values[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_set_values"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat_set_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<> */ struct sidl__array* in_values,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.set_values) */
    /* Insert-Code-Here {csdms.examples.c.Heat.set_values} (set_values method)
      */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.set_values) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.set_values) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.set_values) */
  }
}

/*
 * Method:  get_component_name[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_component_name"

#ifdef __cplusplus
extern "C"
#endif
char*
impl_csdms_examples_c_Heat_get_component_name(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_component_name) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    char *name = (char*)malloc(sizeof(char) * 2048);

    CALL_BMI(Get_component_name, this->state, name);
    return name;

  EXIT:
    free(name);
    return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_component_name) */
  }
}

/*
 * Method:  get_input_item_count[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_input_item_count"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_csdms_examples_c_Heat_get_input_item_count(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_input_item_count) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    int number_of_names = 0;
    CALL_BMI(Get_input_var_name_count, this->state, &number_of_names);
    return number_of_names;

    EXIT: return -1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_input_item_count) */
  }
}

/*
 * Method:  get_input_item_list[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_input_item_list"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_string__array*
impl_csdms_examples_c_Heat_get_input_item_list(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_input_item_list) */
    struct sidl_string__array* item_names_array = NULL;
    char **item_names = NULL;
    const int MAX_NAME_LENGTH = 2048;
    int number_of_names = 0;
    int i;

    GET_PRIVATE_DATA_OR_RAISE(this);
    CALL_BMI(Get_input_var_name_count, this->state, &number_of_names);

    item_names = (char**)malloc(sizeof(char*) * number_of_names);
    item_names[0] = (char*)calloc(number_of_names * MAX_NAME_LENGTH,
        sizeof(char));
    for (i = 1; i < number_of_names; i ++) {
      item_names[i] = item_names[i - 1] + MAX_NAME_LENGTH;
    }

    CALL_BMI(Get_input_var_names, this->state, item_names);

    item_names_array = sidl_string__array_create1d(number_of_names);
    for (i = 0; i < number_of_names; i ++) {
      sidl_string__array_set1(item_names_array, i, item_names[i]);
    }
    free(item_names);

    return item_names_array;

    EXIT: return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_input_item_list) */
  }
}

/*
 * Method:  get_output_item_count[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_output_item_count"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_csdms_examples_c_Heat_get_output_item_count(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_output_item_count) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    int number_of_names = 0;
    CALL_BMI(Get_output_var_name_count, this->state, &number_of_names);
    return number_of_names;

    EXIT: return -1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_output_item_count) */
  }
}

/*
 * Method:  get_output_item_list[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_output_item_list"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_string__array*
impl_csdms_examples_c_Heat_get_output_item_list(
  /* in */ csdms_examples_c_Heat self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_output_item_list) */
    struct sidl_string__array* item_names_array = NULL;
    char **item_names = NULL;
    const int MAX_NAME_LENGTH = 2048;
    int number_of_names = 0;
    int i;

    GET_PRIVATE_DATA_OR_RAISE(this);
    CALL_BMI(Get_output_var_name_count, this->state, &number_of_names);

    item_names = (char**)malloc(sizeof(char*) * number_of_names);
    item_names[0] = (char*)calloc(number_of_names * MAX_NAME_LENGTH,
        sizeof(char));
    for (i = 1; i < number_of_names; i ++) {
      item_names[i] = item_names[i - 1] + MAX_NAME_LENGTH;
    }

    CALL_BMI(Get_output_var_names, this->state, item_names);

    item_names_array = sidl_string__array_create1d(number_of_names);
    for (i = 0; i < number_of_names; i ++) {
      sidl_string__array_set1(item_names_array, i, item_names[i]);
    }
    free(item_names);

    return item_names_array;

    EXIT: return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_output_item_list) */
  }
}

/*
 * Method:  get_values_at_indices[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_values_at_indices"

#ifdef __cplusplus
extern "C"
#endif
struct sidl__array*
impl_csdms_examples_c_Heat_get_values_at_indices(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<int> */ struct sidl_int__array* indices,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_values_at_indices) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_values_at_indices} (
      get_values_at_indices method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_values_at_indices) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_values_at_indices) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_values_at_indices) */
  }
}

/*
 * Method:  set_values_at_indices[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_set_values_at_indices"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat_set_values_at_indices(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<int> */ struct sidl_int__array* indices,
  /* in array<> */ struct sidl__array* in_values,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.set_values_at_indices) */
    /* Insert-Code-Here {csdms.examples.c.Heat.set_values_at_indices} (
      set_values_at_indices method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.set_values_at_indices) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.set_values_at_indices) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.set_values_at_indices) */
  }
}

/*
 * Method:  get_grid_rank[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_rank"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_csdms_examples_c_Heat_get_grid_rank(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_rank) */
    GET_PRIVATE_DATA_OR_RAISE(this);

    int rank;
    CALL_BMI(Get_var_rank, this->state, long_var_name, &rank);
    if (rank == 0)
      rank = 1;

    return rank;

EXIT:

    return -1;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_rank) */
  }
}

/*
 * Method:  get_grid_spacing[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_spacing"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_spacing(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_spacing) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    struct sidl_double__array* spacing = NULL;
    int rank;

    rank = impl_csdms_examples_c_Heat_get_grid_rank(self, long_var_name, _ex);

    spacing = sidl_double__array_create1d(rank);

    CALL_BMI(Get_grid_spacing, this->state, long_var_name,
        sidl_double__array_first(spacing));

    return spacing;

EXIT:

    return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_spacing) */
  }
}

/*
 * Method:  get_grid_origin[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_origin"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_origin(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_origin) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    struct sidl_double__array* origin = NULL;
    int rank;

    rank = impl_csdms_examples_c_Heat_get_grid_rank(self, long_var_name, _ex);

    origin = sidl_double__array_create1d(rank);

    CALL_BMI(Get_grid_origin, this->state, long_var_name,
        sidl_double__array_first(origin));

    return origin;

EXIT:
    return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_origin) */
  }
}

/*
 * Method:  get_grid_shape[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_shape"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_int__array*
impl_csdms_examples_c_Heat_get_grid_shape(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_shape) */
    GET_PRIVATE_DATA_OR_RAISE(this);
    struct sidl_int__array* shape = NULL;
    int rank;

    rank = impl_csdms_examples_c_Heat_get_grid_rank(self, long_var_name, _ex);

    shape = sidl_int__array_create1d(rank);

    CALL_BMI(Get_grid_shape, this->state, long_var_name,
        sidl_int__array_first(shape));

    return shape;

EXIT:
    return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_shape) */
  }
}

/*
 * Method:  get_grid_x[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_x"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_x(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_x) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_grid_x} (get_grid_x method)
      */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_grid_x) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_grid_x) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_x) */
  }
}

/*
 * Method:  get_grid_y[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_y"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_y(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_y) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_grid_y} (get_grid_y method)
      */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_grid_y) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_grid_y) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_y) */
  }
}

/*
 * Method:  get_grid_z[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_z"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_z(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_z) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_grid_z} (get_grid_z method)
      */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_grid_z) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_grid_z) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_z) */
  }
}

/*
 * Method:  get_grid_connectivity[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_connectivity"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_int__array*
impl_csdms_examples_c_Heat_get_grid_connectivity(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_connectivity) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_grid_connectivity} (
      get_grid_connectivity method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_grid_connectivity) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_grid_connectivity) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_connectivity) */
  }
}

/*
 * Method:  get_grid_offset[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_offset"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_int__array*
impl_csdms_examples_c_Heat_get_grid_offset(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_offset) */
    /* Insert-Code-Here {csdms.examples.c.Heat.get_grid_offset} (
      get_grid_offset method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.get_grid_offset) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.get_grid_offset) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_offset) */
  }
}

/*
 * Method:  get_grid_values[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_get_grid_values"

#ifdef __cplusplus
extern "C"
#endif
struct sidl_double__array*
impl_csdms_examples_c_Heat_get_grid_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.get_grid_values) */
    GET_PRIVATE_DATA_OR_RAISE(this);

    if (this && this->state)
    {
      int status = 0;

      if (values) {
        CALL_BMI(Get_value, this->state, long_var_name,
            sidl_char__array_first((struct sidl_char__array*)(values)));
        return values;
      } else {
        int rank = 0;
        int size = 0;
        void *data = NULL;
        char type[2048];

        CALL_BMI(Get_value_ptr, this->state, long_var_name, &data);
        CALL_BMI(Get_var_size, this->state, long_var_name, &size);
        CALL_BMI(Get_var_type, this->state, long_var_name, type);

        if (data) { /* Create an array that borrows these values. */
          const int n_dims = 1;
          const int lower[1] = {0};
          const int upper[1] = {size - 1};
          const int stride[1] = {1};

          if (strcmp(type, "double") == 0) {
            values = (struct sidl__array*)sidl_double__array_borrow(data, n_dims,
                lower, upper, stride);
          } else if (strcmp(type, "int") == 0) {
            values = (struct sidl__array*)sidl_int__array_borrow(data, n_dims,
                lower, upper, stride);
          }

        } else { /* Create a new array to hold the values*/
          void * buffer = NULL;

          if (strcmp(type, "double") == 0) {
            values = (struct sidl__array*)sidl_double__array_create1d(size);
            buffer = (void*)sidl_double__array_first((struct sidl_double__array*)values);
          } else if (strcmp(type, "int") == 0) {
            values = (struct sidl__array*)sidl_int__array_create1d(size);
            buffer = (void*)sidl_int__array_first((struct sidl_int__array*)values);
          }

          if (buffer)
            CALL_BMI(Get_value, this->state, long_var_name, buffer);
        }
      }
    }

    return values;

  EXIT: return NULL;
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.get_grid_values) */
  }
}

/*
 * Method:  set_grid_values[]
 */

#undef __FUNC__
#define __FUNC__ "impl_csdms_examples_c_Heat_set_grid_values"

#ifdef __cplusplus
extern "C"
#endif
void
impl_csdms_examples_c_Heat_set_grid_values(
  /* in */ csdms_examples_c_Heat self,
  /* in */ const char* long_var_name,
  /* in array<double> */ struct sidl_double__array* vals,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(csdms.examples.c.Heat.set_grid_values) */
    /* Insert-Code-Here {csdms.examples.c.Heat.set_grid_values} (
      set_grid_values method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.c.Heat.set_grid_values) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.c.Heat.set_grid_values) */
    /* DO-NOT-DELETE splicer.end(csdms.examples.c.Heat.set_grid_values) */
  }
}
/* Babel internal methods, Users should not edit below this line. */

/* DO-NOT-DELETE splicer.begin(_misc) */
/* Insert-Code-Here {_misc} (miscellaneous code) */
/* DO-NOT-DELETE splicer.end(_misc) */

