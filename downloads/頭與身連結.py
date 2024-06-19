# NX 1872
# Journal created by Reader on Wed Jun 19 19:48:54 2024 台北標準時間

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
    
    fileNew1.NewFileName = "C:\\Users\\Reader\\Desktop\\嚴\m\\model1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.81088808275580626
    rotMatrix1.Xy = 0.58423864647107004
    rotMatrix1.Xz = -0.033551769167385746
    rotMatrix1.Yx = -0.024803174430979645
    rotMatrix1.Yy = 0.022970054063731961
    rotMatrix1.Yz = 0.99942842622893935
    rotMatrix1.Zx = 0.5846753969364159
    rotMatrix1.Zy = 0.81125679077956392
    rotMatrix1.Zz = -0.0041351700427958819
    translation1 = NXOpen.Point3d(-21.307882789659491, 0.90672470924261717, 15.195757534814653)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.90572327300951838)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = -0.028055028728903655
    rotMatrix2.Xy = 0.99946603691134328
    rotMatrix2.Xz = -0.016749818618444386
    rotMatrix2.Yx = -0.46519793790800607
    rotMatrix2.Yy = 0.0017768288246612601
    rotMatrix2.Yz = 0.88520490364969506
    rotMatrix2.Zx = 0.88476199846577763
    rotMatrix2.Zy = 0.032626430084492314
    rotMatrix2.Zz = 0.4648996903965219
    translation2 = NXOpen.Point3d(-21.307882789659491, 0.90672470924261717, 15.195757534814653)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.90572327300951838)
    
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
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Rectangle...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId9, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(0.0, 4.6739809602848421, -14.999999999999993)
    endPoint1 = NXOpen.Point3d(0.0, 4.6739809602848572, 15.000000000000007)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(0.0, 4.6739809602848572, 15.000000000000007)
    endPoint2 = NXOpen.Point3d(0.0, -4.6739809602848217, 15.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(0.0, -4.6739809602848217, 15.0)
    endPoint3 = NXOpen.Point3d(0.0, -4.6739809602848368, -15.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(0.0, -4.6739809602848368, -15.0)
    endPoint4 = NXOpen.Point3d(0.0, 4.6739809602848421, -14.999999999999993)
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
    
    geom3.Geometry = line2
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
    
    conGeom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point2 = datumCsys2.FindObject("POINT 1")
    conGeom1_5.Geometry = point2
    conGeom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_5.SplineDefiningPointIndex = 0
    conGeom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_5.Geometry = line1
    conGeom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_5, conGeom2_5)
    
    conGeom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_6.Geometry = point2
    conGeom1_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_6.SplineDefiningPointIndex = 0
    conGeom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_6.Geometry = line2
    conGeom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_6, conGeom2_6)
    
    geom4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom4.Geometry = line1
    geom4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateVerticalConstraint(geom4)
    
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
    dimOrigin1 = NXOpen.Point3d(0.0, 14.61079087585099, 2.1042199519224297e-15)
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
    dimOrigin2 = NXOpen.Point3d(0.0, 1.0210555061119592e-14, 24.936809915566144)
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
    
    point3 = NXOpen.Point3d(0.0, -4.673980960284827, 4.9661047703026071)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(line3, workPart.ModelingViews.WorkView, point3)
    
    point1_1 = NXOpen.Point3d(0.0, -4.6739809602848217, 15.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(0.0, -4.6739809602848368, -15.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    dimensionlinearunits21 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits23 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    point1_3 = NXOpen.Point3d(0.0, 4.6739809602848492, 7.1054273576010019e-15)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line1, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(0.0, -4.673980960284827, 4.9661047703026071)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line3, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    point1_5 = NXOpen.Point3d(0.0, 4.6739809602848492, 7.1054273576010019e-15)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line1, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(0.0, -4.673980960284827, 4.9661047703026071)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line3, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    point1_7 = NXOpen.Point3d(0.0, 4.6739809602848492, 7.1054273576010019e-15)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line1, workPart.ModelingViews.WorkView, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    dimensionlinearunits27 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits37 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
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
    
    point5 = NXOpen.Point3d(0.0, 3.7976095302313944, 33.594238152047097)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
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
    
    dimensionlinearunits39 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits41 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits45 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    expression7 = workPart.Expressions.FindObject("p0")
    expression7.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId12, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(1.069751897255294)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId12, "Edit Driving Value")
    
    scaleAboutPoint1 = NXOpen.Point3d(20.740790511263825, -0.87637143005340246, 0.0)
    viewCenter1 = NXOpen.Point3d(-20.740790511263825, 0.87637143005340246, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(25.925988139079781, -1.0954642875667531, 0.0)
    viewCenter2 = NXOpen.Point3d(-25.925988139079781, 1.0954642875667531, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(32.407485173849722, -1.3693303594584412, 0.0)
    viewCenter3 = NXOpen.Point3d(-32.407485173849722, 1.3693303594584412, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(47.356008264604363, -2.2822172657640851, 0.0)
    viewCenter4 = NXOpen.Point3d(-47.356008264604363, 2.2822172657640851, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(37.884806611683487, -1.8257738126112679, 0.0)
    viewCenter5 = NXOpen.Point3d(-37.884806611683487, 1.8257738126112679, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(30.307845289346794, -1.4606190500890144, 0.0)
    viewCenter6 = NXOpen.Point3d(-30.307845289346794, 1.4606190500890144, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(24.246276231477434, -1.1684952400712116, 0.0)
    viewCenter7 = NXOpen.Point3d(-24.246276231477434, 1.1684952400712116, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(7.7120685844699413, 1.4021942880854439, 0.0)
    viewCenter8 = NXOpen.Point3d(-7.7120685844699413, -1.4021942880854439, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(6.1696548675759537, 1.3087146688797371, 0.0)
    viewCenter9 = NXOpen.Point3d(-6.1696548675759537, -1.3087146688797371, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    point6 = NXOpen.Point3d(0.0, 4.9999999999998446, 12.444145667472052)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line1, workPart.ModelingViews.WorkView, point6)
    
    point1_8 = NXOpen.Point3d(0.0, 4.9999999999998463, 16.046278458829416)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line1, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    point1_9 = NXOpen.Point3d(0.0, 4.9999999999998304, -16.046278458829402)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line1, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
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
    
    point8 = NXOpen.Point3d(0.0, 34.000144186066848, 3.9188043959125496)
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
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits75 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits77 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits79 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits83 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    expression8 = workPart.Expressions.FindObject("p1")
    expression8.SetFormula("35")
    
    theSession.SetUndoMarkVisibility(markId16, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId16, "Edit Driving Value")
    
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId18, None)
    
    theSession.DeleteUndoMark(markId18, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("10")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId20, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(-1.5099033134902129e-14, -4.9999999999999831, 17.472049725525974)
    section1.AddToSection(rules1, line3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId22, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId21, None)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = -0.099935846474691531
    rotMatrix3.Xy = 0.99483893157022718
    rotMatrix3.Xz = 0.01755923750026725
    rotMatrix3.Yx = -0.83227555074550752
    rotMatrix3.Yy = -0.093250907419914486
    rotMatrix3.Yz = 0.54646287696111751
    rotMatrix3.Zx = 0.5452799594892912
    rotMatrix3.Zy = 0.039997106114898255
    rotMatrix3.Zz = 0.83729922804322732
    translation3 = NXOpen.Point3d(-21.578371729591414, 4.8157864602100195, 11.752891056742044)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.90572327300951838)
    
    extrudeBuilder1.Destroy()
    
    section1.Destroy()
    
    workPart.Expressions.Delete(expression9)
    
    workPart.Expressions.Delete(expression10)
    
    theSession.UndoToMark(markId20, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 5 
    objects1[0] = line1
    objects1[1] = line2
    objects1[2] = line3
    objects1[3] = line4
    objects1[4] = sketch2
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show")
    
    objects2 = [NXOpen.DisplayableObject.Null] * 5 
    objects2[0] = line1
    objects2[1] = line2
    objects2[2] = line3
    objects2[3] = line4
    objects2[4] = sketch2
    theSession.DisplayManager.ShowObjects(objects2, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = sketch2
    nErrs2 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs3 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId25, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane4
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId27, "Create Sketch Dialog")
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = -0.059817278759373066
    rotMatrix4.Xy = 0.99747311676894468
    rotMatrix4.Xz = 0.038331116407834563
    rotMatrix4.Yx = -0.20933835519449481
    rotMatrix4.Yy = -0.050081233047086671
    rotMatrix4.Yz = 0.97655994344481745
    rotMatrix4.Zx = 0.97601196007338209
    rotMatrix4.Zy = 0.050390985500691425
    rotMatrix4.Zz = 0.21180510469292774
    translation4 = NXOpen.Point3d(-21.578371729591414, 4.8157864602100195, 11.752891056742044)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.90572327300951838)
    
    direction3 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction3, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane5.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom5 = [NXOpen.NXObject.Null] * 1 
    geom5[0] = datumPlane1
    plane5.SetGeometry(geom5)
    
    plane5.SetFlip(False)
    
    plane5.SetExpression(None)
    
    plane5.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane5.Evaluate()
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane6.SynchronizeToPlane(plane5)
    
    plane6.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom6 = [NXOpen.NXObject.Null] * 1 
    geom6[0] = datumPlane1
    plane6.SetGeometry(geom6)
    
    plane6.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane6.Evaluate()
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId28, None)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
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
    
    nXObject5 = sketchInPlaceBuilder2.Commit()
    
    sketch3 = nXObject5
    feature2 = sketch3.Feature
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId30)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId29, None)
    
    theSession.SetUndoMarkName(markId27, "Create Sketch")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression12)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression11)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane4.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression14)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression13)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane6.DestroyPlane()
    
    scaleAboutPoint10 = NXOpen.Point3d(39.728838162420892, 3.2133619101958009, 0.0)
    viewCenter10 = NXOpen.Point3d(-39.728838162420892, -3.2133619101958009, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(49.661047703026121, 4.0167023877447505, 0.0)
    viewCenter11 = NXOpen.Point3d(-49.661047703026121, -4.0167023877447505, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(62.076309628782639, 5.0208779846809382, 0.0)
    viewCenter12 = NXOpen.Point3d(-62.076309628782639, -5.0208779846809382, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(89.006473364798723, 3.9938802150870876, 0.0)
    viewCenter13 = NXOpen.Point3d(-89.006473364798637, -3.9938802150870876, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(71.205178691838981, 3.1951041720696702, 0.0)
    viewCenter14 = NXOpen.Point3d(-71.205178691838896, -3.1951041720696702, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(56.964142953471189, 2.5560833376557364, 0.0)
    viewCenter15 = NXOpen.Point3d(-56.964142953471125, -2.5560833376557364, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch4 = theSession.ActiveSketch
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.1044513909164272
    rotMatrix5.Xy = 0.99292082435194406
    rotMatrix5.Xz = 0.056552130851789943
    rotMatrix5.Yx = -0.62869148874302461
    rotMatrix5.Yy = 0.021861808775403186
    rotMatrix5.Yz = 0.77734745982677711
    rotMatrix5.Zx = 0.77060814874856998
    rotMatrix5.Zy = -0.11674886674106071
    rotMatrix5.Zz = 0.62652436760031494
    translation5 = NXOpen.Point3d(-21.578371729591414, 4.8157864602100195, 11.752891056742044)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.90572327300951838)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects4 = [NXOpen.DisplayableObject.Null] * 1 
    objects4[0] = sketch4
    theSession.DisplayManager.BlankObjects(objects4)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects5 = [NXOpen.DisplayableObject.Null] * 1 
    objects5[0] = sketch4
    theSession.DisplayManager.BlankObjects(objects5)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = sketch4
    nErrs5 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs6 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId34, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.PlaneReference = plane7
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId36, "Create Sketch Dialog")
    
    datumAxis2 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction4 = workPart.Directions.CreateDirection(datumAxis2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane2 = workPart.Datums.FindObject("DATUM_CSYS(0) XY plane")
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane2, direction4, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem3
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane8.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom7 = [NXOpen.NXObject.Null] * 1 
    geom7[0] = datumPlane2
    plane8.SetGeometry(geom7)
    
    plane8.SetFlip(False)
    
    plane8.SetExpression(None)
    
    plane8.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane8.Evaluate()
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane9.SynchronizeToPlane(plane8)
    
    plane9.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom8 = [NXOpen.NXObject.Null] * 1 
    geom8[0] = datumPlane2
    plane9.SetGeometry(geom8)
    
    plane9.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane9.Evaluate()
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId37, None)
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
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
    
    nXObject6 = sketchInPlaceBuilder3.Commit()
    
    sketch5 = nXObject6
    feature3 = sketch5.Feature
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs7 = theSession.UpdateManager.DoUpdate(markId39)
    
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId38, None)
    
    theSession.SetUndoMarkName(markId36, "Create Sketch")
    
    sketchInPlaceBuilder3.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression16)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression15)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane7.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression18)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression17)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane9.DestroyPlane()
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId41, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 8.262509080385513, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = arc1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys3 = workPart.Features.FindObject("SKETCH(1:1B)")
    point9 = datumCsys3.FindObject("POINT 1")
    geom2_5.Geometry = point9
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = arc1
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(0.0, 3.3122699718553799, 0.0)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression19 = sketchDimensionalConstraint3.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId42, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    point1_10 = NXOpen.Point3d(6.216404593789834, 5.4429192745953632, 0.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc1, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    point1_11 = NXOpen.Point3d(6.216404593789834, 5.4429192745953632, 0.0)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point10 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point10
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
    
    point11 = NXOpen.Point3d(35.054857202136098, 11.392828590694235, 0.0)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point11)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = False
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject7 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId43, None)
    
    theSession.SetUndoMarkName(markId42, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId42, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId44, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    expression20 = workPart.Expressions.FindObject("p0")
    expression20.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId44, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.605143056589176)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId45, None)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId44, "Edit Driving Value")
    
    sketchRapidDimensionBuilder5.Destroy()
    
    theSession.UndoToMark(markId46, None)
    
    theSession.DeleteUndoMark(markId46, None)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.99418088249166525
    rotMatrix6.Xy = 0.09056413144759215
    rotMatrix6.Xz = -0.058331046478147547
    rotMatrix6.Yx = 0.040028136283858304
    rotMatrix6.Yy = 0.19214350129760996
    rotMatrix6.Yz = 0.98055016353817082
    rotMatrix6.Zx = 0.10001060540629388
    rotMatrix6.Zy = -0.9771791099917333
    rotMatrix6.Zz = 0.1874002822890832
    translation6 = NXOpen.Point3d(-0.35332064698307519, 3.4137689331011267, 2.9912216239639022)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.90572327300951838)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch6 = theSession.ActiveSketch
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("10")
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId48, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = feature3
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section2.AllowSelfIntersection(True)
    
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule2
    helpPoint2 = NXOpen.Point3d(4.9529396213588619, -0.54823568967392156, 0.0)
    section2.AddToSection(rules2, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId50, None)
    
    direction5 = workPart.Directions.CreateDirection(sketch6, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder2.Direction = direction5
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId49, None)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("35")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("35")
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId51, None)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder2.ParentFeatureInternal = False
    
    feature4 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId52, None)
    
    theSession.SetUndoMarkName(markId48, "Extrude")
    
    expression23 = extrudeBuilder2.Limits.StartExtend.Value
    expression24 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression21)
    
    workPart.Expressions.Delete(expression22)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.99576046686549757
    rotMatrix7.Xy = 0.017101998054170599
    rotMatrix7.Xz = 0.090380386646416969
    rotMatrix7.Yx = -0.090843677793334326
    rotMatrix7.Yy = 0.02859118533090621
    rotMatrix7.Yz = 0.99545465508296749
    rotMatrix7.Zx = 0.014440181189354724
    rotMatrix7.Zy = -0.99944487881219313
    rotMatrix7.Zz = 0.030023580454196914
    translation7 = NXOpen.Point3d(-22.170366205997393, 0.99891054322668626, 22.191654831799113)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 0.90572327300951838)
    
    scaleAboutPoint16 = NXOpen.Point3d(-7.3030952504450291, 4.3818571502670123, 0.0)
    viewCenter16 = NXOpen.Point3d(7.3030952504450291, -4.3818571502670123, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-9.1288690630563476, 5.4773214378337656, 0.0)
    viewCenter17 = NXOpen.Point3d(9.1288690630562233, -5.4773214378337656, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-11.411086328820433, 6.8466517972922061, 0.0)
    viewCenter18 = NXOpen.Point3d(11.411086328820279, -6.8466517972922061, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-14.263857911025543, 8.5583147466152578, 0.0)
    viewCenter19 = NXOpen.Point3d(14.263857911025347, -8.5583147466152578, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(8.558314746615137, 11.411086328820364, 0.0)
    viewCenter20 = NXOpen.Point3d(-8.5583147466153786, -11.411086328820243, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(6.8466517972921084, 9.1288690630562428, 0.0)
    viewCenter21 = NXOpen.Point3d(-6.8466517972923038, -9.1288690630561931, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(5.4773214378336093, 7.3030952504450326, 0.0)
    viewCenter22 = NXOpen.Point3d(-5.4773214378339201, -7.3030952504449544, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(4.3818571502668879, 5.8424762003560264, 0.0)
    viewCenter23 = NXOpen.Point3d(-4.3818571502671366, -5.8424762003559643, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-17.527428601068149, 8.1794666804984555, 0.0)
    viewCenter24 = NXOpen.Point3d(17.527428601067925, -8.1794666804984058, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(-13.320845736811837, 6.3098742963845371, 0.0)
    viewCenter25 = NXOpen.Point3d(13.320845736811597, -6.3098742963844776, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-10.282758112626691, 4.8609401986962322, 0.0)
    viewCenter26 = NXOpen.Point3d(10.282758112626484, -4.8609401986961691, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-20.939434702076078, 0.29913478145824934, 0.0)
    viewCenter27 = NXOpen.Point3d(20.939434702075847, -0.2991347814582111, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.61999707294077799
    rotMatrix8.Xy = -0.78459083232270765
    rotMatrix8.Xz = -0.0045667691017338592
    rotMatrix8.Yx = -0.38278648707943858
    rotMatrix8.Yy = -0.30755495180991038
    rotMatrix8.Yz = 0.8711397459228839
    rotMatrix8.Zx = -0.68489279077403808
    rotMatrix8.Zy = -0.53835599509280541
    rotMatrix8.Zz = -0.49101393839012836
    translation8 = NXOpen.Point3d(-23.674253714626524, -1.1765308234127785, 31.309811411574795)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 2.211238459495894)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.95638303532763835
    rotMatrix9.Xy = 0.2762210048153978
    rotMatrix9.Xz = -0.095044443479160717
    rotMatrix9.Yx = 0.085188949282016826
    rotMatrix9.Yy = 0.047491099860242955
    rotMatrix9.Yz = 0.99523235395272891
    rotMatrix9.Zx = 0.27941784599004643
    rotMatrix9.Zy = -0.95992007580466487
    rotMatrix9.Zz = 0.021888705065540727
    translation9 = NXOpen.Point3d(-22.090894413021566, -3.3481514639350651, 22.334015151100616)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 2.211238459495894)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.Tolerance = 0.01
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder1.Section = section3
    
    smartVolumeProfileBuilder3 = revolveBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId53, "Revolve Dialog")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
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
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    direction6 = workPart.Directions.CreateDirection(datumAxis2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane3 = workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane")
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane3, direction6, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, True)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem4
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature5 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder4.Csystem = cartesianCoordinateSystem4
    
    sketchInPlaceBuilder4.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject8 = sketchInPlaceBuilder4.Commit()
    
    sketchInPlaceBuilder4.Destroy()
    
    sketch7 = nXObject8
    sketch7.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId55, None, True)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint28 = NXOpen.Point3d(6.7604460609558252, 3.8289252026653529, 0.0)
    viewCenter28 = NXOpen.Point3d(-6.7604460609560757, -3.8289252026652902, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(8.4505575761948357, 4.786156503331692, 0.0)
    viewCenter29 = NXOpen.Point3d(-8.450557576195056, -4.7861565033316396, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(10.563196970243542, 5.9826956291645814, 0.0)
    viewCenter30 = NXOpen.Point3d(-10.563196970243803, -5.9826956291645486, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(13.203996212804467, 7.4783695364557259, 0.0)
    viewCenter31 = NXOpen.Point3d(-13.203996212804711, -7.478369536455685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(30.234814336842199, 9.3479619205696558, 0.0)
    viewCenter32 = NXOpen.Point3d(-30.234814336842454, -9.3479619205696292, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(24.187851469473763, 7.4783695364557259, 0.0)
    viewCenter33 = NXOpen.Point3d(-24.187851469474008, -7.478369536455685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(19.35028117557901, 5.9826956291645805, 0.0)
    viewCenter34 = NXOpen.Point3d(-19.350281175579223, -5.9826956291645477, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(15.480224940463158, 4.7861565033316777, 0.0)
    viewCenter35 = NXOpen.Point3d(-15.480224940463417, -4.7861565033316387, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(12.384179952370507, 3.8289252026653426, 0.0)
    viewCenter36 = NXOpen.Point3d(-12.384179952370756, -3.8289252026653009, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(2.5366629467656439, 3.1588632921989177, 0.0)
    viewCenter37 = NXOpen.Point3d(-2.5366629467658779, -3.158863292198876, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId58, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(-0.40855380473013747, -0.0, -1.0146651787062404)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 6.9423865728073944, ( 273.37375929846331 * math.pi/180.0 ), ( 446.62624070153669 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = arc2
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(2.8922627311457858, 0.0, 0.36653846431181325)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateRadialDimension(dimObject1_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension4 = sketchDimensionalConstraint4.AssociatedDimension
    
    expression25 = sketchDimensionalConstraint4.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId59, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint5 = NXOpen.Point3d(-1.1102230246251565e-16, 0.0, -7.9450197955304702)
    endPoint5 = NXOpen.Point3d(6.8930927689148836e-15, 0.0, 5.9156894381179903)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line5
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = arc2
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    geom9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom9.Geometry = line5
    geom9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateVerticalConstraint(geom9)
    
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = line5
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = arc2
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.ActiveSketch.Update()
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId61, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint6 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    endPoint6 = NXOpen.Point3d(14.72773270178104, 0.0, 5.9156894381179903)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = line6
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = arc2
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = line6
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_3.Geometry = line6
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 0.0
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(8.2440034543366743, 0.0, 0.082090599906335715)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_5, dimObject2_3, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint5
    dimension5 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression26 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis3 = workPart.Datums.FindObject("SKETCH(3:1B) X axis")
    dimObject1_6.Geometry = datumAxis3
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 28.574999999999999
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line6
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = 14.72773270178104
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 5.9156894381179903
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(4.352607639209241, 0.0, 0.55494685019235035)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_6, dimObject2_4, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension6 = sketchDimensionalConstraint6.AssociatedDimension
    
    expression27 = sketchDimensionalConstraint6.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.ActiveSketch.Update()
    
    theSession.DeleteUndoMark(markId62, "Curve")
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects7 = [NXOpen.NXObject.Null] * 1 
    objects7[0] = line6
    errorList1 = theSession.ActiveSketch.DeleteObjects(objects7)
    
    errorList1.Dispose()
    theSession.DeleteUndoMark(markId63, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines33 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines36)
    
    theSession.SetUndoMarkName(markId65, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point1_13 = NXOpen.Point3d(5.5788873849758049, 0.0, 2.4992043871867646)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    point1_14 = NXOpen.Point3d(-0.40855380473013747, 0.0, -2.0146651787062404)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    point1_15 = NXOpen.Point3d(-0.40855380473013747, 0.0, -0.0146651787062404)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(5.5788873849758049, 0.0, 2.4992043871867646)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    point1_18 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point1_19 = NXOpen.Point3d(5.5788873849758049, 0.0, 2.4992043871867646)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    point1_20 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point1_21 = NXOpen.Point3d(5.5788873849758049, 0.0, 2.4992043871867646)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    point1_22 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(5.5788873849758049, 0.0, 2.4992043871867646)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    point1_24 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point1_25 = NXOpen.Point3d(5.5788873849758049, 0.0, 2.4992043871867646)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(-0.40855380473013747, 0.0, -1.0146651787062404)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point12 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point12
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
    sketchRapidDimensionBuilder6.Origin.SetAssociativeOrigin(assocOrigin4)
    
    point13 = NXOpen.Point3d(12.583534588288455, 0.0, 11.123027713742825)
    sketchRapidDimensionBuilder6.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point13)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.TextCentered = False
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject9 = sketchRapidDimensionBuilder6.Commit()
    
    theSession.DeleteUndoMark(markId66, None)
    
    theSession.SetUndoMarkName(markId65, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId65, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines37 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines40)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId67, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    expression28 = workPart.Expressions.FindObject("p7")
    expression28.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId67, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(1.4404268467511165)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId68, None)
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId67, "Edit Driving Value")
    
    point1_27 = NXOpen.Point3d(-0.58849186867560332, 0.0, -1.4615509638719881)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    point1_28 = NXOpen.Point3d(-0.58849186867560332, 0.0, -1.4615509638719881)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    point1_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin5 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin5.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin5.View = NXOpen.View.Null
    assocOrigin5.ViewOfGeometry = workPart.ModelingViews.WorkView
    point14 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin5.PointOnGeometry = point14
    assocOrigin5.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.DimensionLine = 0
    assocOrigin5.AssociatedView = NXOpen.View.Null
    assocOrigin5.AssociatedPoint = NXOpen.Point.Null
    assocOrigin5.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.XOffsetFactor = 0.0
    assocOrigin5.YOffsetFactor = 0.0
    assocOrigin5.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder7.Origin.SetAssociativeOrigin(assocOrigin5)
    
    point15 = NXOpen.Point3d(5.9977832397041073, 0.0, -2.4313675036924085)
    sketchRapidDimensionBuilder7.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point15)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.TextCentered = False
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject10 = sketchRapidDimensionBuilder7.Commit()
    
    theSession.DeleteUndoMark(markId70, None)
    
    theSession.SetUndoMarkName(markId69, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId69, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId71, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    scaleAboutPoint38 = NXOpen.Point3d(-3.4843219344255547, -2.5270906337590908, 0.0)
    viewCenter38 = NXOpen.Point3d(3.4843219344253273, 2.5270906337591308, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-4.3554024180319262, -3.1588632921988635, 0.0)
    viewCenter39 = NXOpen.Point3d(4.3554024180316926, 3.1588632921989053, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(-5.4442530225398862, -3.9485791152485894, 0.0)
    viewCenter40 = NXOpen.Point3d(5.4442530225396357, 3.9485791152486311, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-6.8053162781748062, -4.9357238940607369, 0.0)
    viewCenter41 = NXOpen.Point3d(6.8053162781745851, 4.9357238940607893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(-8.5066453477184751, -6.1696548675759209, 0.0)
    viewCenter42 = NXOpen.Point3d(8.5066453477182797, 6.1696548675759697, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(-10.633306684648051, -7.7120685844699199, 0.0)
    viewCenter43 = NXOpen.Point3d(10.633306684647888, 7.7120685844699608, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(-8.5066453477184734, -6.16965486757592, 0.0)
    viewCenter44 = NXOpen.Point3d(8.506645347718278, 6.1696548675759688, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(-6.8053162781747787, -4.935723894060736, 0.0)
    viewCenter45 = NXOpen.Point3d(6.8053162781746224, 4.9357238940607751, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(-5.4442530225398436, -3.948579115248589, 0.0)
    viewCenter46 = NXOpen.Point3d(5.4442530225396979, 3.9485791152486307, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(-4.1639561578986051, -3.0631401621322194, 0.0)
    viewCenter47 = NXOpen.Point3d(4.1639561578984718, 3.063140162132278, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(-3.6374789425321228, -2.2973551215991597, 0.0)
    viewCenter48 = NXOpen.Point3d(3.6374789425319762, 2.2973551215992263, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(-2.9712459572683771, -1.8378840972793224, 0.0)
    viewCenter49 = NXOpen.Point3d(2.9712459572682168, 1.8378840972793866, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(-2.4260070084088272, -1.4703072778234538, 0.0)
    viewCenter50 = NXOpen.Point3d(2.4260070084086691, 1.4703072778235178, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    theSession.UndoToMark(markId71, None)
    
    theSession.DeleteUndoMark(markId71, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects8 = [NXOpen.NXObject.Null] * 1 
    radiusDimension1 = nXObject10
    objects8[0] = radiusDimension1
    errorList2 = theSession.ActiveSketch.DeleteObjects(objects8)
    
    errorList2.Dispose()
    theSession.DeleteUndoMark(markId72, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects9 = [NXOpen.NXObject.Null] * 1 
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    objects9[0] = perpendicularDimension1
    errorList3 = theSession.ActiveSketch.DeleteObjects(objects9)
    
    errorList3.Dispose()
    theSession.DeleteUndoMark(markId74, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects10 = [NXOpen.NXObject.Null] * 1 
    perpendicularDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    objects10[0] = perpendicularDimension2
    errorList4 = theSession.ActiveSketch.DeleteObjects(objects10)
    
    errorList4.Dispose()
    theSession.DeleteUndoMark(markId76, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects11 = [NXOpen.NXObject.Null] * 1 
    parallelDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 4 1")
    objects11[0] = parallelDimension1
    errorList5 = theSession.ActiveSketch.DeleteObjects(objects11)
    
    errorList5.Dispose()
    theSession.DeleteUndoMark(markId78, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects12 = [NXOpen.NXObject.Null] * 1 
    horizontalDimension1 = nXObject9
    objects12[0] = horizontalDimension1
    errorList6 = theSession.ActiveSketch.DeleteObjects(objects12)
    
    errorList6.Dispose()
    theSession.DeleteUndoMark(markId80, None)
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId83, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    perpendicularDimension3 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension3)
    
    theSession.UpdateManager.LogForUpdate(horizontalDimension1)
    
    perpendicularDimension4 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension4)
    
    parallelDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    center3 = NXOpen.Point3d(-0.46085613209410203, 0.0, 0.0)
    arc2.SetParameters(9.9999999999962466, center3, ( 273.37375929846331 * math.pi/180.0 ), ( 446.62624070153669 * math.pi/180.0 ))
    
    startPoint7 = NXOpen.Point3d(0.1276357365814986, 0.0, -9.9826688475791698)
    endPoint7 = NXOpen.Point3d(0.12763573658149863, 0.0, 9.9826688475791698)
    line5.SetEndpoints(startPoint7, endPoint7)
    
    sketchHelpedDimensionalConstraint4 = theSession.ActiveSketch.FindObject("ENTITY 243 8 1")
    sketchHelpedDimensionalConstraint4.Refresh()
    
    sketchHelpedDimensionalConstraint5 = theSession.ActiveSketch.FindObject("ENTITY 243 14 1")
    helpPoint1_1 = NXOpen.Point3d(9.4115081313206428, 0.0, -1.4615509638719881)
    helpPoint2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint5.SetHelpPoints(True, False, helpPoint1_1, helpPoint2_1)
    
    sketchHelpedDimensionalConstraint6 = theSession.ActiveSketch.FindObject("ENTITY 243 2 1")
    sketchHelpedDimensionalConstraint6.Refresh()
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId83)
    
    geoms3 = [NXOpen.SmartObject.Null] * 2 
    geoms3[0] = arc2
    geoms3[1] = line5
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 2 
    geoms4[0] = arc2
    geoms4[1] = line5
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms4)
    
    geoms5 = [NXOpen.SmartObject.Null] * 2 
    geoms5[0] = arc2
    geoms5[1] = line5
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms5)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder9 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines45 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines48)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder9.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines49 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines49)
    
    lines50 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines50)
    
    lines51 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines51)
    
    lines52 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines52)
    
    theSession.SetUndoMarkName(markId84, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder9.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder9.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    point16 = NXOpen.Point3d(0.12763573658149951, 0.0, 5.5886992258103501)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(line5, workPart.ModelingViews.WorkView, point16)
    
    point1_30 = NXOpen.Point3d(0.12763573658149863, 0.0, 9.9826688475791698)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line5, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(0.1276357365814986, 0.0, -9.9826688475791698)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line5, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    point1_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    point1_33 = NXOpen.Point3d(0.12763573658149951, 0.0, 5.5886992258103501)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line5, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    point1_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    point1_35 = NXOpen.Point3d(0.12763573658149951, 0.0, 5.5886992258103501)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line5, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    point1_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Destroy()
    
    theSession.UndoToMark(markId84, None)
    
    theSession.DeleteUndoMark(markId84, None)
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId86, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension3)
    
    theSession.UpdateManager.LogForUpdate(horizontalDimension1)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension4)
    
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    center4 = NXOpen.Point3d(0.63697330201409885, 0.0, 0.039208194075293079)
    arc2.SetParameters(9.9999999999962466, center4, ( 273.37375929846331 * math.pi/180.0 ), ( 446.62624070153669 * math.pi/180.0 ))
    
    startPoint8 = NXOpen.Point3d(1.2254651706896995, 0.0, -9.9434606535038768)
    endPoint8 = NXOpen.Point3d(1.2254651706896995, 0.0, 10.021877041654463)
    line5.SetEndpoints(startPoint8, endPoint8)
    
    sketchHelpedDimensionalConstraint4.Refresh()
    
    helpPoint1_2 = NXOpen.Point3d(9.5391438679021441, 0.0, 0.0)
    helpPoint2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint5.SetHelpPoints(True, False, helpPoint1_2, helpPoint2_2)
    
    sketchHelpedDimensionalConstraint6.Refresh()
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId86)
    
    geoms6 = [NXOpen.SmartObject.Null] * 2 
    geoms6[0] = arc2
    geoms6[1] = line5
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms6)
    
    geoms7 = [NXOpen.SmartObject.Null] * 2 
    geoms7[0] = arc2
    geoms7[1] = line5
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms7)
    
    geoms8 = [NXOpen.SmartObject.Null] * 2 
    geoms8[0] = arc2
    geoms8[1] = line5
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms8)
    
    scaleAboutPoint51 = NXOpen.Point3d(-8.2925330469245271, -0.78416388150582939, 0.0)
    viewCenter51 = NXOpen.Point3d(8.2925330469243601, 0.78416388150588412, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(-10.365666308655632, -0.9802048518822909, 0.0)
    viewCenter52 = NXOpen.Point3d(10.365666308655479, 0.98020485188235074, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(-12.957082885819517, -1.2252560648528688, 0.0)
    viewCenter53 = NXOpen.Point3d(12.957082885819368, 1.2252560648529276, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-16.196353607274375, -1.5315700810660997, 0.0)
    viewCenter54 = NXOpen.Point3d(16.196353607274226, 1.5315700810661599, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-20.245442009092944, -1.9144626013326327, 0.0)
    viewCenter55 = NXOpen.Point3d(20.245442009092805, 1.9144626013326826, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-25.306802511366183, -2.3930782516657909, 0.0)
    viewCenter56 = NXOpen.Point3d(25.306802511366037, 2.3930782516658535, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(-20.245442009092944, -1.9144626013326327, 0.0)
    viewCenter57 = NXOpen.Point3d(20.245442009092805, 1.9144626013326911, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-16.196353607274368, -1.5315700810660995, 0.0)
    viewCenter58 = NXOpen.Point3d(16.196353607274229, 1.5315700810661594, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-12.957082885819517, -1.2252560648528688, 0.0)
    viewCenter59 = NXOpen.Point3d(12.957082885819368, 1.2252560648529329, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(-10.365666308655632, -0.9802048518822909, 0.0)
    viewCenter60 = NXOpen.Point3d(10.365666308655486, 0.98020485188235507, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-8.29253304692452, -0.78416388150582605, 0.0)
    viewCenter61 = NXOpen.Point3d(8.2925330469243672, 0.78416388150588756, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(-6.6340264375396325, -0.62733110520465263, 0.0)
    viewCenter62 = NXOpen.Point3d(6.6340264375394797, 0.62733110520471547, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(-5.4075941268644687, -0.22583919787365445, 0.0)
    viewCenter63 = NXOpen.Point3d(5.4075941268643195, 0.22583919787372012, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(-4.3461498968581393, -0.16059676293236796, 0.0)
    viewCenter64 = NXOpen.Point3d(4.3461498968579928, 0.160596762932431, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(-3.4769199174865264, -0.12847741034588878, 0.0)
    viewCenter65 = NXOpen.Point3d(3.4769199174863781, 0.12847741034595042, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(-2.7815359339892383, -0.10278192827670428, 0.0)
    viewCenter66 = NXOpen.Point3d(2.7815359339890882, 0.10278192827676702, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(-2.2252287471914047, -0.082225542621357145, 0.0)
    viewCenter67 = NXOpen.Point3d(2.2252287471912542, 0.082225542621419886, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(-1.870631094636666, 0.032890217048586967, 0.0)
    viewCenter68 = NXOpen.Point3d(1.8706310946365154, -0.032890217048523865, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-1.4965048757093484, 0.026312173638875877, 0.0)
    viewCenter69 = NXOpen.Point3d(1.496504875709197, -0.026312173638812775, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(-1.1972039005674935, 0.021049738911107126, 0.0)
    viewCenter70 = NXOpen.Point3d(1.1972039005673429, -0.021049738911044252, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-1.1261610317426138, 0.13050838124869935, 0.0)
    viewCenter71 = NXOpen.Point3d(1.1261610317424626, -0.13050838124863692, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(-0.86388128491061378, 0.087566913870105512, 0.0)
    viewCenter72 = NXOpen.Point3d(0.86388128491046223, -0.087566913870042951, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-0.67763319502541763, 0.061970431354237243, 0.0)
    viewCenter73 = NXOpen.Point3d(0.67763319502526631, -0.061970431354175209, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(-0.53348458296237222, 0.043109865289913847, 0.0)
    viewCenter74 = NXOpen.Point3d(0.5334845829622219, -0.043109865289851626, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(-0.426787666369913, 0.03448789223193708, 0.0)
    viewCenter75 = NXOpen.Point3d(0.42678766636976206, -0.034487892231874977, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-0.3414301330959455, 0.027590313785556035, 0.0)
    viewCenter76 = NXOpen.Point3d(0.34143013309579462, -0.027590313785493838, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(-0.27314410647677123, 0.022072251028450892, 0.0)
    viewCenter77 = NXOpen.Point3d(0.27314410647662074, -0.022072251028388817, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-0.21674950509915869, 0.01765780082276695, 0.0)
    viewCenter78 = NXOpen.Point3d(0.21674950509900792, -0.017657800822704892, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-0.27093688137392929, 0.022072251028450892, 0.0)
    viewCenter79 = NXOpen.Point3d(0.27093688137377875, -0.022072251028388817, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-0.3386711017173929, 0.027590313785555921, 0.0)
    viewCenter80 = NXOpen.Point3d(0.3386711017172423, -0.027590313785493963, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-0.42333887714672219, 0.03448789223193708, 0.0)
    viewCenter81 = NXOpen.Point3d(0.42333887714657165, -0.034487892231875122, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(-0.52917359643338424, 0.043109865289913452, 0.0)
    viewCenter82 = NXOpen.Point3d(0.52917359643323314, -0.043109865289851605, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(-0.6614669955417114, 0.053887331612384286, 0.0)
    viewCenter83 = NXOpen.Point3d(0.66146699554156008, -0.053887331612322252, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(-0.82683374442712032, 0.067359164515472719, 0.0)
    viewCenter84 = NXOpen.Point3d(0.82683374442696944, -0.06735916451541045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(-1.0335421805338814, 0.084198955644333176, 0.0)
    viewCenter85 = NXOpen.Point3d(1.0335421805337301, -0.084198955644270768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(-1.2919277256673325, 0.10524869455540867, 0.0)
    viewCenter86 = NXOpen.Point3d(1.2919277256671815, -0.10524869455534672, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(-1.6149096570841472, 0.13156086819425281, 0.0)
    viewCenter87 = NXOpen.Point3d(1.6149096570839956, -0.13156086819419086, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(-2.0186370713551653, 0.1644510852428081, 0.0)
    viewCenter88 = NXOpen.Point3d(2.018637071355013, -0.16445108524274646, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(-2.5232963391939367, 0.20556385655350298, 0.0)
    viewCenter89 = NXOpen.Point3d(2.5232963391937853, -0.20556385655344023, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(-3.1541204239924032, 0.25695482069187087, 0.0)
    viewCenter90 = NXOpen.Point3d(3.1541204239922531, -0.25695482069180814, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(-3.9426505299904813, 0.32119352586483019, 0.0)
    viewCenter91 = NXOpen.Point3d(3.9426505299903329, -0.32119352586476857, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(-4.9283131624880836, 0.40149190733103068, 0.0)
    viewCenter92 = NXOpen.Point3d(4.9283131624879353, -0.40149190733096768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint92, viewCenter92)
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId88, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension3)
    
    theSession.UpdateManager.LogForUpdate(horizontalDimension1)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension4)
    
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    center5 = NXOpen.Point3d(-0.040538777092412603, 0.0, 0.82861946813126153)
    arc2.SetParameters(9.9999999999962466, center5, ( 273.37375929846331 * math.pi/180.0 ), ( 446.62624070153669 * math.pi/180.0 ))
    
    startPoint9 = NXOpen.Point3d(0.54795309158318806, 0.0, -9.1540493794479083)
    endPoint9 = NXOpen.Point3d(0.54795309158318806, 0.0, 10.811288315710431)
    line5.SetEndpoints(startPoint9, endPoint9)
    
    sketchHelpedDimensionalConstraint4.Refresh()
    
    helpPoint1_3 = NXOpen.Point3d(10.636973302010345, 0.0, 0.039208194075293079)
    helpPoint2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint5.SetHelpPoints(True, False, helpPoint1_3, helpPoint2_3)
    
    sketchHelpedDimensionalConstraint6.Refresh()
    
    nErrs10 = theSession.UpdateManager.DoUpdate(markId88)
    
    geoms9 = [NXOpen.SmartObject.Null] * 2 
    geoms9[0] = arc2
    geoms9[1] = line5
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms9)
    
    geoms10 = [NXOpen.SmartObject.Null] * 2 
    geoms10[0] = arc2
    geoms10[1] = line5
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms10)
    
    geoms11 = [NXOpen.SmartObject.Null] * 2 
    geoms11[0] = arc2
    geoms11[1] = line5
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms11)
    
    scaleAboutPoint93 = NXOpen.Point3d(-6.4866036278165247, 0.4767716399555928, 0.0)
    viewCenter93 = NXOpen.Point3d(6.4866036278163755, -0.47677163995552935, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(-5.1892829022532334, 0.38141731196448125, 0.0)
    viewCenter94 = NXOpen.Point3d(5.1892829022530842, -0.38141731196441819, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-4.1514263218026031, 0.30513384957159057, 0.0)
    viewCenter95 = NXOpen.Point3d(4.1514263218024521, -0.30513384957152895, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-3.3211410574420959, 0.24410707965727918, 0.0)
    viewCenter96 = NXOpen.Point3d(3.321141057441948, -0.24410707965721642, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(-2.6569128459536926, 0.19528566372582962, 0.0)
    viewCenter97 = NXOpen.Point3d(2.656912845953542, -0.19528566372576686, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(-3.3211410574420959, 0.24410707965727918, 0.0)
    viewCenter98 = NXOpen.Point3d(3.321141057441948, -0.24410707965721642, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-4.1514263218026022, 0.3051338495715919, 0.0)
    viewCenter99 = NXOpen.Point3d(4.1514263218024512, -0.30513384957152889, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(-5.1892829022532316, 0.38141731196448114, 0.0)
    viewCenter100 = NXOpen.Point3d(5.1892829022530851, -0.38141731196441814, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(-6.4866036278165193, 0.47677163995559491, 0.0)
    viewCenter101 = NXOpen.Point3d(6.4866036278163763, -0.47677163995553146, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(-8.1082545347706372, 0.59596454994448544, 0.0)
    viewCenter102 = NXOpen.Point3d(8.1082545347704844, -0.59596454994442249, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint102, viewCenter102)
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId90, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension3)
    
    theSession.UpdateManager.LogForUpdate(horizontalDimension1)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension4)
    
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    center6 = NXOpen.Point3d(-0.55024530007122086, 0.0, 0.0052473925501210772)
    arc2.SetParameters(9.9999999999962466, center6, ( 273.37375929846331 * math.pi/180.0 ), ( 446.62624070153669 * math.pi/180.0 ))
    
    startPoint10 = NXOpen.Point3d(0.038246568604379805, 0.0, -9.9774214550290488)
    endPoint10 = NXOpen.Point3d(0.038246568604379805, 0.0, 9.9879162401292909)
    line5.SetEndpoints(startPoint10, endPoint10)
    
    sketchHelpedDimensionalConstraint4.Refresh()
    
    helpPoint1_4 = NXOpen.Point3d(9.9594612229038333, 0.0, 0.82861946813126153)
    helpPoint2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint5.SetHelpPoints(True, False, helpPoint1_4, helpPoint2_4)
    
    sketchHelpedDimensionalConstraint6.Refresh()
    
    nErrs11 = theSession.UpdateManager.DoUpdate(markId90)
    
    geoms12 = [NXOpen.SmartObject.Null] * 2 
    geoms12[0] = arc2
    geoms12[1] = line5
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms12)
    
    geoms13 = [NXOpen.SmartObject.Null] * 2 
    geoms13[0] = arc2
    geoms13[1] = line5
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms13)
    
    geoms14 = [NXOpen.SmartObject.Null] * 2 
    geoms14[0] = arc2
    geoms14[1] = line5
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms14)
    
    scaleAboutPoint103 = NXOpen.Point3d(-3.3523005934376142, 6.6261847987245215, 0.0)
    viewCenter103 = NXOpen.Point3d(3.3523005934374637, -6.6261847987244602, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(-2.5877408089694058, 5.3009478389796252, 0.0)
    viewCenter104 = NXOpen.Point3d(2.5877408089692526, -5.3009478389795621, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(-2.0701926471755376, 4.2407582711837071, 0.0)
    viewCenter105 = NXOpen.Point3d(2.0701926471753889, -4.240758271183644, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(-2.5877408089694058, 5.3009478389796252, 0.0)
    viewCenter106 = NXOpen.Point3d(2.5877408089692526, -5.3009478389795621, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(-3.2346760112117368, 6.6261847987245215, 0.0)
    viewCenter107 = NXOpen.Point3d(3.2346760112115862, -6.6261847987244602, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint107, viewCenter107)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId54, None)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint2 = [None] * 3 
    starthelperpoint2[0] = 0.0
    starthelperpoint2[1] = 0.0
    starthelperpoint2[2] = 0.0
    revolveBuilder1.SetStartLimitHelperPoint(starthelperpoint2)
    
    endhelperpoint2 = [None] * 3 
    endhelperpoint2[0] = 0.0
    endhelperpoint2[1] = 0.0
    endhelperpoint2[2] = 0.0
    revolveBuilder1.SetEndLimitHelperPoint(endhelperpoint2)
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 2 
    curves1[0] = line5
    curves1[1] = arc2
    seedPoint1 = NXOpen.Point3d(3.1754159457112645, 0.0, 0.0052473925501200702)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch7, curves1, seedPoint1, 0.01)
    
    section3.AllowSelfIntersection(False)
    
    rules3 = [None] * 1 
    rules3[0] = regionBoundaryRule1
    helpPoint3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section3.AddToSection(rules3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId92, None)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    refs1 = section3.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression29)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    revolveBuilder1.Section = section3
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    direction7 = workPart.Directions.CreateDirection(line5, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1.Point = NXOpen.Point.Null
    
    axis1.Evaluate()
    
    revolveBuilder1.Axis = axis1
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    theSession.DeleteUndoMark(markId93, None)
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    revolveBuilder1.ParentFeatureInternal = True
    
    feature6 = revolveBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId94, None)
    
    theSession.SetUndoMarkName(markId53, "Revolve")
    
    expression32 = revolveBuilder1.Limits.StartExtend.Value
    expression33 = revolveBuilder1.Limits.EndExtend.Value
    revolveBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression30)
    
    workPart.Expressions.Delete(expression31)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.35227030665085246
    rotMatrix10.Xy = 0.76960735398737112
    rotMatrix10.Xz = 0.53255060955806643
    rotMatrix10.Yx = -0.40078512648068954
    rotMatrix10.Yy = -0.39015939457311172
    rotMatrix10.Yz = 0.8289432605541821
    rotMatrix10.Zx = 0.84574045276548537
    rotMatrix10.Zy = -0.50545046000067828
    rotMatrix10.Zz = 0.17100561113931773
    translation10 = NXOpen.Point3d(-29.919812428629069, -1.2490736727378824, 20.446710507361288)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 2.211238459495894)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = -0.49545425221432066
    rotMatrix11.Xy = -0.82392117299622836
    rotMatrix11.Xz = 0.27509813640092906
    rotMatrix11.Yx = 0.61758999559549943
    rotMatrix11.Yy = -0.11142468751581652
    rotMatrix11.Yz = 0.77856736147384797
    rotMatrix11.Zx = -0.61082540983745404
    rotMatrix11.Zy = 0.55564236672568312
    rotMatrix11.Zz = 0.56405130883314447
    translation11 = NXOpen.Point3d(-26.666327507545066, -0.65775558095377029, 15.584910732398754)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 2.211238459495894)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()