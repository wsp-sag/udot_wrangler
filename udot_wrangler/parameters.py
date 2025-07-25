import os
from cube_wrangler.logger import WranglerLogger
from cube_wrangler import Parameters


def get_base_dir(udot_wrangler_base_dir=os.getcwd()):
    d = udot_wrangler_base_dir
    for i in range(3):
        if ".settings" in os.listdir(d):
            WranglerLogger.info("udot Wrangler base directory set as: {}".format(d))
            return d
        d = os.path.dirname(d)

    msg = "Cannot find UDOT Wrangler base directory from {}, please input using keyword in parameters: `udot_wrangler_base_dir =` ".format(
        udot_wrangler_base_dir
    )
    WranglerLogger.error(msg)
    raise (ValueError(msg))


class UDOT_Parameters(Parameters):
    """A class representing all the parameters defining the model networks.

    Parameters can be set at runtime by initializing a parameters instance
    with a keyword argument setting the attribute.  Parameters that are
    not explicitly set will use default parameters listed in this class.
    .. highlight:: python
    ##TODO potentially split this between several classes.

    Attr:
    """

    def __init__(self, **kwargs):
        """
        constructor for the Parameters class
        """
        super().__init__(**kwargs)

        if "categories" in kwargs:
            self.categories = kwargs.get("categories")
        else:
            self.categories = {
                # suffix, source (in order of search)
                "sov": ["sov", "default"],
                "hov2": ["hov2", "default", "sov"],
                "hov3": ["hov3", "hov2", "default", "sov"],
                "truck": ["trk", "sov", "default"],
            }
            self.categories = {
                # suffix, source (in order of search)
                "sov": "sov",
                "hov2": "hov2",
                "hov3": "hov3",
                "truck": "trk",
            }

        # prefix, source variable, categories
        self.properties_to_split = {}

        if "udot_wrangler_base_dir" in kwargs:
            self.base_dir = get_base_dir(
                udot_wrangler_base_dir=kwargs.get("udot_wrangler_base_dir")
            )
        else:
            self.base_dir = get_base_dir()

        if "data_file_location" in kwargs:
            self.data_file_location = kwargs.get("data_file_location")
        else:
            self.data_file_location = os.path.join(self.base_dir, "udot_data")

        if "settings_location" in kwargs:
            self.settings_location = kwargs.get("settings_location")
        else:
            self.settings_location = os.path.join(self.base_dir, ".settings")

        if "scratch_location" in kwargs:
            self.scratch_location = kwargs.get("scratch_location")
        else:
            self.scratch_location = os.path.join(self.base_dir, "tests", "scratch")

        if "no_model_link_id_in_cube" in kwargs:
            self.no_model_link_id_in_cube = kwargs.get("no_model_link_id_in_cube")
        else:
            self.no_model_link_id_in_cube = True

        if "no_lanes_in_cube" in kwargs:
            self.no_lanes_in_cube = kwargs.get("no_lanes_in_cube")
        else:
            self.no_lanes_in_cube = True

        if "no_drive_access_in_cube" in kwargs:
            self.no_drive_access_in_cube = kwargs.get("no_drive_access_in_cube")
        else:
            self.no_drive_access_in_cube = True

        if "no_walk_access_in_cube" in kwargs:
            self.no_walk_access_in_cube = kwargs.get("no_walk_access_in_cube")
        else:
            self.no_walk_access_in_cube = True

        if "no_bike_access_in_cube" in kwargs:
            self.no_bike_access_in_cube = kwargs.get("no_bike_access_in_cube")
        else:
            self.no_bike_access_in_cube = True

        if "no_name_in_cube" in kwargs:
            self.no_name_in_cube = kwargs.get("no_name_in_cube")
        else:
            self.no_name_in_cube = True

        self.net_to_dbf_crosswalk = os.path.join(
            self.settings_location, "net_to_dbf.csv"
        )

        self.log_to_net_crosswalk = os.path.join(
            self.settings_location, "log_to_net.csv"
        )

        self.output_variables = [
            "model_link_id",
            "A",
            "B",
            "DISTANCE",
            "STREET",
            "ONEWAY",
            "LINKID",
            "TAZID",
            "PATHGRP",
            "TRK_RSTRCT",
            "DISTEXCEPT",
            "RAILSPD",
            "HOV_LYEAR",
            "LN_2015",
            "LN_2019",
            "TRN_2015",
            "TRN_2019",
            "FT_2015",
            "FT_2019",
            "FT_P4_EOP3",
            "SFAC",
            "CFAC",
            "SCREN_SML",
            "SCREN_MED",
            "SCREN_LRG",
            "SCREN_MPO",
            "JEFF_EDIT",
            "UDOT_FC",
            "UDOTFCCODE",
            "UDOT_AT",
            "TYPE",
            "PROJFLAG",
            "PROJ_ID_N",
            "GEOMETRYSO",
            "GEOMETRY_1",
            "SEGID",
            "TRNSFSRC",
            "JOINDIST",
            "NEW",
            "USE",
            "REMOVE",
            "SHAPE_LENG",
            "GEOMETRY_2",
            "GEOMETRY_3",
            "SHAPE_LE_1",
            "LN23_2028",
            "TRN23_2028",
            "FT23_2028",
            "PASSLANE",
            "SELGRP",
            "LN23_2032",
            "LN23_2042",
            "LN23_2050",
            "LN23_2032UF",
            "LN23_2042UF",
            "LN23_2050UF",
            "TL23_2032",
            "TL23_2042",
            "TL23_2050",
            "TL23_2032UF",
            "TL23_2042UF",
            "TL23_2050UF",
            "PL23_2032",
            "PL23_2042",
            "PL23_2050",
            "PL23_2032UF",
            "PL23_2042UF",
            "PL23_2050UF",
            "FT23_2032",
            "FT23_2042",
            "FT23_2050",
            "FT23_2032UF",
            "FT23_2042UF",
            "FT23_2050UF",
            "LN_2023",
            "FT_2023",
            "TRN_2023",
            "PL_2023",
            "LN_TMP",
            "TRN_TMP",
            "FT_TMP",
            "PL_TMP",
            "PROJECT_NUMBER",
            "model_node_id",
            "X",
            "Y",
            "EXTERNAL",
            "PNR_2015",
            "PNR_2019",
            "PNR_2024",
            "PNR_2030",
            "PNR_2040",
            "PNR_2050",
            "PNR_2030UF",
            "PNR_2040UF",
            "PNR_2050UF",
            "PROJ",
        ]

        self.output_link_shp = os.path.join(self.scratch_location, "links.shp")
        self.output_node_shp = os.path.join(self.scratch_location, "nodes.shp")
        self.output_link_csv = os.path.join(self.scratch_location, "links.csv")
        self.output_node_csv = os.path.join(self.scratch_location, "nodes.csv")
        self.output_link_txt = os.path.join(self.scratch_location, "links.txt")
        self.output_node_txt = os.path.join(self.scratch_location, "nodes.txt")
        self.output_link_header_width_txt = os.path.join(
            self.scratch_location, "links_header_width.txt"
        )
        self.output_node_header_width_txt = os.path.join(
            self.scratch_location, "nodes_header_width.txt"
        )
        self.output_cube_network_script = os.path.join(
            self.scratch_location, "make_complete_network_from_fixed_width_file.s"
        )
        self.output_dir = os.path.join(self.scratch_location)
        self.output_epsg = 26912
        self.wrangler_epsg = 4269

        self.zones = 952

        self.bool_col = [
            "rail_only",
            "bus_only",
            "drive_access",
            "bike_access",
            "walk_access",
            "truck_access",
        ]

        self.int_col = [
            "model_link_id",
            "model_node_id",
            "A",
            "B",
            "lanes",
            "drive_access",
            "walk_access",
            "bike_access",
            "truck_access",
        ]

        self.float_col = ["distance", "X", "Y"]

        self.string_col = [
            "name",
            "roadway",
            "LINKID",
            "STREET",
            "UDOT_FC",
            "UDOT_AT",
            "TYPE",
            "SEGID",
            "TRNSFSRC",
            "PROJECT_NUMBER",
        ]

        self.__dict__.update(kwargs)
