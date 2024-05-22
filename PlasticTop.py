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

ri.Translate(0, 2, 8)
ri.TransformBegin()


ri.Bxdf("PxrDisneyBsdf","Plastic",
{
	"int transmissionBehavior" : [0],
	"float presence" : [1],
	"normal bumpNormal" : [0,0,0],
	"int shadowBumpTerminator" : [1],
	"int inputAOV" : [0],
	"color baseColor" : [0,0,.8],
	"color emitColor" : [0,0,0],
	"float metallic" : [0],
	"float specularTint" : [0],
	"float roughness" : [.25],
	"float anisotropic" : [0],
	"float ior" : [1.5],
	"float specReflectScale" : [1.0],
	"float clearcoat" : [0],
	"float clearcoatGloss" : [1],
	"float sheen" : [0],
	"float sheenTint" : [.5],
	"float diffTrans" : [0],
	"float specTrans" : [0],
	"int isThin" : [0],
	"color transColor" : [0,0,1],
	"float transDistance" : [1],
	"float subsurface" : [0],
	"color subsurfaceColor" : [0,0,0],
	"color scatterDistances" : [1,1,1],
	"float g" : [0],
})

ri.Rotate(45, 1, 0, 0)
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
