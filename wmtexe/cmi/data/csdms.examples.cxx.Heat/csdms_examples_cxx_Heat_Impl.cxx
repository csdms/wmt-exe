// 
// File:          csdms_examples_cxx_Heat_Impl.cxx
// Symbol:        csdms.examples.cxx.Heat-v0.0
// Symbol Type:   class
// Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
// Description:   Server-side implementation for csdms.examples.cxx.Heat
// 
// WARNING: Automatically generated; only changes within splicers preserved
// 
// 
#include "csdms_examples_cxx_Heat_Impl.hxx"

// 
// Includes for all method dependencies.
// 
#ifndef included_sidl_BaseInterface_hxx
#include "sidl_BaseInterface.hxx"
#endif
#ifndef included_sidl_ClassInfo_hxx
#include "sidl_ClassInfo.hxx"
#endif
#ifndef included_sidl_NotImplementedException_hxx
#include "sidl_NotImplementedException.hxx"
#endif
// DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._includes)

  // Insert-UserCode-Here {csdms.examples.cxx.Heat._includes:prolog} (additional includes or code)

  // Bocca generated code. bocca.protected.begin(csdms.examples.cxx.Heat._includes)

#define _BOCCA_CTOR_MESSAGES 0
  // If -D_BOCCA_STDERR is given to the compiler, diagnostics print to stderr.
  // In production use, probably want not to use -D_BOCCA_STDERR.
#ifdef _BOCCA_STDERR

#include <iostream>

#ifdef _BOCCA_CTOR_PRINT
#undef _BOCCA_CTOR_MESSAGES
#define _BOCCA_CTOR_MESSAGES 1
#endif // _BOCCA_CTOR_PRINT
#else  // _BOCCA_STDERR


#endif // _BOCCA_STDERR



  // If -D_BOCCA_BOOST is given to the compiler, exceptions and diagnostics
  // will include function names for boost-understood compilers.
  // If boost is not available (and therefore ccaffeine is not in use),
  // -D_BOCCA_BOOST can be omitted and function names will not be included in
  // messages.
#ifndef _BOCCA_BOOST
#define BOOST_CURRENT_FUNCTION ""
#else
#include <boost/current_function.hpp>
#endif

  // This is intended to simplify exception throwing as SIDL_THROW does for C.
#define BOCCA_THROW_CXX(EX_CLS, MSG) \
{ \
    EX_CLS ex = EX_CLS::_create(); \
    ex.setNote( MSG ); \
    ex.add(__FILE__, __LINE__, BOOST_CURRENT_FUNCTION); \
    throw ex; \
}

  // This simplifies exception extending and rethrowing in c++, like
  // SIDL_CHECK in C. EX_OBJ must be the caught exception and is extended with
  // msg and file/line/func added. Continuing the throw is up to the user.
#define BOCCA_EXTEND_THROW_CXX(EX_OBJ, MSG, LINEOFFSET) \
{ \
  std::string msg = std::string(MSG) + std::string(BOOST_CURRENT_FUNCTION); \
  EX_OBJ.add(__FILE__,__LINE__ + LINEOFFSET, msg); \
}


  // Bocca generated code. bocca.protected.end(csdms.examples.cxx.Heat._includes)

  // Insert-UserCode-Here {csdms.examples.cxx.Heat._includes:epilog} (additional includes or code)

// DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._includes)

// special constructor, used for data wrapping(required).  Do not put code here unless you really know what you're doing!
csdms::examples::cxx::Heat_impl::Heat_impl() : StubBase(reinterpret_cast< 
  void*>(::csdms::examples::cxx::Heat::_wrapObj(reinterpret_cast< void*>(
  this))),false) , _wrapped(true){ 
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._ctor2)
  // Insert-Code-Here {csdms.examples.cxx.Heat._ctor2} (ctor2)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._ctor2)
}

// user defined constructor
void csdms::examples::cxx::Heat_impl::_ctor() {
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._ctor)

  // Insert-UserCode-Here {csdms.examples.cxx.Heat._ctor:prolog} (constructor method)

  // bocca-default-code. User may edit or delete.begin(csdms.examples.cxx.Heat._ctor)
   #if _BOCCA_CTOR_MESSAGES

     std::cerr << "CTOR csdms.examples.cxx.Heat: " << BOOST_CURRENT_FUNCTION
               << " constructing " << this << std::endl;

   #endif // _BOCCA_CTOR_MESSAGES
  // bocca-default-code. User may edit or delete.end(csdms.examples.cxx.Heat._ctor)

  // Insert-UserCode-Here {csdms.examples.cxx.Heat._ctor:epilog} (constructor method)

  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._ctor)
}

