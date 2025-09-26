import ckan.plugins.toolkit as tk
import ckanext.deliserdang.logic.schema as schema


@tk.side_effect_free
def deliserdang_get_sum(context, data_dict):
    tk.check_access(
        "deliserdang_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.deliserdang_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'deliserdang_get_sum': deliserdang_get_sum,
    }
