import re

def validate_property_key(prop_key) :
    tmp_reg = re.compile('matrix_\d+_\d+')
    result = tmp_reg.findall(prop_key)
    return len(result) > 0

def fetch_property_index(prop_key) :
    tmp_reg = re.compile('matrix_(\d+)_(\d+)')
    result = tmp_reg.match(prop_key)

    if result :
        return {
            'r' : int(result.group(1)), 'c' : int(result.group(2))
        }
    else :
        return None

class SparseMatrix :
    def __init__(self, obj={}) :
        self.obj = obj

    def assign_value(self, idx, value) :
        if validate_property_key(idx) :
            tmp_obj = self.obj
            tmp_obj[idx] = value
            self.obj = tmp_obj

    def remove_value(self, idx) :
        if validate_property_key(idx) :
            tmp_obj = self.obj
            
            if idx in tmp_obj :
                del tmp_obj[idx]

    def fetch_matrix_size(self) :
        max_row = 0
        max_col = 0
        
        tmp_obj = self.obj

        for k in tmp_obj.keys() :
            tmp_idx = fetch_property_index(k)
            
            if tmp_idx is not None :
                max_row = max(max_row, tmp_idx['r'])
                max_col = max(max_col, tmp_idx['c'])

        return {
            'r' : max_row + 1, 'c' : max_col + 1
        }

    def sort_by_idx_and_unit(self, idx, unit) :
        if type(idx) == int and unit in ('ROW', 'COL', ) :
            print(idx)
            print(unit)
            tmp_obj = self.obj
            mat_size = self.fetch_matrix_size()

            if unit == 'ROW' :
                tmp_reg = re.compile('matrix_{}_\d+'.format(idx))
            
            if unit == 'COL' :
                tmp_reg = re.compile('matrix_\d+_{}'.format(idx))
 
    def __str__(self) :
        tmp_obj = self.obj
        mat_size = self.fetch_matrix_size()

        tmp_str = ''
        for k in range(0, mat_size['r']) :
            for l in range(0, mat_size['c']) :
                tmp_idx = 'matrix_{}_{}'.format(k, l)
                
                if tmp_idx in tmp_obj :
                    tmp_str += '{} '.format(tmp_obj[tmp_idx])
                else :
                    tmp_str += '- '

            if k != mat_size['r'] - 1 :
                tmp_str += '\n'

        return tmp_str


sparse_matrix_1 = SparseMatrix()

sparse_matrix_1.assign_value('matrix_0_0', 10)
sparse_matrix_1.assign_value('matrix_0_1', 30)
sparse_matrix_1.assign_value('matrix_1_1', 10)
sparse_matrix_1.assign_value('matrix_2_1', 20)
sparse_matrix_1.assign_value('matrix_3_1', 30)
sparse_matrix_1.assign_value('matrix_4_1', 40)

print(sparse_matrix_1.fetch_matrix_size()) # {'r': 5, 'c': 2}
print(sparse_matrix_1) 

# 10 30
# - 10
# - 20
# - 30
# - 40

sparse_matrix_1.assign_value('matrix_3_1', 4)
sparse_matrix_1.assign_value('matrix_4_1', 21)
print(sparse_matrix_1)

# 10 30
# - 10
# - 20
# - 4
# - 21

sparse_matrix_1.assign_value('matrix_3_2', 51)
sparse_matrix_1.assign_value('matrix_1_2', 41)
sparse_matrix_1.assign_value('matrix_0_2', 31)
print(sparse_matrix_1.fetch_matrix_size()) # {'r': 5, 'c': 3}
print(sparse_matrix_1)

# 10 30 31
# - 10 41
# - 20 -
# - 4 51
# - 21 -

sparse_matrix_1.remove_value('matrix_3_2')
print(sparse_matrix_1)

# 10 30 31
# - 10 41
# - 20 -
# - 4 -
# - 21 -

sparse_matrix_1.sort_by_idx_and_unit(1, 'COL')