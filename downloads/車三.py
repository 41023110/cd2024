# NX 1872
# Journal created by Admin on Thu Jun 20 17:33:36 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "New Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "ModelTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "Model"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "C:\\Users\\Admin\\Desktop\\機器人組裝\model1.pr\\model1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    # User Function call - UF_PART_ask_part_name
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId4, "Create Sketch Dialog")
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) Y axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) YZ plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = datumPlane1
    plane2.SetGeometry(geom1)
    
    plane2.SetFlip(False)
    
    plane2.SetExpression(None)
    
    plane2.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane2.Evaluate()
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane3.SynchronizeToPlane(plane2)
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = datumPlane1
    plane3.SetGeometry(geom2)
    
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane3.Evaluate()
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject2 = sketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject2
    feature1 = sketch1.Feature
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "Create Sketch")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression4)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression3)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane3.DestroyPlane()
    
    scaleAboutPoint1 = NXOpen.Point3d(23.009045977284433, 2.3599021515163687, 0.0)
    viewCenter1 = NXOpen.Point3d(-23.009045977284433, -2.3599021515163687, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(18.407236781827546, 1.887921721213095, 0.0)
    viewCenter2 = NXOpen.Point3d(-18.407236781827546, -1.887921721213095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(14.725789425462036, 1.510337376970476, 0.0)
    viewCenter3 = NXOpen.Point3d(-14.725789425462036, -1.510337376970476, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(11.780631540369644, 1.2082699015763809, 0.0)
    viewCenter4 = NXOpen.Point3d(-11.780631540369644, -1.2082699015763809, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(14.725789425462036, 1.510337376970476, 0.0)
    viewCenter5 = NXOpen.Point3d(-14.725789425462004, -1.510337376970476, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(18.407236781827589, 1.8879217212130954, 0.0)
    viewCenter6 = NXOpen.Point3d(-18.40723678182755, -1.8879217212130954, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Rectangle...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId9, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint1 = NXOpen.Point3d(0.0, -78.0, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(0.0, -78.0, 0.0)
    endPoint2 = NXOpen.Point3d(0.0, -78.0, 7.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(0.0, -78.0, 7.0)
    endPoint3 = NXOpen.Point3d(0.0, 0.0, 7.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(0.0, 0.0, 7.0)
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = line3
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom3.Geometry = line1
    geom3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom3)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point2 = datumCsys2.FindObject("POINT 1")
    geom2_5.Geometry = point2
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(0.0, -39.0, 10.034229620620708)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression5 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(0.0, -67.965770379379293, 3.5)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression6 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines5 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines8)
    
    theSession.SetUndoMarkName(markId10, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits1 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits2 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits3 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits4 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits5 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits6 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits7 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits8 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits9 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits10 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits11 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits12 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits13 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits14 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits15 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits16 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits17 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits18 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits19 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits20 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    point1_1 = NXOpen.Point3d(0.0, -78.0, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point3 = NXOpen.Point3d(0.0, -72.566991159127838, 7.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(line3, workPart.ModelingViews.WorkView, point3)
    
    point1_2 = NXOpen.Point3d(0.0, -72.566991159127838, 7.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line3, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    point1_3 = NXOpen.Point3d(0.0, -78.0, 0.0)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    dimensionlinearunits21 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits23 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin1 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin1.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin1.View = NXOpen.View.Null
    assocOrigin1.ViewOfGeometry = workPart.ModelingViews.WorkView
    point4 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point4
    assocOrigin1.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.DimensionLine = 0
    assocOrigin1.AssociatedView = NXOpen.View.Null
    assocOrigin1.AssociatedPoint = NXOpen.Point.Null
    assocOrigin1.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.XOffsetFactor = 0.0
    assocOrigin1.YOffsetFactor = 0.0
    assocOrigin1.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin1)
    
    point5 = NXOpen.Point3d(0.0, -105.0156457424777, 4.1298287651536327)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = True
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId11, None)
    
    theSession.SetUndoMarkName(markId10, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId10, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines9 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines12)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId12, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits27 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits37 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits39 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits41 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits45 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    expression7 = workPart.Expressions.FindObject("p0")
    expression7.SetFormula("0.6")
    
    theSession.SetUndoMarkVisibility(markId12, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.085714285714285715)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId12, "Edit Driving Value")
    
    scaleAboutPoint7 = NXOpen.Point3d(-31.563691276531202, -4.1298287651536079, 0.0)
    viewCenter7 = NXOpen.Point3d(31.56369127653123, 4.1298287651536079, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(-14.867383554552958, -2.3599021515163385, 0.0)
    viewCenter8 = NXOpen.Point3d(14.867383554553058, 2.3599021515163385, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-11.516322499399756, -1.887921721213071, 0.0)
    viewCenter9 = NXOpen.Point3d(11.516322499399852, 1.887921721213071, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-9.2130579995197799, -1.5103373769704698, 0.0)
    viewCenter10 = NXOpen.Point3d(9.2130579995198953, 1.5103373769704569, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-7.3704463996158349, -1.2082699015763658, 0.0)
    viewCenter11 = NXOpen.Point3d(7.3704463996159175, 1.2082699015763554, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-4.1564484614226842, 1.063277513387197, 0.0)
    viewCenter12 = NXOpen.Point3d(4.1564484614227579, -1.0632775133872301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-3.3251587691381408, 0.85062201070975763, 0.0)
    viewCenter13 = NXOpen.Point3d(3.3251587691382332, -0.8506220107097906, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-2.6601270153105072, 0.68049760856780617, 0.0)
    viewCenter14 = NXOpen.Point3d(2.6601270153105814, -0.68049760856783259, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-2.1281016122484022, 0.54439808685424096, 0.0)
    viewCenter15 = NXOpen.Point3d(2.1281016122484697, -0.54439808685426627, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(21.498775357226087, 2.0192219948775714, 0.0)
    viewCenter16 = NXOpen.Point3d(-21.498775357226013, -2.0192219948776016, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(17.199020285780868, 1.6153775959020513, 0.0)
    viewCenter17 = NXOpen.Point3d(-17.199020285780804, -1.6153775959020811, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(13.759216228624702, 1.2923020767216389, 0.0)
    viewCenter18 = NXOpen.Point3d(-13.759216228624636, -1.2923020767216671, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(11.007372982899771, 1.0338416613773094, 0.0)
    viewCenter19 = NXOpen.Point3d(-11.007372982899705, -1.0338416613773371, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(8.3356017874187636, 0.79463908090177227, 0.0)
    viewCenter20 = NXOpen.Point3d(-8.3356017874186996, -0.79463908090180135, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(6.6295603320949299, 0.63571126472141459, 0.0)
    viewCenter21 = NXOpen.Point3d(-6.6295603320948659, -0.63571126472144335, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    point6 = NXOpen.Point3d(0.0, -2.9508501318938571, 0.59999999999999998)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line3, workPart.ModelingViews.WorkView, point6)
    
    point1_4 = NXOpen.Point3d(0.0, 0.0, 0.59999999999999998)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    point1_5 = NXOpen.Point3d(0.0, -6.6857142857142859, 0.59999999999999998)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point7 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point7
    assocOrigin2.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.DimensionLine = 0
    assocOrigin2.AssociatedView = NXOpen.View.Null
    assocOrigin2.AssociatedPoint = NXOpen.Point.Null
    assocOrigin2.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.XOffsetFactor = 0.0
    assocOrigin2.YOffsetFactor = 0.0
    assocOrigin2.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder2.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point8 = NXOpen.Point3d(0.0, -2.6187234303251108, 1.5058434656658366)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point8)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = False
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject4 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.SetUndoMarkName(markId14, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId14, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder3 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines13 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines16)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId16, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    expression8 = workPart.Expressions.FindObject("p1")
    expression8.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId16, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId16, "Edit Driving Value")
    
    scaleAboutPoint22 = NXOpen.Point3d(0.30098982329670704, 0.85107467276989868, 0.0)
    viewCenter22 = NXOpen.Point3d(-0.30098982329664509, -0.85107467276992699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(0.3762372791208739, 1.0638433409623766, 0.0)
    viewCenter23 = NXOpen.Point3d(-0.37623727912081417, -1.0638433409624055, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(0.47029659890108538, 1.3298041762029749, 0.0)
    viewCenter24 = NXOpen.Point3d(-0.47029659890102454, -1.329804176203004, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(0.58787074862634969, 1.6622552202537217, 0.0)
    viewCenter25 = NXOpen.Point3d(-0.58787074862628752, -1.6622552202537495, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId18, None)
    
    theSession.DeleteUndoMark(markId18, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    sketch2 = theSession.ActiveSketch
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    scaleAboutPoint26 = NXOpen.Point3d(9.7345963750049513, -5.3097798409117924, 0.0)
    viewCenter26 = NXOpen.Point3d(-9.7345963750049513, 5.3097798409117924, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(7.5516868848523, -4.247823872729434, 0.0)
    viewCenter27 = NXOpen.Point3d(-7.5516868848523, 4.247823872729434, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(3.02067475394092, -1.51033737697046, 0.0)
    viewCenter28 = NXOpen.Point3d(-3.02067475394092, 1.51033737697046, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-2.416539803152749, 1.208269901576368, 0.0)
    viewCenter29 = NXOpen.Point3d(2.4165398031527232, -1.2082699015763809, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-3.5039827145715075, 1.3290968917340165, 0.0)
    viewCenter30 = NXOpen.Point3d(3.5039827145714662, -1.3290968917340269, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(-2.8031861716572064, 1.0632775133872052, 0.0)
    viewCenter31 = NXOpen.Point3d(2.8031861716571735, -1.0632775133872217, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-2.2425489373257785, 0.85062201070976418, 0.0)
    viewCenter32 = NXOpen.Point3d(2.2425489373257257, -0.8506220107097906, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-1.7940391498606227, 0.68049760856780084, 0.0)
    viewCenter33 = NXOpen.Point3d(1.7940391498605806, -0.68049760856782715, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(-1.4352313198884981, 0.54439808685424063, 0.0)
    viewCenter34 = NXOpen.Point3d(1.4352313198884643, -0.54439808685427016, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(-1.1481850559107984, 0.43551846948338913, 0.0)
    viewCenter35 = NXOpen.Point3d(1.1481850559107682, -0.4355184694834161, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-0.91854804472864415, 0.34841477558670586, 0.0)
    viewCenter36 = NXOpen.Point3d(0.91854804472861173, -0.34841477558673828, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-0.7348384357829153, 0.27873182046936035, 0.0)
    viewCenter37 = NXOpen.Point3d(0.73483843578288721, -0.27873182046939277, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(-0.58787074862633226, 0.22298545637548484, 0.0)
    viewCenter38 = NXOpen.Point3d(0.58787074862630806, -0.22298545637551767, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-0.47029659890107128, 0.17838836510038647, 0.0)
    viewCenter39 = NXOpen.Point3d(0.47029659890104364, -0.17838836510041689, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint39, viewCenter39)
    
    # ----------------------------------------------
    #   Menu: Edit->Settings...
    # ----------------------------------------------
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId20, "Sketch Settings Dialog")
    
    scaleAboutPoint40 = NXOpen.Point3d(-6.2403493536940333, -0.49300057264112157, 0.0)
    viewCenter40 = NXOpen.Point3d(6.2403493536940067, 0.49300057264109171, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-7.9788250572179384, -0.82707332910187326, 0.0)
    viewCenter41 = NXOpen.Point3d(7.9788250572179109, 0.8270733291018415, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(-10.520859259898645, -0.75004198962670099, 0.0)
    viewCenter42 = NXOpen.Point3d(10.520859259898623, 0.75004198962666824, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(-8.4166874079189178, -0.60003359170136206, 0.0)
    viewCenter43 = NXOpen.Point3d(8.4166874079188947, 0.6000335917013303, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint43, viewCenter43)
    
    theSession.UndoToMark(markId20, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    theSession.UndoToMarkWithStatus(markId21, None)
    
    theSession.DeleteUndoMarksUpToMark(markId21, None, False)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Suppress...
    # ----------------------------------------------
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Suppress Feature")
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    workPart.Features.SuppressFeatures(features1)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled2, undoUnavailable2 = theSession.UndoLastNVisibleMarks(1)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    horizontalDimension1 = nXObject4
    sketchLinearDimensionBuilder1 = workPart.Sketches.CreateLinearDimensionBuilder(horizontalDimension1)
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Inferred
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId23, "Linear Dimension Dialog")
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits73 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Style.OrdinateStyle.DoglegCreationOption = NXOpen.Annotations.OrdinateDoglegCreationOption.No
    
    dimensionlinearunits75 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits77 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchLinearDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits79 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits83 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits85 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    theSession.DeleteUndoMark(markId24, None)
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionValue.SetFormula("8")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionValue.SetFormula("8")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionMode = NXOpen.Annotations.DrivingValueBuilder.DrivingExpressionMode.KeepExpression
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    nXObject5 = sketchLinearDimensionBuilder1.Commit()
    
    point1_6 = NXOpen.Point3d(0.0, 0.0, 0.59999999999999998)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, NXOpen.View.Null, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    point1_7 = NXOpen.Point3d(0.0, -8.0, 0.59999999999999942)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, NXOpen.View.Null, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    theSession.SetUndoMarkName(markId25, "Linear Dimension - =")
    
    theSession.SetUndoMarkVisibility(markId25, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId23, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    scaleAboutPoint44 = NXOpen.Point3d(-5.5916643896925713, 0.22055288776048063, 0.0)
    viewCenter44 = NXOpen.Point3d(5.5916643896925491, -0.22055288776051271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(-6.9895804871157123, 0.27569110970060362, 0.0)
    viewCenter45 = NXOpen.Point3d(6.9895804871156901, -0.27569110970063676, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(-8.7369756088946335, 0.34461388712575791, 0.0)
    viewCenter46 = NXOpen.Point3d(8.7369756088946158, -0.34461388712579077, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(-10.92121951111829, 0.43076735890720386, 0.0)
    viewCenter47 = NXOpen.Point3d(10.921219511118272, -0.43076735890723628, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(-13.651524388897862, 0.34841477558670564, 0.0)
    viewCenter48 = NXOpen.Point3d(13.651524388897835, -0.34841477558673806, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(-17.064405486122322, 0.43551846948338546, 0.0)
    viewCenter49 = NXOpen.Point3d(17.0644054861223, -0.4355184694834226, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(-21.3305068576529, 0.54439808685423596, 0.0)
    viewCenter50 = NXOpen.Point3d(21.330506857652882, -0.54439808685426971, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(-26.724996991026817, 0.61863418960708294, 0.0)
    viewCenter51 = NXOpen.Point3d(26.724996991026806, -0.61863418960712513, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(-33.406246238783524, 0.69596346330797032, 0.0)
    viewCenter52 = NXOpen.Point3d(33.40624623878351, -0.69596346330801651, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(-41.757807798479398, 0.86995432913496273, 0.0)
    viewCenter53 = NXOpen.Point3d(41.757807798479398, -0.86995432913501214, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-53.405529649675614, 0.84578893110344278, 0.0)
    viewCenter54 = NXOpen.Point3d(53.405529649675614, -0.84578893110348397, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-42.724423719740486, 0.67663114488275411, 0.0)
    viewCenter55 = NXOpen.Point3d(42.724423719740486, -0.6766311448827953, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-34.17953897579239, 0.54130491590619667, 0.0)
    viewCenter56 = NXOpen.Point3d(34.17953897579239, -0.54130491590623619, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(-27.343631180633906, 0.43304393272495728, 0.0)
    viewCenter57 = NXOpen.Point3d(27.343631180633906, -0.43304393272498892, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-21.874904944507126, 0.34643514617996163, 0.0)
    viewCenter58 = NXOpen.Point3d(21.874904944507126, -0.34643514617999538, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-11.917369028591214, 0.55429623388794536, 0.0)
    viewCenter59 = NXOpen.Point3d(11.91736902859121, -0.55429623388798255, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(-9.5338952228729745, 0.44343698711035356, 0.0)
    viewCenter60 = NXOpen.Point3d(9.5338952228729639, -0.44343698711039137, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-7.6271161782983805, 0.35474958968828069, 0.0)
    viewCenter61 = NXOpen.Point3d(7.6271161782983716, -0.35474958968831743, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(-6.1016929426387039, 0.28379967175061938, 0.0)
    viewCenter62 = NXOpen.Point3d(6.1016929426387003, -0.28379967175065562, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    nXObject6 = sketchLinearDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.SetUndoMarkName(markId23, "Linear Dimension")
    
    expression9 = sketchLinearDimensionBuilder1.Driving.ExpressionValue
    sketchLinearDimensionBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId26, None)
    
    theSession.SetUndoMarkVisibility(markId23, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.DeleteUndoMark(markId25, None)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch3 = theSession.ActiveSketch
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    scaleAboutPoint63 = NXOpen.Point3d(3.2448654583349503, -6.7847186856095032, 0.0)
    viewCenter63 = NXOpen.Point3d(-3.2448654583349503, 6.7847186856095032, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(2.5958923666679605, -5.4277749484876034, 0.0)
    viewCenter64 = NXOpen.Point3d(-2.5958923666679605, 5.4277749484876034, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(2.0767138933343685, -4.342219958790082, 0.0)
    viewCenter65 = NXOpen.Point3d(-2.0767138933343685, 4.342219958790082, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(1.661371114667495, -3.4737759670320663, 0.0)
    viewCenter66 = NXOpen.Point3d(-1.6613711146675207, 3.4737759670320663, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(-5.1955605767784254, 6.766311448827687, 0.0)
    viewCenter67 = NXOpen.Point3d(5.1955605767783846, -6.766311448827687, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(-4.156448461422741, 5.413049159062151, 0.0)
    viewCenter68 = NXOpen.Point3d(4.1564484614227082, -5.413049159062151, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-3.3251587691381932, 4.3304393272497208, 0.0)
    viewCenter69 = NXOpen.Point3d(3.3251587691381665, -4.330439327249727, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(-2.6601270153105543, 3.4643514617997768, 0.0)
    viewCenter70 = NXOpen.Point3d(2.6601270153105281, -3.4643514617997768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-2.128101612248452, 2.7714811694398214, 0.0)
    viewCenter71 = NXOpen.Point3d(2.1281016122484182, -2.7714811694398214, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(0.39592588134853002, -0.51470364575310723, 0.0)
    viewCenter72 = NXOpen.Point3d(-0.39592588134856044, 0.51470364575310723, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(0.31674070507881857, -0.41176291660248576, 0.0)
    viewCenter73 = NXOpen.Point3d(-0.31674070507885099, 0.41176291660248576, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(0.25339256406305488, -0.3294103332819886, 0.0)
    viewCenter74 = NXOpen.Point3d(-0.25339256406308297, 0.3294103332819886, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.Tolerance = 0.01
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder1.Section = section1
    
    smartVolumeProfileBuilder1 = revolveBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId29, "Revolve Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint1 = [None] * 3 
    starthelperpoint1[0] = 0.0
    starthelperpoint1[1] = 0.0
    starthelperpoint1[2] = 0.0
    revolveBuilder1.SetStartLimitHelperPoint(starthelperpoint1)
    
    endhelperpoint1 = [None] * 3 
    endhelperpoint1[0] = 0.0
    endhelperpoint1[1] = 0.0
    endhelperpoint1[2] = 0.0
    revolveBuilder1.SetEndLimitHelperPoint(endhelperpoint1)
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    features2[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section1.AllowSelfIntersection(False)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(2.2204460492503131e-16, -3.2818570145981347, -3.3306690738754696e-16)
    section1.AddToSection(rules1, line1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId31, None)
    
    revolveBuilder1.Section = section1
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId30, None)
    
    pointonstartcurve1 = NXOpen.Point3d(0.0, -4.0, -2.8516775465859793e-16)
    section1.SetStartCurveOfClosedLoop(0, pointonstartcurve1)
    
    revolveBuilder1.Section = section1
    
    pointonstartcurve2 = NXOpen.Point3d(0.0, -4.0, -2.8516775465859793e-16)
    section1.SetStartCurveOfClosedLoop(0, pointonstartcurve2)
    
    revolveBuilder1.Section = section1
    
    revolveBuilder1.Destroy()
    
    section1.Destroy()
    
    workPart.Expressions.Delete(expression10)
    
    theSession.UndoToMark(markId29, None)
    
    theSession.DeleteUndoMark(markId29, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder2 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder2.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder2.Tolerance = 0.01
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder2.Section = section2
    
    smartVolumeProfileBuilder2 = revolveBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId32, "Revolve Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint2 = [None] * 3 
    starthelperpoint2[0] = 0.0
    starthelperpoint2[1] = 0.0
    starthelperpoint2[2] = 0.0
    revolveBuilder2.SetStartLimitHelperPoint(starthelperpoint2)
    
    endhelperpoint2 = [None] * 3 
    endhelperpoint2[0] = 0.0
    endhelperpoint2[1] = 0.0
    endhelperpoint2[2] = 0.0
    revolveBuilder2.SetEndLimitHelperPoint(endhelperpoint2)
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    revolveBuilder2.Destroy()
    
    section2.Destroy()
    
    theSession.UndoToMark(markId32, None)
    
    theSession.DeleteUndoMark(markId32, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects1 = [NXOpen.TaggedObject.Null] * 6 
    objects1[0] = line1
    objects1[1] = line2
    objects1[2] = line3
    objects1[3] = line4
    objects1[4] = sketch3
    objects1[5] = datumCsys1
    nErrs2 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs3 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId33, None)
    
    scaleAboutPoint75 = NXOpen.Point3d(-0.79058479987679331, -0.040542810250090502, 0.0)
    viewCenter75 = NXOpen.Point3d(0.79058479987675867, 0.040542810250090502, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-0.98823099984598728, -0.050678512812613125, 0.0)
    viewCenter76 = NXOpen.Point3d(0.98823099984595275, 0.050678512812613125, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(-1.235288749807484, -0.063348141015766399, 0.0)
    viewCenter77 = NXOpen.Point3d(1.2352887498074461, 0.063348141015766399, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-1.5441109372593413, -0.079185176269708002, 0.0)
    viewCenter78 = NXOpen.Point3d(1.5441109372593076, 0.079185176269708002, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-1.8311572012370498, -0.049490735168565385, 0.0)
    viewCenter79 = NXOpen.Point3d(1.8311572012370076, 0.049490735168565385, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-1.4649257609896398, -0.039592588134852301, 0.0)
    viewCenter80 = NXOpen.Point3d(1.4649257609895994, 0.039592588134852301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-1.1719406087917121, -0.031674070507881853, 0.0)
    viewCenter81 = NXOpen.Point3d(1.1719406087916771, 0.031674070507884552, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint81, viewCenter81)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled3, undoUnavailable3 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = sketch3
    nErrs4 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs5 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId35, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder3 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder3.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder3.Tolerance = 0.01
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder3.Section = section3
    
    smartVolumeProfileBuilder3 = revolveBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId37, "Revolve Dialog")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint3 = [None] * 3 
    starthelperpoint3[0] = 0.0
    starthelperpoint3[1] = 0.0
    starthelperpoint3[2] = 0.0
    revolveBuilder3.SetStartLimitHelperPoint(starthelperpoint3)
    
    endhelperpoint3 = [None] * 3 
    endhelperpoint3[0] = 0.0
    endhelperpoint3[1] = 0.0
    endhelperpoint3[2] = 0.0
    revolveBuilder3.SetEndLimitHelperPoint(endhelperpoint3)
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    direction2 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction2, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem2
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature2 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    sketchInPlaceBuilder2.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject7 = sketchInPlaceBuilder2.Commit()
    
    sketchInPlaceBuilder2.Destroy()
    
    sketch4 = nXObject7
    sketch4.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId39, None, True)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_000")
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint82 = NXOpen.Point3d(0.038008884609439082, 0.12669628203153505, 0.0)
    viewCenter82 = NXOpen.Point3d(-0.038008884609474436, -0.12669628203153283, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(0.030407107687547726, 0.1013570256252298, 0.0)
    viewCenter83 = NXOpen.Point3d(-0.030407107687583083, -0.10135702562522626, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(0.024325686150032527, 0.081085620500185265, 0.0)
    viewCenter84 = NXOpen.Point3d(-0.0243256861500693, -0.081085620500181019, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(0.01946054892002376, 0.06486849640014708, 0.0)
    viewCenter85 = NXOpen.Point3d(-0.019460548920059967, -0.064868496400143694, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(0.015568439136015386, 0.051894797120118567, 0.0)
    viewCenter86 = NXOpen.Point3d(-0.015568439136051592, -0.051894797120114945, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Rectangle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId41, "Curve")
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId43, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint5 = NXOpen.Point3d(0.0, -2.5499999999999989, 0.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    startPoint6 = NXOpen.Point3d(0.0, -2.5499999999999989, 0.0)
    endPoint6 = NXOpen.Point3d(0.0, -2.5499999999999989, 0.35000000000000003)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    startPoint7 = NXOpen.Point3d(0.0, -2.5499999999999989, 0.35000000000000003)
    endPoint7 = NXOpen.Point3d(0.0, 0.0, 0.35000000000000003)
    line7 = workPart.Curves.CreateLine(startPoint7, endPoint7)
    
    startPoint8 = NXOpen.Point3d(0.0, 0.0, 0.35000000000000003)
    endPoint8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    line8 = workPart.Curves.CreateLine(startPoint8, endPoint8)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line5
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = line6
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = line6
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = line7
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = line7
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = line8
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    geom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_9.Geometry = line8
    geom1_9.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_9.SplineDefiningPointIndex = 0
    geom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_9.Geometry = line5
    geom2_9.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_9, geom2_9)
    
    geom4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom4.Geometry = line5
    geom4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateHorizontalConstraint(geom4)
    
    conGeom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_5.Geometry = line5
    conGeom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_5.SplineDefiningPointIndex = 0
    conGeom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_5.Geometry = line6
    conGeom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_5, conGeom2_5)
    
    conGeom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_6.Geometry = line6
    conGeom1_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_6.SplineDefiningPointIndex = 0
    conGeom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_6.Geometry = line7
    conGeom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_6, conGeom2_6)
    
    conGeom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_7.Geometry = line7
    conGeom1_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_7.SplineDefiningPointIndex = 0
    conGeom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_7.Geometry = line8
    conGeom2_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint18 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_7, conGeom2_7)
    
    conGeom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_8.Geometry = line8
    conGeom1_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_8.SplineDefiningPointIndex = 0
    conGeom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_8.Geometry = line5
    conGeom2_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint19 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_8, conGeom2_8)
    
    geom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_10.Geometry = line5
    geom1_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_10.SplineDefiningPointIndex = 0
    geom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys3 = feature2
    point9 = datumCsys3.FindObject("POINT 1")
    geom2_10.Geometry = point9
    geom2_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint20 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_10, geom2_10)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = line5
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_3.Geometry = line5
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 0.0
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(0.0, -1.2749999999999995, 0.28243845487735891)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_3, dimObject2_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint3
    dimension3 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression11 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = line6
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line6
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = 0.0
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 0.0
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(0.0, -2.2675615451226401, 0.17500000000000002)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_4, dimObject2_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint4 = sketchDimensionalConstraint4
    dimension4 = sketchHelpedDimensionalConstraint4.AssociatedDimension
    
    expression12 = sketchHelpedDimensionalConstraint4.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms3 = [NXOpen.SmartObject.Null] * 4 
    geoms3[0] = line5
    geoms3[1] = line6
    geoms3[2] = line7
    geoms3[3] = line8
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 4 
    geoms4[0] = line5
    geoms4[1] = line6
    geoms4[2] = line7
    geoms4[3] = line8
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms4)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines17 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines20)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines21 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines24)
    
    theSession.SetUndoMarkName(markId44, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    point10 = NXOpen.Point3d(0.0, -2.3782128693031899, 0.34999999999999998)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(line7, workPart.ModelingViews.WorkView, point10)
    
    point1_8 = NXOpen.Point3d(0.0, -2.5499999999999989, 0.35000000000000003)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line7, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    point1_9 = NXOpen.Point3d(0.0, 0.0, 0.35000000000000003)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line7, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    point1_10 = NXOpen.Point3d(0.0, -1.2749999999999995, 0.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line5, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    point1_11 = NXOpen.Point3d(0.0, -2.3782128693031899, 0.34999999999999998)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line7, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(0.0, -1.2749999999999995, 0.0)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line5, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(0.0, -2.3782128693031899, 0.34999999999999998)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line7, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    point1_14 = NXOpen.Point3d(0.0, -1.2749999999999995, 0.0)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line5, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point11 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point11
    assocOrigin3.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.DimensionLine = 0
    assocOrigin3.AssociatedView = NXOpen.View.Null
    assocOrigin3.AssociatedPoint = NXOpen.Point.Null
    assocOrigin3.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.XOffsetFactor = 0.0
    assocOrigin3.YOffsetFactor = 0.0
    assocOrigin3.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder4.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point12 = NXOpen.Point3d(0.0, -3.2500454609211484, 0.010451936482476804)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point12)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = False
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject8 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId45, None)
    
    theSession.SetUndoMarkName(markId44, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId44, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder5 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines25 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines25)
    
    lines26 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines26)
    
    lines27 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines27)
    
    lines28 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines28)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId46, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    expression13 = workPart.Expressions.FindObject("p4")
    expression13.SetFormula("0.6")
    
    theSession.SetUndoMarkVisibility(markId46, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(1.7142857142857144)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId47, None)
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId46, "Edit Driving Value")
    
    point13 = NXOpen.Point3d(0.0, -1.3984390996753895, 0.60000000000000009)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(line7, workPart.ModelingViews.WorkView, point13)
    
    point1_15 = NXOpen.Point3d(0.0, 0.0, 0.60000000000000009)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line7, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(0.0, -4.3714285714285701, 0.60000000000000009)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line7, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point14 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point14
    assocOrigin4.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.DimensionLine = 0
    assocOrigin4.AssociatedView = NXOpen.View.Null
    assocOrigin4.AssociatedPoint = NXOpen.Point.Null
    assocOrigin4.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.XOffsetFactor = 0.0
    assocOrigin4.YOffsetFactor = 0.0
    assocOrigin4.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder5.Origin.SetAssociativeOrigin(assocOrigin4)
    
    point15 = NXOpen.Point3d(0.0, -1.3901359321361708, 1.0068320411887157)
    sketchRapidDimensionBuilder5.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point15)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.TextCentered = False
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject9 = sketchRapidDimensionBuilder5.Commit()
    
    theSession.DeleteUndoMark(markId49, None)
    
    theSession.SetUndoMarkName(markId48, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId48, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines29 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines32)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId50, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    expression14 = workPart.Expressions.FindObject("p5")
    expression14.SetFormula("8")
    
    theSession.SetUndoMarkVisibility(markId50, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId51, None)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId50, "Edit Driving Value")
    
    scaleAboutPoint87 = NXOpen.Point3d(-2.9600792277314674, 0.55631222512765222, 0.0)
    viewCenter87 = NXOpen.Point3d(2.9600792277314318, -0.55631222512764866, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(-3.4094881707916791, 0.46705317408105118, 0.0)
    viewCenter88 = NXOpen.Point3d(3.4094881707916391, -0.46705317408104846, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(-4.0413073257290968, 0.4800268733610798, 0.0)
    viewCenter89 = NXOpen.Point3d(4.0413073257290577, -0.48002687336107752, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(-9.7546001461719261, 0.45407947480102018, 0.0)
    viewCenter90 = NXOpen.Point3d(9.7546001461718923, -0.45407947480101879, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(-8.8026549614997904, 0.33731618128075902, 0.0)
    viewCenter91 = NXOpen.Point3d(8.8026549614997531, -0.33731618128075785, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(-7.0421239691998352, 0.26985294502460722, 0.0)
    viewCenter92 = NXOpen.Point3d(7.0421239691997988, -0.26985294502460538, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint92, viewCenter92)
    
    perpendicularDimension1 = nXObject8
    point16 = NXOpen.Point3d(0.0, -8.380158308804674, 0.36164997599286386)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(perpendicularDimension1, workPart.ModelingViews.WorkView, point16)
    
    point1_17 = NXOpen.Point3d(0.0, -7.461059982127658, 0.59999999999999787)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line7, NXOpen.View.Null, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    point1_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    sketchRapidDimensionBuilder6.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    expression13.SetFormula("0.3")
    
    theSession.SetUndoMarkVisibility(markId52, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId53, None)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId52, "Edit Driving Value")
    
    sketchRapidDimensionBuilder6.Destroy()
    
    theSession.UndoToMark(markId54, None)
    
    theSession.DeleteUndoMark(markId54, None)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId38, None)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint4 = [None] * 3 
    starthelperpoint4[0] = 0.0
    starthelperpoint4[1] = 0.0
    starthelperpoint4[2] = 0.0
    revolveBuilder3.SetStartLimitHelperPoint(starthelperpoint4)
    
    endhelperpoint4 = [None] * 3 
    endhelperpoint4[0] = 0.0
    endhelperpoint4[1] = 0.0
    endhelperpoint4[2] = 0.0
    revolveBuilder3.SetEndLimitHelperPoint(endhelperpoint4)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 4 
    curves1[0] = line8
    curves1[1] = line6
    curves1[2] = line7
    curves1[3] = line5
    seedPoint1 = NXOpen.Point3d(0.0, -5.333333333333333, 0.19999999999999871)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch4, curves1, seedPoint1, 0.01)
    
    section3.AllowSelfIntersection(False)
    
    rules2 = [None] * 1 
    rules2[0] = regionBoundaryRule1
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section3.AddToSection(rules2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId56, None)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    refs1 = section3.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression15)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    revolveBuilder3.Section = section3
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    direction3 = workPart.Directions.CreateDirection(line5, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1.Point = NXOpen.Point.Null
    
    axis1.Evaluate()
    
    revolveBuilder3.Axis = axis1
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    theSession.DeleteUndoMark(markId57, None)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    revolveBuilder3.ParentFeatureInternal = True
    
    feature3 = revolveBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId58, None)
    
    theSession.SetUndoMarkName(markId37, "Revolve")
    
    expression18 = revolveBuilder3.Limits.StartExtend.Value
    expression19 = revolveBuilder3.Limits.EndExtend.Value
    revolveBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression16)
    
    workPart.Expressions.Delete(expression17)
    
    scaleAboutPoint93 = NXOpen.Point3d(-1.3176413331279779, -1.596373153597334, 0.0)
    viewCenter93 = NXOpen.Point3d(1.3176413331279435, 1.5963731535973382, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(-1.0541130665023823, -1.2770985228778671, 0.0)
    viewCenter94 = NXOpen.Point3d(1.054113066502353, 1.2770985228778706, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-0.84329045320191132, -1.0216788183022922, 0.0)
    viewCenter95 = NXOpen.Point3d(0.84329045320187812, 1.0216788183022978, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-0.67463236256153136, -0.81734305464183388, 0.0)
    viewCenter96 = NXOpen.Point3d(0.67463236256149928, 0.81734305464183943, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint96, viewCenter96)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId59, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    revolve1 = feature3
    edge1 = revolve1.FindObject("EDGE * 1 * 3 {(0.2598076211353,-8,0.15)(0,-8,-0.3)(-0.2598076211353,-8,0.15) REVOLVED(1)}")
    seedEdges1[0] = edge1
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules3 = [None] * 1 
    rules3[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules3, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    seedEdges2 = [NXOpen.Edge.Null] * 2 
    seedEdges2[0] = edge1
    edge2 = revolve1.FindObject("EDGE * 1 * 2 {(0.2598076211353,0,0.15)(0,0,-0.3)(-0.2598076211353,0,0.15) REVOLVED(1)}")
    seedEdges2[1] = edge2
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules4 = [None] * 1 
    rules4[0] = edgeMultipleSeedTangentRule2
    scCollector1.ReplaceRules(rules4, False)
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder1.Tolerance = 0.01
    
    edgeBlendBuilder1.AllInstancesOption = False
    
    edgeBlendBuilder1.RemoveSelfIntersection = True
    
    edgeBlendBuilder1.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder1.LimitFailingAreas = True
    
    edgeBlendBuilder1.ConvexConcaveY = False
    
    edgeBlendBuilder1.RollOverSmoothEdge = True
    
    edgeBlendBuilder1.RollOntoEdge = True
    
    edgeBlendBuilder1.MoveSharpEdge = True
    
    edgeBlendBuilder1.TrimmingOption = False
    
    edgeBlendBuilder1.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder1.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder1.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder1.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex1 = edgeBlendBuilder1.AddChainset(scCollector1, "0.1")
    
    feature4 = edgeBlendBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId60, None)
    
    theSession.SetUndoMarkName(markId59, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression23)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression22)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression20)
    
    workPart.Expressions.Delete(expression21)
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder2 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData2 = edgeBlendBuilder2.LimitsListData
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder2 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId61, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder2)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression27)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression26)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression24)
    
    workPart.Expressions.Delete(expression25)
    
    theSession.UndoToMark(markId61, None)
    
    theSession.DeleteUndoMark(markId61, None)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId62, "Name Parts Dialog")
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    theSession.DeleteUndoMark(markId63, None)
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    workPart.AssignPermanentName("C:\\Users\\Admin\\Desktop\\機器人組裝\車三.prt\\車三.prt")
    
    theSession.DeleteUndoMark(markId64, None)
    
    theSession.SetUndoMarkName(markId62, "Name Parts")
    
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()