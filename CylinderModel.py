#!/usr/bin/env python
# import the python renderman library
import prman


ri = prman.Ri()  # create an instance of the RenderMan interface
ri.Option("rib", {"string asciistyle": "indented"})

filename = "Cylinder.rib"
# this is the begining of the rib archive generation we can only
# make RI calls after this function else we get a core dump
ri.Begin("__render")
# now we add the display element using the usual elements
# FILENAME DISPLAY Type Output format
ri.Display("Cylinder.exr", "it", "rgba")
# Specify PAL resolution 1:1 pixel Aspect ratio
ri.Format(720, 576, 1)
# now set the projection to perspective
ri.Projection(ri.PERSPECTIVE, {ri.FOV: 50})


# now we start our world
ri.WorldBegin()

ri.Translate(0, 0, 8)
ri.TransformBegin()

# create a simple checker pattern
expr = """
$colour = c1;
$c = floor( 10 * $u ) +floor( 10 * $v );
if( fmod( $c, 2.0 ) < 1.0 )
{
	$colour=c2;
}
$colour
"""

# use the pattern
ri.Pattern("PxrSeExpr", "seTexture", {"color c1": [1, 1, 1], "color c2": [1, 0, 0], "string expression": [expr]})
ri.Bxdf(
    "PxrDiffuse",
    "diffuse",
    {
        #  'color diffuseColor'  : [1,0,0]
        "reference color diffuseColor": ["seTexture:resultRGB"]
    },
)


ri.Rotate(45, 1, 1, 0)
ri.Cylinder(1, 0, 1.3 , 360)

ri.Torus(0.8, 0.2, 270, 360, 360)
ri.TransformBegin()
ri.Translate(0,0,-1.2)
ri.Disk(1,0.8,360)
ri.TransformEnd()


ri.TransformBegin()
ri.Translate(0,0,1.33)
ri.Cylinder(1, 0, 3.1 , 360)
ri.Torus(0.85, 0.15, 90, 180, 360)
ri.TransformBegin()
ri.Translate(0,0,-1.15)
ri.Disk(1,0.85,360)
ri.TransformEnd()
ri.TransformEnd()

ri.TransformBegin()
ri.Translate(0,0,4.5)
ri.Cylinder(1, 0, 0.05 , 360)
ri.Torus(0.95, 0.05, 270, 360, 360)
ri.TransformBegin()
ri.Translate(0,0,-.95)
ri.Disk(1.05,0.95,360)
ri.TransformEnd()
ri.TransformBegin()
ri.Translate(0,0,0.05)
ri.Torus(0.95, 0.05, 0, 90, 360)
ri.TransformEnd()
ri.TransformEnd()
ri.TransformEnd()

ri.WorldEnd()
# and finally end the rib file
ri.End()
