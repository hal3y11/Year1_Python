import math

paint_coverage = 5.1
can_diameter = 0.15
can_height = 0.30
box_dimensions = (0.60, 0.30, 0.35)
hall_length = 40
hall_width = 30
ceiling_height = 3.4

total_wall_area = 2 * (hall_length + hall_width) * ceiling_height
num_cans_required = math.ceil(total_wall_area / paint_coverage)
cans_per_box = math.floor(box_dimensions[0] / can_diameter) * math.floor(box_dimensions[1] / can_diameter) * math.floor(box_dimensions[2] / can_height)
num_full_boxes = math.floor(num_cans_required / cans_per_box)
cans_not_packed = num_cans_required % cans_per_box

print("Number of cans required:", num_cans_required)
print("Number of cans in a box:", cans_per_box)
print("Number of full boxes:", num_full_boxes)
print("Cans not packed in boxes:", cans_not_packed)