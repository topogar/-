import pytest
import requests
import json

class Tester:

    def __init__(self, host, page, tmp_data):
        self.url = host + page
        self.created_objects_ids = []
        self.tmp_data = tmp_data
        self.headers = {'Content-Type': 'application/json', }
        self.id = 200
        self.name = page

    
    def find_obj_by_id(self, id):
        return json.loads(requests.request("GET", self.url + "?id={}".format(id)).content)

    def find_obj_by_name(self, name):
        return json.loads(requests.request("GET", self.url + "?name[$like]={}".format(name)).content)

    def create_obj(self, name):
        if self.name == 'categories':
            self.tmp_data['id'] = str(self.id)
            self.id += 1

        data = self.tmp_data
        data['name'] = name
        response = requests.request("POST", 
                                    self.url,
                                    headers=self.headers, 
                                    data=json.dumps(data))
        print(response.json())
        self.created_objects_ids.append(json.loads(response.content)['id'])
        return json.loads(response.content)


    def delete_obj_by_id(self, id):
        requests.request("DELETE", self.url + '?id={}'.format(id))

    def delete_all_obj(self):
        for id in self.created_objects_ids:
            self.delete_obj_by_id(id)
