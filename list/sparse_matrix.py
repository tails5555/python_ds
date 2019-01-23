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
            'ROW' : int(result.group(1)), 'COL' : int(result.group(2))
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
                max_row = max(max_row, tmp_idx['ROW'])
                max_col = max(max_col, tmp_idx['COL'])

        return {
            'ROW' : max_row + 1, 'COL' : max_col + 1
        }

    def sort_by_idx_and_unit(self, idx, unit, oper) :
        if type(idx) == int and unit in ('ROW', 'COL', ) and oper in ('ASC', 'DESC', ) :
            tmp_obj = self.obj
            mat_size = self.fetch_matrix_size()
            pivot_data = []
            pivot_reg = None

            if unit == 'COL' :
                pivot_reg = re.compile('matrix_{}_\d+'.format(idx))

            if unit == 'ROW' :
                pivot_reg = re.compile('matrix_\d+_{}'.format(idx))
            
            for k in tmp_obj.keys() :
                res = pivot_reg.match(k)
                if res :
                    if res.group(0) == k :
                        idx = fetch_property_index(k)
                        pivot_data.append({
                            'key' : idx[unit], 'data' : tmp_obj[k]
                        })

            if len(pivot_data) != mat_size[unit] :
                return

            new_mat = {}
            pivot_data.sort(key = lambda obj : obj['data'], reverse = True if oper == 'DESC' else False)
            for seq, pivot in enumerate(pivot_data) :
                data_reg = None
                if unit == 'COL' :
                    data_reg = re.compile('matrix_\d+_{}'.format(pivot['key']))

                if unit == 'ROW' :
                    data_reg = re.compile('matrix_{}_\d+'.format(pivot['key']))

                for k in tmp_obj.keys() :
                    res = data_reg.match(k)
                    if res :
                        if res.group(0) == k :
                            cur_idx = fetch_property_index(k)
                            assign_idx = ''

                            if unit == 'ROW' :
                                assign_idx = 'matrix_{}_{}'.format(seq, cur_idx['COL'])

                            if unit == 'COL' :
                                assign_idx = 'matrix_{}_{}'.format(cur_idx['ROW'], seq)

                            new_mat[assign_idx] = tmp_obj[k]

            self.obj = new_mat

    def __str__(self) :
        tmp_obj = self.obj
        mat_size = self.fetch_matrix_size()

        tmp_str = ''
        for k in range(0, mat_size['ROW']) :
            for l in range(0, mat_size['COL']) :
                tmp_idx = 'matrix_{}_{}'.format(k, l)
                
                if tmp_idx in tmp_obj :
                    tmp_str += '{} '.format(tmp_obj[tmp_idx])
                else :
                    tmp_str += '- '

            if k != mat_size['ROW'] - 1 :
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

sparse_matrix_1.assign_value('matrix_1_0', 90)
sparse_matrix_1.assign_value('matrix_3_2', 3)
print(sparse_matrix_1)

# 10 30 31 
# 90 10 41
# - 20 -
# - 4 3
# - 21 - 

sparse_matrix_1.sort_by_idx_and_unit(1, 'COL', 'ASC')
print(sparse_matrix_1)

# 30 31 10
# 10 41 90
# 20 - -
# 4 3 -
# 21 - -

sparse_matrix_1.sort_by_idx_and_unit(0, 'ROW', 'ASC')
print(sparse_matrix_1)

# 4 3 -
# 10 41 90
# 20 - -
# 21 - -
# 30 31 10