// user defined destructor
void csdms::examples::cxx::Heat_impl::_dtor() {
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._dtor)
  // Insert-UserCode-Here {csdms.examples.cxx.Heat._dtor} (destructor method)

  // bocca-default-code. User may edit or delete.begin(csdms.examples.cxx.Heat._dtor)
   #if _BOCCA_CTOR_MESSAGES

     std::cerr << "DTOR csdms.examples.cxx.Heat: " << BOOST_CURRENT_FUNCTION
               << " destructing " << this << std::endl;

   #endif // _BOCCA_CTOR_MESSAGES
  // bocca-default-code. User may edit or delete.end(csdms.examples.cxx.Heat._dtor)

  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._dtor)
}

// static class initializer
void csdms::examples::cxx::Heat_impl::_load() {
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._load)
  // Insert-Code-Here {csdms.examples.cxx.Heat._load} (class initialization)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._load)
}

// user defined static methods: (none)

// user defined non-static methods:
/**
 *  This function should never be called, but helps babel generate better code. 
 */
void
csdms::examples::cxx::Heat_impl::boccaForceUsePortInclude_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.boccaForceUsePortInclude)
  // DO-NOT-EDIT-BOCCA
  // Bocca generated code. bocca.protected.begin(csdms.examples.cxx.Heat.boccaForceUsePortInclude)

  // Bocca generated code. bocca.protected.end(csdms.examples.cxx.Heat.boccaForceUsePortInclude)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.boccaForceUsePortInclude)
}

/**
 * Method:  initialize[]
 */
bool
csdms::examples::cxx::Heat_impl::initialize_impl (
  /* in */const ::std::string& config_file ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.initialize)
  CALL_BMI_VOID(Initialize, config_file.c_str());
  return 0;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.initialize)
}

/**
 * Method:  update[]
 */
bool
csdms::examples::cxx::Heat_impl::update_impl (
  /* in */double time_interval ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.update)
  CALL_BMI_VOID(UpdateUntil, time_interval);
  return 0;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.update)
}

/**
 * Method:  finalize[]
 */
bool
csdms::examples::cxx::Heat_impl::finalize_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.finalize)
  CALL_BMI_VOID(Finalize);
  return 0;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.finalize)
}

/**
 * Method:  get_start_time[]
 */
double
csdms::examples::cxx::Heat_impl::get_start_time_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_start_time)
  double time;
  CALL_BMI_VOID(GetStartTime, &time);
  return time;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_start_time)
}

/**
 * Method:  get_current_time[]
 */
double
csdms::examples::cxx::Heat_impl::get_current_time_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_current_time)
  double time;
  CALL_BMI_VOID(GetCurrentTime, &time);
  return time;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_current_time)
}

/**
 * Method:  get_end_time[]
 */
double
csdms::examples::cxx::Heat_impl::get_end_time_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_end_time)
  double time;
  CALL_BMI_VOID(GetEndTime, &time);
  return time;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_end_time)
}

/**
 * Method:  get_values[]
 */
::sidl::basearray
csdms::examples::cxx::Heat_impl::get_values_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_values)
  // Insert-Code-Here {csdms.examples.cxx.Heat.get_values} (get_values method)
  //
  // This method has not been implemented
  //
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.cxx.Heat.get_values)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_values");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.cxx.Heat.get_values)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_values)
}

/**
 * Method:  set_values[]
 */
void
csdms::examples::cxx::Heat_impl::set_values_impl (
  /* in */const ::std::string& long_var_name,
  /* in array<> */::sidl::basearray& in_values ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.set_values)
  // Insert-Code-Here {csdms.examples.cxx.Heat.set_values} (set_values method)
  //
  // This method has not been implemented
  //
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.cxx.Heat.set_values)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "set_values");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.cxx.Heat.set_values)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.set_values)
}

/**
 * Method:  get_component_name[]
 */
::std::string
csdms::examples::cxx::Heat_impl::get_component_name_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_component_name)
  char name[2048];
  CALL_BMI_VOID(GetComponentName, name);
  return std::string(name);
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_component_name)
}

/**
 * Method:  get_input_item_count[]
 */
