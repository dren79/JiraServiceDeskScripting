import json

from helpers import get_all_request_types, get_all_servicedesks


def main():
    my_instance = {}

    service_desks = get_all_servicedesks()
    my_instance['service_desks'] = {}
    for desk in service_desks['values']:
        desk_id = desk['id']
        my_instance['service_desks'][f'{desk_id}'] = desk['projectName']
        my_instance['service_desks'][f'{desk["projectName"]}'] = desk_id

    request_types = get_all_request_types()
    my_instance['request_types'] = {}
    for type_ in request_types.get('values', 'No_types_returned'):
        s_desk_no = type_['serviceDeskId']
        if my_instance['request_types'].get(f'{s_desk_no}', None) is None:
            my_instance['request_types'][f'{s_desk_no}'] = {}
        name = type_.get('name', 'no_name')
        my_instance['request_types'][f'{s_desk_no}'][f'{name}'] = type_.get('id', 'no_id')

    return my_instance


if __name__ == "__main__":
    my_instance_details = main()
    with open(f'output/my_service_instance_details.json', 'w') as outfile:
        json.dump(my_instance_details, outfile)