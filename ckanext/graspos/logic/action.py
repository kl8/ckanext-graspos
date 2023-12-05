import ckan.plugins.toolkit as tk
import ckanext.graspos.logic.schema as schema


@tk.side_effect_free
def graspos_get_sum(context, data_dict):
    tk.check_access(
        "graspos_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.graspos_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'graspos_get_sum': graspos_get_sum,
    }
