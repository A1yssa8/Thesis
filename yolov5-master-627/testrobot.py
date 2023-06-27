import subprocess
import json

file_path = 'D:\\thesis\yolov5-master\detect_label_single.py'
source = 'D:\\thesis\yolov5-master\\test-image\\test-different-type\\test2.jpg'

arguments = ["--source", source,'--save-txt']

completed_process1 = subprocess.run(["python", file_path] + arguments, capture_output=True, text=True)

output = completed_process1.stdout.split('\n')
class_dict1 = output[0] 
bbox_dict1 = output[1]
class_dict = json.loads(class_dict1) 
bbox_dict = json.loads(bbox_dict1)

print(bbox_dict)

def find_key_value_by_keyword(dictionary, keyword):
    key_value_dict = {key: value for key, value in dictionary.items() if keyword in key and value}
    return key_value_dict

tips = find_key_value_by_keyword(bbox_dict, 'tip')
tips = list(tips.values())
tmp = list()
for tip in tips[0]:
    tmp.append(tip['bbox'])
print(tmp)


print('1')
def detect_level(threshold, bbox_dict):
# 搜索检测框
    tips = matching_keys = find_key_by_keyword(temp, 'tip')
         
# #             # 初始化距离和匹配液体
#              min_distance = float('inf')
#              matched_liquid = None

#              for liquid_type in ['blue liquid', 'red liquid', 'transparent liquid']:
                 
#                 for _, liquid_bbox in liquid_detections.iterrows():
#                     # 计算x坐标距离
#                     distance = abs((tube_bbox['xmin'] + tube_bbox['xmax']) / 2 - (liquid_bbox['xmin'] + liquid_bbox['xmax']) / 2)
                    
#                     # 更新匹配液体
#                     if distance < min_distance:
#                         min_distance = distance
#                         matched_liquid = liquid_bbox
            
#             # 计算高度
#             if matched_liquid is not None:
#                 liquid_level = (tube_bbox['ymax'] - matched_liquid['ymin']) / (tube_bbox['ymax'] - tube_bbox['ymin'])
#                 # 预警
#                 if liquid_level < threshold:
#                     print(f'Warning: Liquid level in {tube_type} is below the threshold! Current level: {liquid_level}')



# # # 去除首尾的大括号并分割成键值对
# # output_dict = dict(item.split(': ') for item in output[1:-1].split(', '))
# def detect_tip(output_dict):
# # # 遍历字典中的键值对
#     has_tip_in_key = False
#     has_full_tips = False
#     for key, value in output_dict.items():
#         if 'tip' in key and value != 8:
#             #p300.pause("error")
#             # 添加终止程序的逻辑
#             print(f"tip: {key}, value: {value}", 'not 8')
#             has_tip_in_key = True
#         if 'tip' in key and value == 8:
#             print(f"tip: {key}, value: {value}")
#             has_tip_in_key = True
#             has_full_tips = True
#     if not has_tip_in_key:
#         # 如果所有键中都没有 'tip'，输出特定的消息
#         print("no tips")
#     return has_full_tips
    
# # output_dict1 = output_decode(completed_process1)
# has_full_tips = detect_tip(class_dict)

# if has_full_tips:
#         completed_process = subprocess.run(["python", file_path] + arguments, capture_output=True, text=True)
        
#         for key, value in class_dict.items():
#             if 'liquid' in key :
#                 print(f"liquid: {key}, value: {value}")

