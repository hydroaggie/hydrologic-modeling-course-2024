ptf !

#Description: 1D problem for flow and tracer transport

#=========================== flow and transport mode ========================================
SIMULATION
  SIMULATION_TYPE SUBSURFACE
  PROCESS_MODELS
    SUBSURFACE_FLOW flow
      MODE RICHARDS
    /
    SUBSURFACE_TRANSPORT transport
      MODE GIRT
    /
  /
END  

SUBSURFACE
#=========================== numerical methods ================================
NUMERICAL_METHODS FLOW
  NEWTON_SOLVER
  /
END 

NUMERICAL_METHODS TRANSPORT
  TIMESTEPPER
    CFL_GOVERNOR 1.d0 #set CFL=1 to limit timestep so dt<dx/v_max
  /
  NEWTON_SOLVER
  /
END

#=========================== chemistry ========================================
CHEMISTRY
  PRIMARY_SPECIES
    Tracer # add conservative tracer as the species
  /
  OUTPUT # IMPORTANT: add output block to write concentration to file
    ALL
    TOTAL
  /  
END

#=========================== discretization ===================================
GRID
  TYPE STRUCTURED
  NXYZ 100 1 1
  BOUNDS
    0.d0 0.d0 0.d0
    40.d0 1.d0 1.d0
  /
END

#=========================== fluid properties =================================
FLUID_PROPERTY 
  DIFFUSION_COEFFICIENT 1.d-9 
/

#=========================== material properties ==============================
MATERIAL_PROPERTY soil1
  ID 1
  POROSITY 0.25d0
  TORTUOSITY 1.d0 #for calculating effective diffusion coefficient
  PERMEABILITY
    PERM_ISO 2.d-11 
  /
  CHARACTERISTIC_CURVES default
  LONGITUDINAL_DISPERSIVITY !aL         ! m
END

#=========================== characteristic curves ============================
CHARACTERISTIC_CURVES default
  SATURATION_FUNCTION VAN_GENUCHTEN
    ALPHA 1.d-4
    M 0.5d0
    LIQUID_RESIDUAL_SATURATION 0.1d0
  /
  PERMEABILITY_FUNCTION MUALEM_VG_LIQ
    M 0.5d0
    LIQUID_RESIDUAL_SATURATION 0.1d0
  /
END

#=========================== output options ===================================
OUTPUT
  TIME_UNITS d
#  SNAPSHOT_FILE
#      NO_PRINT_INITIAL
#      PERIODIC TIME 1. d between 1. d and 9. d
#      FORMAT TECPLOT POINT
#  /
#  FORMAT HDF5
  PERIODIC_OBSERVATION TIMESTEP 1
#  VELOCITY_AT_CENTER
END

#=========================== times ============================================
TIME
  FINAL_TIME 10.d0 d
  INITIAL_TIMESTEP_SIZE 1.d-3 h
  MAXIMUM_TIMESTEP_SIZE 1.d0 d
END

#=========================== regions ==========================================
REGION all
  COORDINATES
    0.d0 0.d0 0.d0
    40.d0 1.d0 1.d0
  /
END

REGION west
  FACE WEST
  COORDINATES
    0.d0 0.d0 0.d0
    0.d0 1.d0 1.d0
  /
END

REGION east
  FACE EAST
  COORDINATES
    40.d0 0.d0 0.d0
    40.d0 1.d0 1.d0
  /
END

REGION middle
  COORDINATE 20d0 0.5d0 0.5d0
END

#=========================== observation points ===============================
OBSERVATION
  REGION middle
  VELOCITY
END


#=========================== flow conditions ==================================

FLOW_CONDITION initial
  TYPE
    LIQUID_PRESSURE HYDROSTATIC
  /
  DATUM 0.d0 0.d0 5.d0
  GRADIENT
    LIQUID_PRESSURE -0.1 0.d0 0.d0 #head gradient dh/dx = (1-5)/40 = 0.1 m/m
  /
  LIQUID_PRESSURE 101325.0 
END

FLOW_CONDITION inlet
  TYPE
    LIQUID_PRESSURE HYDROSTATIC
  /
  DATUM 0.d0 0.d0 5.d0
  LIQUID_PRESSURE 101325.0 
/

FLOW_CONDITION outlet
  TYPE
    LIQUID_PRESSURE HYDROSTATIC
  /
  DATUM 0.d0 0.d0 1.d0
  LIQUID_PRESSURE 101325.0 
/


#=========================== transport conditions =============================
TRANSPORT_CONDITION initial
  TYPE ZERO_GRADIENT #mass is allowed to exit via advection with the following water, but not due to dispersion
  CONSTRAINT_LIST
    0.d0 initial
  /
END

TRANSPORT_CONDITION inlet
  TYPE DIRICHLET_ZERO_GRADIENT
  CONSTRAINT_LIST
    0.d0 inlet
  /
END

#=========================== constraints ======================================
CONSTRAINT initial
  CONCENTRATIONS
    Tracer 1.d-20  T # T = total aqueous component concentration. Default units [mol/L]
  /
END

CONSTRAINT inlet
  CONCENTRATIONS
    Tracer 1.d0  T
  /
END

#=========================== condition couplers ===============================
# initial condition
INITIAL_CONDITION
  FLOW_CONDITION initial
  TRANSPORT_CONDITION initial
  REGION all
END


# west boundary condition
BOUNDARY_CONDITION inlet
  FLOW_CONDITION inlet
  TRANSPORT_CONDITION inlet
  REGION west
END

# east boundary condition
BOUNDARY_CONDITION outlet
  FLOW_CONDITION outlet
  TRANSPORT_CONDITION initial
  REGION east
END

#=========================== stratigraphy couplers ============================
STRATA
  REGION all
  MATERIAL soil1
END


END_SUBSURFACE
