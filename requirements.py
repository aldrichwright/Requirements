	

# Define the pages of the app:
import hyperdiv as hd
from mainroute import *
import globalstate




router = mainrouter


def main():
    template = hd.template(title="Requirements")


    # Sidebar menu linking to the app's pages:
    # 	


    with template.sidebar:
        if globalstate.globalstate().getCategory() =="Empty":
            hd.navigation_menu({
            "Login": {"icon": "stop-circle", "href": "/login"},
            })
        else:
            if globalstate.globalstate().getCategory() =="admin":
                hd.navigation_menu({
                    "Login": {"icon": "stop-circle", "href": "/login"},
                    "User": {"icon": "person", "href": "/UserEntry"},
                    "User Category": {"icon": "person", "href": "/reqUserCat"},
                    "Category": {"icon": "list-ol", "href": "/reqCat"},
                    "Priority": {"icon": "list-ul", "href": "/reqPrior"},
                    "Initiative": {"icon": "list-check", "href": "/reqInit"},
                    "Risk": {"icon": "list", "href": "/reqRisk"},

            })
            else:
                if globalstate.globalstate().getCategory() =="user":
                    hd.navigation_menu({
                    "Login": {"icon": "stop-circle", "href": "/login"},
                    "Requirements": {"icon": "file-earmark-text", "href": "/reqEntry"},
                    "Reports": {
                        "Report by Category": {"href": "/repChartTableCat", "icon": "layout-text-window"},
                        "Report by Priority": {"href": "/repChartTablePrior", "icon": "layout-text-window"},
                        "Report by Initiative": {"href": "/repChartTableInit", "icon": "layout-text-window"},
                        "Report by Risk": {"href": "/repChartTableRisk", "icon": "layout-text-window"},
                        "Report by Request By": {"href": "/repChartTableBy", "icon": "layout-text-window"},
                        },
            })
                else:    
                    hd.navigation_menu({
                    "Login": {"icon": "stop-circle", "href": "/login"},
                    "Reports": {
                        "Report by Category": {"href": "/repChartTableCat", "icon": "layout-text-window"},
                        "Report by Priority": {"href": "/repChartTablePrior", "icon": "layout-text-window"},
                        "Report by Initiative": {"href": "/repChartTableRisk", "icon": "layout-text-window"},
                        "Report by Risk": {"href": "/repChartTableRisk", "icon": "layout-text-window"},
                        "Report by Request By": {"href": "/repChartTableBy", "icon": "layout-text-window"},
                        },
            }

)


	
	
    # A topbar contact link:
    template.add_topbar_links(
	{"Contact": {"icon": "envelope", "href": "mailto:aldrichwright@hotmail.com"}
	},

    ),

    # Render the active page in the body:
    with template.body:
        router.run()
hd.run(main, index_page=hd.index_page(title="Requirement"))