int32_t
csdms::examples::cxx::Heat_impl::get_input_item_count_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_input_item_count)
  int number_of_names = 0;
  CALL_BMI_VOID(GetInputVarNameCount, &number_of_names)
  return number_of_names;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_input_item_count)
}

/**
 * Method:  get_input_item_list[]
 */
::sidl::array< ::std::string>
csdms::examples::cxx::Heat_impl::get_input_item_list_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_input_item_list)
  ::sidl::array< ::std::string> input_item_array = NULL;

  {
    const int MAX_NAME_LENGTH = 512;
    int number_of_names = 0;
    char **input_item_names = NULL;

    CALL_BMI_VOID(GetInputVarNameCount, &number_of_names);

    input_item_names = (char**)malloc(sizeof(char*) * number_of_names);
    input_item_names[0] = (char*)calloc(number_of_names * MAX_NAME_LENGTH,
        sizeof(char));
    for (int i = 1; i < number_of_names; i ++) {
      input_item_names[i] = input_item_names[i - 1] + MAX_NAME_LENGTH;
    }

    CALL_BMI_VOID(GetInputVarNames, input_item_names);

    input_item_array = sidl::array< ::std::string>::create1d(number_of_names);
    for (int i = 0; i < number_of_names; i ++) {
      input_item_array.set(i, ::std::string(input_item_names[i]));
    }
    free(input_item_names[0]);
    free(input_item_names);
  }

  return input_item_array;

  EXIT: return NULL;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_input_item_list)
}

/**
 * Method:  get_output_item_count[]
 */
int32_t
csdms::examples::cxx::Heat_impl::get_output_item_count_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_output_item_count)
  int number_of_names = 0;
  CALL_BMI_VOID(GetOutputVarNameCount, &number_of_names)
  return number_of_names;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_output_item_count)
}

/**
 * Method:  get_output_item_list[]
 */
::sidl::array< ::std::string>
csdms::examples::cxx::Heat_impl::get_output_item_list_impl () 

{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_output_item_list)
  ::sidl::array< ::std::string> output_item_array = NULL;

  {
    const int MAX_NAME_LENGTH = 512;
    int number_of_names = 0;
    char **output_item_names = NULL;

    CALL_BMI_VOID(GetOutputVarNameCount, &number_of_names);

    output_item_names = (char**)malloc(sizeof(char*) * number_of_names);
    output_item_names[0] = (char*)calloc(number_of_names * MAX_NAME_LENGTH,
        sizeof(char));
    for (int i = 1; i < number_of_names; i ++) {
      output_item_names[i] = output_item_names[i - 1] + MAX_NAME_LENGTH;
    }

    CALL_BMI_VOID(GetOutputVarNames, output_item_names);

    output_item_array = sidl::array< ::std::string>::create1d(number_of_names);
    for (int i = 0; i < number_of_names; i ++) {
      output_item_array.set(i, ::std::string(output_item_names[i]));
    }
    free(output_item_names[0]);
    free(output_item_names);
  }

  return output_item_array;

  EXIT: return NULL;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_output_item_list)
}

/**
 * Method:  get_values_at_indices[]
 */
::sidl::basearray
csdms::examples::cxx::Heat_impl::get_values_at_indices_impl (
  /* in */const ::std::string& long_var_name,
  /* in array<int> */::sidl::array<int32_t>& indices ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_values_at_indices)
  // Insert-Code-Here {csdms.examples.cxx.Heat.get_values_at_indices} (get_values_at_indices method)
  //
  // This method has not been implemented
  //
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.cxx.Heat.get_values_at_indices)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_values_at_indices");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.cxx.Heat.get_values_at_indices)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_values_at_indices)
}

/**
 * Method:  set_values_at_indices[]
 */
void
csdms::examples::cxx::Heat_impl::set_values_at_indices_impl (
  /* in */const ::std::string& long_var_name,
  /* in array<int> */::sidl::array<int32_t>& indices,
  /* in array<> */::sidl::basearray& in_values ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.set_values_at_indices)
  // Insert-Code-Here {csdms.examples.cxx.Heat.set_values_at_indices} (set_values_at_indices method)
  //
  // This method has not been implemented
  //
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.cxx.Heat.set_values_at_indices)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "set_values_at_indices");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.cxx.Heat.set_values_at_indices)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.set_values_at_indices)
}

/**
 * Method:  get_grid_rank[]
 */
