from pyradioconfig.calculator_model_framework.interfaces.iphy_filter import IPhyFilter


class PhyFiltersRainier(IPhyFilter):

    # Studio black list (files removed before Studio distribution)
    customer_phy_groups = ['Phys_imagotag',
                           'Phys_Internal_Base_Experimental',
                           'Phys_Internal_Base_Utility',
                           'Phys_Internal_Base_ValOnly',
                           'Phys_Internal_Connect',
                           'Phys_Internal_MBus',
                           'Phys_RAIL_Base_Standard_BLE',
                           'Phys_RAIL_Base_Standard_IEEE802154',
                           'Phys_RAIL_Base_Standard_ZWave',
                           'Phys_Internal_Base_Customer_Signify'
                           ]

    # Studio white list (these PHYs show in Studio as proprietary starting points)
    simplicity_studio_phy_groups = []

    # Special designation for simulation PHYs
    sim_tests_phy_groups = []

    # Special designation for non-functional PHYs
    non_functional_phy_groups = []
