#!/usr/bin/env python
import prman
import sys
import sys, os.path, subprocess
import argparse

# def main(
#     shadingrate=10,
#     pixelvar=0.1,
#     fov=48.0,
#     width=1024,
#     height=720,
#     integrator="PxrPathTracer",
#     integratorParams={},
# ):
ri = prman.Ri()  # create an instance of the RenderMan interface
ri.Option("rib", {"string asciistyle": "indented"})
filename = "PlasticTop.rib"
ri.Begin("__render")
ri.Option("searchpath", {"string texture": "./textures/:@"})

ri.Display("PlasticTop.exr", "it", "rgba")
ri.Format(2048, 1440, 1)


ri.Hider("raytrace", {"int incremental": [1]})
ri.ShadingRate(10)
ri.PixelVariance(0.05)
ri.Integrator('PxrPathTracer', "integrator", {})
# # now set the projection to perspective
ri.Projection(ri.PERSPECTIVE, {ri.FOV: 48})



# now we start our world
ri.WorldBegin()
ri.Translate(0, 2, 8)
ri.AttributeBegin()
ri.TransformBegin()
ri.Declare("domeLight", "string")
ri.Rotate(-90, 1, 0, 0)
ri.Rotate(100, 0, 0, 1)
ri.Attribute("visibility", {"int camera": [0]})
ri.Light("PxrDomeLight", "domeLight", {"string lightColorMap": "Luxo-Jr_4000x2000.tex"})
ri.TransformEnd()
ri.AttributeEnd()



ri.AttributeBegin()


ri.Pattern("turbulance", "diskTx", {})
ri.Attribute("displacementbound", {
    "sphere" : [0.1],
    "coordinatesystem" : ["shader"],
})
ri.Displace("PxrDisplace", "myDisp",
{
    "float dispAmount" : [ 0.011 ],  
	"reference float dispScalar" : [ "diskTx:mag" ],
    })
ri.Bxdf("PxrDisneyBsdf","scratches",
{
    "int transmissionBehavior" : [0],
    "float presence" : [1],
    "normal bumpNormal" : [0,0,0],
    "int shadowBumpTerminator" : [1],
    "int inputAOV" : [0],
    "color baseColor" : [0,0,.8],
    "color emitColor" : [0,0,0],
    "float metallic" : [.2],
    "float roughness" : [0.3],
    "float anisotropic" : [0.5],
    "float ior" : [1.5],
    "float specReflectScale" : [1.0],
    "float clearcoat" : [0],
    "float clearcoatGloss" : [1],
    "float sheen" : [0],
    "float sheenTint" : [.5],
    "float diffTrans" : [0],
    "float specTrans" : [0],
    "int isThin" : [0],
    "color transColor" : [0,0,0],
    "float transDistance" : [1],
    "float subsurface" : [0],
    "color subsurfaceColor" : [0.4,0,0],
    "color scatterDistances" : [1,1,1],
    "float g" : [0],
})

ri.TransformBegin()
ri.Rotate(65, 1, 0, 0)
ri.Cylinder(1, 0, 1.3 , 360)

ri.Torus(0.8, 0.2, 270, 360, 360)
ri.TransformBegin()
ri.Translate(0,0,-1.2)
ri.Disk(0.999,0.8,360)
ri.TransformEnd()

ri.TransformEnd()
ri.AttributeEnd()




ri.AttributeBegin()
# ri.Pattern("Scratches", "Scratches", {})

ri.Pattern("turbs", "silverturb", {})
ri.Attribute("displacementbound", {
    "sphere" : [0.1],
    "coordinatesystem" : ["shader"],
})
ri.Displace("PxrDisplace", "myDisp",
{
    "float dispAmount" : [ 0.003 ],  
	"reference float dispScalar" : [ "silverturb:mag" ],
    })
ri.Pattern("turb", "whitespots", {})
ri.Bxdf("PxrDisneyBsdf","Silver",
{
    "int transmissionBehavior" : [0],
    "float presence" : [1],
    "normal bumpNormal" : [0,0,0],
    "int shadowBumpTerminator" : [1],
    "int inputAOV" : [0],
    "color baseColor" : [1,1,1],
    "color emitColor" : [0,0,0],
    "float metallic" : [1],
    "float roughness" : [.3],
    "float anisotropic" : [0.5],
    "float ior" : [2],
    "float specReflectScale" : [0.8],
    "float clearcoatGloss" : [0.5],
    "float sheen" : [0],
    "float sheenTint" : [.5],
    "float diffTrans" : [0.5],
    "int isThin" : [0],
    "color transColor" : [0,0,1],
    "float transDistance" : [1],
    "reference float subsurface" : "whitespots:mag",
    "color subsurfaceColor" :  [ 1, 1, 1 ],
    "color scatterDistances" : [1,1,1],
    "float g" : [0],
})
ri.TransformBegin()
ri.Rotate(65, 1, 0, 0)
ri.Translate(0,0,1.33)
ri.Cylinder(1, 0, 3.1 , 360)
ri.Torus(0.85, 0.15, 90, 180, 360)
ri.TransformBegin()
ri.Translate(0,0,-1.15)
ri.Disk(1,0.85,360)
ri.TransformEnd()

ri.TransformEnd()

ri.TransformBegin()
ri.Rotate(65, 1, 0, 0)
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
ri.AttributeEnd()

ri.WorldEnd()
# and finally end the rib file
ri.End()