int32_t
csdms::examples::cxx::Heat_impl::get_grid_rank_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_rank)
  // Insert-Code-Here {csdms.examples.cxx.Heat.get_grid_rank} (get_grid_rank method)
  //
  // This method has not been implemented
  //
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(csdms.examples.cxx.Heat.get_grid_rank)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_rank");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(csdms.examples.cxx.Heat.get_grid_rank)
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_rank)
}

/**
 * Method:  get_grid_spacing[]
 */
::sidl::array<double>
csdms::examples::cxx::Heat_impl::get_grid_spacing_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_spacing)
  ::sidl::array<double> spacing = NULL;
  char grid_type[2048];

#if defined(BMI_HAS_GET_GRID_SPACING)
  CALL_BMI_VOID(GetGridType, long_var_name.c_str(), grid_type);
  if (strcmp(grid_type, "uniform_rectilinear") == 0) {
    int rank;
    CALL_BMI_VOID(GetVarRank, long_var_name.c_str(), &rank);
    if (rank == 0)
      rank = 1;

    spacing = sidl::array<double>::create1d(rank);
    CALL_BMI_VOID(GetGridSpacing, long_var_name.c_str(),
        spacing.first());
  }
  return spacing;

  EXIT: return NULL;
#else
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_spacing");
  throw ex;
#endif
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_spacing)
}

/**
 * Method:  get_grid_origin[]
 */
::sidl::array<double>
csdms::examples::cxx::Heat_impl::get_grid_origin_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_origin)
  ::sidl::array<double> origin = NULL;
  char grid_type[2048];
  
#if defined(BMI_HAS_GET_GRID_ORIGIN)
  CALL_BMI_VOID(GetGridType, long_var_name.c_str(), grid_type);
  if (strcmp(grid_type, "uniform_rectilinear") == 0) {
    int rank;
    CALL_BMI_VOID(GetVarRank, long_var_name.c_str(), &rank);
    if (rank == 0)
      rank = 1;

    origin = sidl::array<double>::create1d(rank);
    CALL_BMI_VOID(GetGridOrigin, long_var_name.c_str(),
        origin.first());
  }
  return origin;

  EXIT: return NULL;
#else
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_origin");
  throw ex;
#endif
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_origin)
}

/**
 * Method:  get_grid_shape[]
 */
::sidl::array<int32_t>
csdms::examples::cxx::Heat_impl::get_grid_shape_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_shape)
  ::sidl::array<int> shape = NULL;
  char grid_type[2048];

#if defined(BMI_HAS_GET_GRID_SHAPE)
  CALL_BMI_VOID(GetGridType, long_var_name.c_str(), grid_type);
  if (strcmp(grid_type, "structured") == 0) {
    int rank;
    CALL_BMI_VOID(GetVarRank, long_var_name.c_str(), &rank);
    if (rank == 0)
      rank = 1;

    shape = sidl::array<int>::create1d(rank);
    CALL_BMI_VOID(GetGridShape, long_var_name.c_str(),
        shape.first());
  }
  return shape;

  EXIT: return NULL;
#else
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_shape");
  throw ex;
#endif
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_shape)
}

/**
 * Method:  get_grid_x[]
 */
::sidl::array<double>
csdms::examples::cxx::Heat_impl::get_grid_x_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_x)
  ::sidl::array<double> coord = NULL;
  int number_of_points = 0;

  CALL_BMI_VOID(GetVarSize, long_var_name.c_str(), &number_of_points);

  coord = sidl::array<double>::create1d(number_of_points);

  CALL_BMI_VOID(GetGridX, long_var_name.c_str(), coord.first());

  return coord;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_x)
}

/**
 * Method:  get_grid_y[]
 */
::sidl::array<double>
csdms::examples::cxx::Heat_impl::get_grid_y_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_y)
  sidl::array<double> coord = NULL;
  int number_of_points = 0;

  CALL_BMI_VOID(GetVarSize, long_var_name.c_str(), &number_of_points);

  coord = sidl::array<double>::create1d(number_of_points);

  CALL_BMI_VOID(GetGridY, long_var_name.c_str(), coord.first());

  return coord;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_y)
}

/**
 * Method:  get_grid_z[]
 */
