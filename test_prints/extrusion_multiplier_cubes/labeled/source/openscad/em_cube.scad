// the label printed to the part
em_value = "0.921";

text_size = 6.5;
text_font = "comic";
// layer height you are printing the em_cubes
layer_height = 0.2;

// width of the cube
cube_width = 30;
// depth of the cube
cube_depth = 30;
// height of the cube
cube_height = 3;

difference() {
	translate([-(cube_width/2), -(cube_depth/2), 0])
		cube([cube_width, cube_depth, cube_height]);
	translate([0,0,-layer_height])
		linear_extrude(layer_height*2)
			mirror([1,0,0])
				text(em_value, size = text_size, halign = "center", valign = "center");
}