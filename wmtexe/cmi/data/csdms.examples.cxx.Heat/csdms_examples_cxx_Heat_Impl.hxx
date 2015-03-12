// 
// File:          csdms_examples_cxx_Heat_Impl.hxx
// Symbol:        csdms.examples.cxx.Heat-v0.0
// Symbol Type:   class
// Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
// Description:   Server-side implementation for csdms.examples.cxx.Heat
// 
// WARNING: Automatically generated; only changes within splicers preserved
// 
// 

#ifndef included_csdms_examples_cxx_Heat_Impl_hxx
#define included_csdms_examples_cxx_Heat_Impl_hxx

#ifndef included_sidl_cxx_hxx
#include "sidl_cxx.hxx"
#endif
#ifndef included_csdms_examples_cxx_Heat_IOR_h
#include "csdms_examples_cxx_Heat_IOR.h"
#endif
#ifndef included_csdms_core_Bmi_hxx
#include "csdms_core_Bmi.hxx"
#endif
#ifndef included_csdms_examples_cxx_Heat_hxx
#include "csdms_examples_cxx_Heat.hxx"
#endif
#ifndef included_sidl_BaseClass_hxx
#include "sidl_BaseClass.hxx"
#endif
#ifndef included_sidl_BaseInterface_hxx
#include "sidl_BaseInterface.hxx"
#endif
#ifndef included_sidl_ClassInfo_hxx
#include "sidl_ClassInfo.hxx"
#endif


// DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._hincludes)
// Insert-Code-Here {csdms.examples.cxx.Heat._hincludes} (includes or arbitrary code)
${bmi_includes}
${bmi_defines}

#define CALL_BMI_VOID(func,...) { \
  try { \
    state.func(__VA_ARGS__); \
  } catch (int e) { \
    BOCCA_THROW_CXX(::sidl::SIDLException, "Error running " #func); \
  } \
}


#define CALL_BMI(rtn,func,...) { \
  try { \
    rtn = state.func(__VA_ARGS__); \
  } catch (int e) { \
    BOCCA_THROW_CXX(::sidl::SIDLException, "Error running " #func); \
  } \
}

// DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._hincludes)

namespace csdms { 
  namespace examples { 
    namespace cxx { 

      /**
       * Symbol "csdms.examples.cxx.Heat" (version 0.0)
       */
      class Heat_impl : public virtual ::csdms::examples::cxx::Heat 
      // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._inherits)
    // Insert-Code-Here {csdms.examples.cxx.Heat._inherits} (optional inheritance here)
      // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._inherits)

      {

      // All data marked protected will be accessable by 
      // descendant Impl classes
      protected:

        bool _wrapped;

        // DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._implementation)
        ${bmi_type} state;
        //bmi::Model state;
        // DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._implementation)

      public:
        // default constructor, used for data wrapping(required)
        Heat_impl();
        // sidl constructor (required)
        // Note: alternate Skel constructor doesn't call addref()
        // (fixes bug #275)
          Heat_impl( struct csdms_examples_cxx_Heat__object * ior ) : StubBase(
            ior,true), 
        ::csdms::core::Bmi((ior==NULL) ? NULL : &((*ior).d_csdms_core_bmi)) , 
          _wrapped(false) {_ctor();}


        // user defined construction
        void _ctor();

        // virtual destructor (required)
        virtual ~Heat_impl() { _dtor(); }

        // user defined destruction
        void _dtor();

        // true if this object was created by a user newing the impl
        inline bool _isWrapped() {return _wrapped;}

        // static class initializer
        static void _load();

      public:


        /**
         *  This function should never be called, but helps babel generate better code. 
         */
        void
        boccaForceUsePortInclude_impl() ;
        /**
         * user defined non-static method.
         */
        bool
        initialize_impl (
          /* in */const ::std::string& config_file
        )
        ;

        /**
         * user defined non-static method.
         */
        bool
        update_impl (
          /* in */double time_interval
        )
        ;

        /**
         * user defined non-static method.
         */
        bool
        finalize_impl() ;
        /**
         * user defined non-static method.
         */
        double
        get_start_time_impl() ;
        /**
         * user defined non-static method.
         */
        double
        get_current_time_impl() ;
        /**
         * user defined non-static method.
         */
        double
        get_end_time_impl() ;
        /**
         * user defined non-static method.
         */
        ::sidl::basearray
        get_values_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        void
        set_values_impl (
          /* in */const ::std::string& long_var_name,
          /* in array<> */::sidl::basearray& in_values
        )
        ;

        /**
         * user defined non-static method.
         */
        ::std::string
        get_component_name_impl() ;
        /**
         * user defined non-static method.
         */
        int32_t
        get_input_item_count_impl() ;
        /**
         * user defined non-static method.
         */
        ::sidl::array< ::std::string>
        get_input_item_list_impl() ;
        /**
         * user defined non-static method.
         */
        int32_t
        get_output_item_count_impl() ;
        /**
         * user defined non-static method.
         */
        ::sidl::array< ::std::string>
        get_output_item_list_impl() ;
        /**
         * user defined non-static method.
         */
        ::sidl::basearray
        get_values_at_indices_impl (
          /* in */const ::std::string& long_var_name,
          /* in array<int> */::sidl::array<int32_t>& indices
        )
        ;

        /**
         * user defined non-static method.
         */
        void
        set_values_at_indices_impl (
          /* in */const ::std::string& long_var_name,
          /* in array<int> */::sidl::array<int32_t>& indices,
          /* in array<> */::sidl::basearray& in_values
        )
        ;

        /**
         * user defined non-static method.
         */
        int32_t
        get_grid_rank_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<double>
        get_grid_spacing_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<double>
        get_grid_origin_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<int32_t>
        get_grid_shape_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<double>
        get_grid_x_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<double>
        get_grid_y_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<double>
        get_grid_z_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<int32_t>
        get_grid_connectivity_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<int32_t>
        get_grid_offset_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        ::sidl::array<double>
        get_grid_values_impl (
          /* in */const ::std::string& long_var_name
        )
        ;

        /**
         * user defined non-static method.
         */
        void
        set_grid_values_impl (
          /* in */const ::std::string& long_var_name,
          /* in array<double> */::sidl::array<double>& vals
        )
        ;

      };  // end class Heat_impl

    } // end namespace cxx
  } // end namespace examples
} // end namespace csdms

// DO-NOT-DELETE splicer.begin(csdms.examples.cxx.Heat._hmisc)
// Insert-Code-Here {csdms.examples.cxx.Heat._hmisc} (miscellaneous things)
// DO-NOT-DELETE splicer.end(csdms.examples.cxx.Heat._hmisc)

#endif