::sidl::array<double>
csdms::examples::cxx::Heat_impl::get_grid_z_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_z)
#if defined(HAS_BMI_GET_GRID_Z)
  ::sidl::array<double> coord = NULL;
  int number_of_points = 0;

  CALL_BMI_VOID(GetVarSize, long_var_name.c_str(), &number_of_points);

  coord = sidl::array<double>::create1d(number_of_points);

  CALL_BMI_VOID(GetGridZ, long_var_name.c_str(), coord.first());

  return coord;
#else
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_z");
  throw ex;
#endif
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_z)
}

/**
 * Method:  get_grid_connectivity[]
 */
::sidl::array<int32_t>
csdms::examples::cxx::Heat_impl::get_grid_connectivity_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_connectivity)
#if defined(BMI_HAS_GET_GRID_CONNECTIVITY)
  ::sidl::array<int> connectivity = NULL;
  int number_of_vertices = 0;

  CALL_BMI_VOID(GetVarVertexCount, long_var_name.c_str(), &number_of_vertices);

  connectivity = sidl::array<int>::create1d(number_of_vertices);
  CALL_BMI_VOID(GetGridConnectivity, long_var_name.c_str(),
      connectivity.first());

  return connectivity;
#else
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_connectivity");
  throw ex;
#endif
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_connectivity)
}

/**
 * Method:  get_grid_offset[]
 */
::sidl::array<int32_t>
csdms::examples::cxx::Heat_impl::get_grid_offset_impl (
  /* in */const ::std::string& long_var_name ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_offset)
#if defined(BMI_HAS_GET_GRID_OFFSET)
  ::sidl::array<int> offset = NULL;
  int number_of_cells = 0;

  CALL_BMI_VOID(GetVarCellCount, long_var_name.c_str(), &number_of_cells);

  offset = sidl::array<int>::create1d(number_of_cells);
  CALL_BMI_VOID(GetGridOffset, long_var_name.c_str(), offset.first());

  return offset;
#else
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_grid_offset");
  throw ex;
#endif
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_offset)
}

/**
 * Method:  get_grid_values[]
 */
::sidl::basearray
csdms::model::HeatCxx_impl::get_grid_values_impl (
  /* in */const ::std::string& long_var_name,
  /* in array<> */::sidl::basearray& values ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.get_grid_values)
  if (values) {
    struct sidl__array * array = values._get_baseior();
    CALL_BMI_VOID(GetValue, long_var_name.c_str(),
          sidl_char__array_first((struct sidl_char__array*)(array)));
    return values;
  } else {
    int rank = 0;
    int size = 0;
    char *data = NULL;
    char type[2048];

    CALL_BMI_VOID(GetValuePtr, long_var_name.c_str(), &data);
    CALL_BMI_VOID(GetVarSize, long_var_name.c_str(), &size);
    CALL_BMI_VOID(GetVarType, long_var_name.c_str(), type);

    if (data) { /* Create an array that borrows these values. */
      const int lower[1] = {0};
      const int upper[1] = {size - 1};
      const int stride[1] = {1};

      if (strcmp(type, "double") == 0) {
        sidl::array<double> dvals;
        dvals.borrow((double*)data, 1, lower, upper, stride);
        values = dvals;
      } else if (strcmp(type, "int") == 0) {
        sidl::array<int> ivals;
        ivals.borrow((int*)data, 1, lower, upper, stride);
        values = ivals;
      }
    } else { /* Create a new array to hold the values*/
      char * buffer = NULL;

      if (strcmp(type, "double") == 0) {
        sidl::array<double> dvals;
        dvals = sidl::array<double>::create1d(size);
        buffer = (char*)dvals.first();
        values = dvals;
      } else if (strcmp(type, "int") == 0) {
        sidl::array<int> ivals;
        ivals = sidl::array<int>::create1d(size);
        buffer = (char*)ivals.first();
        values = ivals;
      }

      if (buffer)
        CALL_BMI_VOID(GetValue, long_var_name.c_str(), buffer);
    }
  }

  return values;

EXIT: return NULL;
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.get_grid_values)
}

/**
 * Method:  set_grid_values[]
 */
void
csdms::examples::cxx::Heat_impl::set_grid_values_impl (
  /* in */const ::std::string& long_var_name,
  /* in array<double> */::sidl::array<double>& vals ) 
{
  // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat.set_grid_values)
  CALL_BMI_VOID(SetValue, long_var_name.c_str(), (char*)vals.first());
  // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat.set_grid_values)
}


// DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._misc)
// Insert-Code-Here {csdms.examples.cxx.Heat._misc} (miscellaneous code)
// DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._misc)

