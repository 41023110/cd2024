# NX 1872
# Journal created by Reader on Wed Jun 19 20:00:48 2024 台北標準時間

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
    
    rotMatrix1.Xx = 0.66866008249028697
    rotMatrix1.Xy = 0.7402508043654209
    rotMatrix1.Xz = 0.070160107756659665
    rotMatrix1.Yx = -0.53676557073147835
    rotMatrix1.Yy = 0.41524126432066388
    rotMatrix1.Yz = 0.73447764736762589
    rotMatrix1.Zx = 0.51456429740255738
    rotMatrix1.Zy = -0.52877541455869403
    rotMatrix1.Zz = 0.67499640354366852
    translation1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.90572327300951838)
    
    scaleAboutPoint1 = NXOpen.Point3d(2.9212381001779915, -8.7637143005340246, 0.0)
    viewCenter1 = NXOpen.Point3d(-2.9212381001779915, 8.7637143005340246, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
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
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XY plane")
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
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom3 = [NXOpen.NXObject.Null] * 1 
    geom3[0] = datumPlane1
    plane3.SetGeometry(geom3)
    
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
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId9, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 14.542148016713169, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point2 = datumCsys2.FindObject("POINT 1")
    geom2_1.Geometry = point2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = arc1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(0.0, 4.1403374648192246, 0.0)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension1 = sketchDimensionalConstraint1.AssociatedDimension
    
    expression5 = sketchDimensionalConstraint1.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
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
    
    point1_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    point1_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
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
    point3 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point3
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
    
    point4 = NXOpen.Point3d(19.718357176201494, 28.48207147673558, 0.0)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point4)
    
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
    
    expression6 = workPart.Expressions.FindObject("p0")
    expression6.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId12, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.68765632068287463)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId12, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder2.Destroy()
    
    theSession.UndoToMark(markId14, None)
    
    theSession.DeleteUndoMark(markId14, None)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    sketch2 = theSession.ActiveSketch
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("35")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId16, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(4.7867912846610627, -8.7637802851903448, 0.0)
    section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId18, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId17, None)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("50")
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId19, None)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId20, None)
    
    theSession.SetUndoMarkName(markId16, "Extrude")
    
    expression9 = extrudeBuilder1.Limits.StartExtend.Value
    expression10 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression7)
    
    workPart.Expressions.Delete(expression8)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.11548384447242668
    rotMatrix2.Xy = 0.98740053630586655
    rotMatrix2.Xz = 0.10818346716920067
    rotMatrix2.Yx = 0.023396413057140589
    rotMatrix2.Yy = -0.11158586954075148
    rotMatrix2.Yz = 0.99347934129245619
    rotMatrix2.Zx = 0.99303378065497938
    rotMatrix2.Zy = -0.11219970865254025
    rotMatrix2.Zz = -0.035987996003619252
    translation2 = NXOpen.Point3d(-0.22027446026902187, -8.6659709232542621, 17.774609988682194)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.72457861840761473)
    
    scaleAboutPoint2 = NXOpen.Point3d(54.773214378337592, 21.178976226290555, 0.0)
    viewCenter2 = NXOpen.Point3d(-54.773214378337713, -21.178976226290555, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(57.96831855040724, 26.930163736015995, 0.0)
    viewCenter3 = NXOpen.Point3d(-57.968318550407396, -26.930163736015995, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(67.325409340039897, 34.233258986461031, 0.0)
    viewCenter4 = NXOpen.Point3d(-67.325409340040096, -34.233258986461031, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(83.443568779498776, 42.791573733076298, 0.0)
    viewCenter5 = NXOpen.Point3d(-83.443568779498847, -42.791573733076298, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(66.754855023599021, 34.233258986460989, 0.0)
    viewCenter6 = NXOpen.Point3d(-66.754855023599021, -34.233258986461038, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(53.403884018879225, 27.386607189168792, 0.0)
    viewCenter7 = NXOpen.Point3d(-53.403884018879225, -27.38660718916887, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(42.723107215103376, 21.909285751335002, 0.0)
    viewCenter8 = NXOpen.Point3d(-42.723107215103376, -21.90928575133513, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(34.178485772082702, 17.527428601068003, 0.0)
    viewCenter9 = NXOpen.Point3d(-34.178485772082702, -17.527428601068127, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrude1 = feature2
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(extrude1)
    
    section1.PrepareMappingData()
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId22, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("70")
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId23, None)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature3 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId24, None)
    
    theSession.SetUndoMarkName(markId22, "Extrude")
    
    section1.CleanMappingData()
    
    expression13 = extrudeBuilder2.Limits.StartExtend.Value
    expression14 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression11)
    
    workPart.Expressions.Delete(expression12)
    
    theSession.DeleteUndoMark(markId22, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId21)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId25, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    extrude2 = feature3
    edge1 = extrude2.FindObject("EDGE * 130 * 140 {(-4.9999999999994,-8.6602540378433,70)(9.9999999999987,0,70)(-4.9999999999994,8.6602540378433,70) EXTRUDE(2)}")
    seedEdges1[0] = edge1
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules2 = [None] * 1 
    rules2[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules2, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId26, None)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    csIndex1 = edgeBlendBuilder1.AddChainset(scCollector1, "10")
    
    feature4 = edgeBlendBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.SetUndoMarkName(markId25, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
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
        
    edgeBlendBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression15)
    
    workPart.Expressions.Delete(expression16)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.9597496590692447
    rotMatrix3.Xy = -0.11999183571172319
    rotMatrix3.Xz = -0.25393414752450189
    rotMatrix3.Yx = -0.25137556124312976
    rotMatrix3.Yy = -0.77024774243612504
    rotMatrix3.Yz = -0.5861132505597797
    rotMatrix3.Zx = -0.12526339898855635
    rotMatrix3.Zy = 0.62635483125348412
    rotMatrix3.Zz = -0.7694080232485544
    translation3 = NXOpen.Point3d(1.3697974593742988, 38.435738676544034, 43.444310942254937)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 1.1321540912618979)
    
    scaleAboutPoint10 = NXOpen.Point3d(7.712068584469904, 30.614575289865478, 0.0)
    viewCenter10 = NXOpen.Point3d(-7.7120685844699839, -30.614575289865599, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(6.1696548675759235, 24.491660231892382, 0.0)
    viewCenter11 = NXOpen.Point3d(-6.1696548675759866, -24.491660231892478, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(4.9357238940607377, 19.593328185513904, 0.0)
    viewCenter12 = NXOpen.Point3d(-4.9357238940607893, -19.593328185513982, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane5
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId28, "Create Sketch Dialog")
    
    edge2 = extrude2.FindObject("EDGE * 120 * 140 {(-4.9999999999994,-8.6602540378433,0)(9.9999999999987,0,0)(-4.9999999999994,8.6602540378433,0) EXTRUDE(2)}")
    point5 = workPart.Points.CreatePoint(edge2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction3 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude2.FindObject("FACE 120 {(0,0,0) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point5, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane6.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom4 = [NXOpen.NXObject.Null] * 1 
    geom4[0] = face1
    plane6.SetGeometry(geom4)
    
    plane6.SetFlip(False)
    
    plane6.SetExpression(None)
    
    plane6.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane6.Evaluate()
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane7.SynchronizeToPlane(plane6)
    
    point6 = workPart.Points.CreatePoint(edge2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane7.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom5 = [NXOpen.NXObject.Null] * 1 
    geom5[0] = face1
    plane7.SetGeometry(geom5)
    
    plane7.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane7.Evaluate()
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId29, None)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
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
    
    nXObject4 = sketchInPlaceBuilder2.Commit()
    
    sketch3 = nXObject4
    feature5 = sketch3.Feature
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId31)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId30, None)
    
    theSession.SetUndoMarkName(markId28, "Create Sketch")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression20)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point6)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression19)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane5.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression22)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression21)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane7.DestroyPlane()
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch4 = theSession.ActiveSketch
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    objects1[0] = sketch4
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    objects2[0] = sketch4
    theSession.DisplayManager.BlankObjects(objects2)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = sketch4
    nErrs4 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs5 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId35, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    revolveBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    revolveBuilder1.Offset.StartOffset.SetFormula("0")
    
    revolveBuilder1.Offset.EndOffset.SetFormula("5")
    
    revolveBuilder1.Tolerance = 0.01
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder1.Section = section2
    
    smartVolumeProfileBuilder2 = revolveBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId37, "Revolve Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
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
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    point7 = workPart.Points.CreatePoint(edge2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction4 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction4, point7, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem3
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature6 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem3
    
    sketchInPlaceBuilder3.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject5 = sketchInPlaceBuilder3.Commit()
    
    sketchInPlaceBuilder3.Destroy()
    
    sketch5 = nXObject5
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId39, None, True)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId42, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 17.607115818094861, ( 272.59032439167669 * math.pi/180.0 ), ( 447.40967560832337 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = arc2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(7.6993924226533279, -2.3198418874881837, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateRadialDimension(dimObject1_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension2 = sketchDimensionalConstraint2.AssociatedDimension
    
    expression23 = sketchDimensionalConstraint2.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId43, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint1 = NXOpen.Point3d(-4.3298697960381105e-15, 17.948086887493726, 0.0)
    endPoint1 = NXOpen.Point3d(1.3446458164812679e-14, -17.230163411993903, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line1
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = arc2
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom6.Geometry = line1
    geom6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateVerticalConstraint(geom6)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line1
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = arc2
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId44, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint2 = NXOpen.Point3d(1.3446458164812679e-14, -17.230163411993903, 0.0)
    endPoint2 = NXOpen.Point3d(-35.178250299487615, -17.230163411993939, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = line2
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line2
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_5.Geometry = line1
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_5.SplineDefiningPointIndex = 0
    try:
        # Constraint already exists.
        sketchGeometricConstraint6 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(910023)
        
    geom7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom7.Geometry = line2
    geom7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreateHorizontalConstraint(geom7)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = line2
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line2
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(-17.589125149743797, -21.300280753409812, 0.0)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_3, dimObject2_1, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint3
    dimension3 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression24 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.ActiveSketch.Update()
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.DeleteUndoMark(markId47, "Curve")
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects4 = [NXOpen.NXObject.Null] * 1 
    objects4[0] = line2
    errorList1 = theSession.ActiveSketch.DeleteObjects(objects4)
    
    errorList1.Dispose()
    theSession.DeleteUndoMark(markId48, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines17 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines20)
    
    theSession.SetUndoMarkName(markId50, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    point1_4 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    point1_5 = NXOpen.Point3d(-0.79574110014246557, 1.3589617377499117, -0.0)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(-0.79574110014246557, -0.6410382622500882, 0.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    point1_7 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    point1_8 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    point1_9 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    point1_10 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    point1_11 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    point1_14 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    point1_15 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
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
    
    point1_18 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    point1_19 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    point1_20 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    point1_21 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    point1_22 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    point1_24 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    point1_25 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    point1_27 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    point1_28 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    point1_29 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    point1_30 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    point1_32 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    point1_33 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    point1_34 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    point1_35 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    point1_36 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    point1_37 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_37 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_37, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_37)
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    point1_38 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_38, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_38)
    
    point1_39 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_39 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_39, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_39)
    
    point1_40 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_40 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_40, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_40)
    
    point1_41 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_41, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_41)
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    point1_42 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_42 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_42, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_42)
    
    point1_43 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_43 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_43, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_43)
    
    point1_44 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_44 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_44, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_44)
    
    point1_45 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_45 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_45, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_45)
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    point1_46 = NXOpen.Point3d(12.281500853977827, -11.430706209448699, 0.0)
    point2_46 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_46, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_46)
    
    point1_47 = NXOpen.Point3d(-0.79574110014246557, 0.35896173774991175, -0.0)
    point2_47 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_47, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_47)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point8 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point8
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
    sketchRapidDimensionBuilder3.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point9 = NXOpen.Point3d(26.024725986865825, -10.649198219912883, 0.0)
    sketchRapidDimensionBuilder3.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point9)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.TextCentered = False
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject6 = sketchRapidDimensionBuilder3.Commit()
    
    theSession.DeleteUndoMark(markId51, None)
    
    theSession.SetUndoMarkName(markId50, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId50, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines21 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines24)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId52, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    expression25 = workPart.Expressions.FindObject("p15")
    expression25.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId52, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.56795219065497049)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId53, None)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId52, "Edit Driving Value")
    
    verticalDimension1 = nXObject6
    point10 = NXOpen.Point3d(27.72800630841893, -4.1878869404151562, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(verticalDimension1, workPart.ModelingViews.WorkView, point10)
    
    point1_48 = NXOpen.Point3d(-0.45194290102010959, 0.2038731053163774, -0.0)
    point2_48 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, NXOpen.View.Null, point1_48, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_48)
    
    point1_49 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_49 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_49, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_49)
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Destroy()
    
    theSession.UndoToMark(markId54, None)
    
    theSession.DeleteUndoMark(markId54, None)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchLinearDimensionBuilder1 = workPart.Sketches.CreateLinearDimensionBuilder(verticalDimension1)
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Inferred
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId55, "Linear Dimension Dialog")
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits165 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Style.OrdinateStyle.DoglegCreationOption = NXOpen.Annotations.OrdinateDoglegCreationOption.No
    
    dimensionlinearunits167 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchLinearDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits171 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits173 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits181 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    # ----------------------------------------------
    #   Dialog Begin Linear Dimension
    # ----------------------------------------------
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    theSession.DeleteUndoMark(markId56, None)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionValue.SetFormula("15")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionValue.SetFormula("15")
    
    sketchLinearDimensionBuilder1.Driving.ExpressionMode = NXOpen.Annotations.DrivingValueBuilder.DrivingExpressionMode.KeepExpression
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    nXObject7 = sketchLinearDimensionBuilder1.Commit()
    
    point1_50 = NXOpen.Point3d(-0.45194290102011236, 15.203873105316372, -0.0)
    point2_50 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, NXOpen.View.Null, point1_50, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_50)
    
    point1_51 = NXOpen.Point3d(-0.45194290102010959, 0.2038731053163774, -0.0)
    point2_51 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, NXOpen.View.Null, point1_51, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_51)
    
    theSession.SetUndoMarkName(markId57, "Linear Dimension - =")
    
    theSession.SetUndoMarkVisibility(markId57, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId55, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Linear Dimension")
    
    nXObject8 = sketchLinearDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId59, None)
    
    theSession.SetUndoMarkName(markId55, "Linear Dimension")
    
    expression26 = sketchLinearDimensionBuilder1.Driving.ExpressionValue
    sketchLinearDimensionBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId58, None)
    
    theSession.SetUndoMarkVisibility(markId55, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.DeleteUndoMark(markId57, None)
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    geom1Help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help1.Point.X = -0.15349797599824455
    geom1Help1.Point.Y = 9.9988218491649938
    geom1Help1.Point.Z = 0.0
    geom1Help1.Parameter = 0.0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = arc1
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    geom2Help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help1.Point.X = -0.15349797599824455
    geom2Help1.Point.Y = 9.9988218491649938
    geom2Help1.Point.Z = 0.0
    geom2Help1.Parameter = 0.0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreateNormalConstraint(conGeom1_1, geom1Help1, conGeom2_1, geom2Help1)
    
    theSession.SetUndoMarkVisibility(markId61, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    parallelDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 4 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension1)
    
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    perpendicularDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    startPoint3 = NXOpen.Point3d(0.0, 9.6629670661714151, 0.0)
    endPoint3 = NXOpen.Point3d(0.0, -9.9731443310383909, 0.0)
    line1.SetEndpoints(startPoint3, endPoint3)
    
    center3 = NXOpen.Point3d(-11.340448946099611, -0.15508863243348792, 0.0)
    arc2.SetParameters(15.0, center3, ( 319.11544430909686 * math.pi/180.0 ), ( 400.88455569090308 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint2 = theSession.ActiveSketch.FindObject("ENTITY 243 7 1")
    sketchHelpedDimensionalConstraint2.Refresh()
    
    sketchHelpedDimensionalConstraint3 = theSession.ActiveSketch.FindObject("ENTITY 243 6 1")
    sketchHelpedDimensionalConstraint3.Refresh()
    
    sketchHelpedGeometricConstraint1 = sketchGeometricConstraint8
    helpPoint1_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    helpPoint2_1 = NXOpen.Point3d(1.8318679906315083e-15, 9.9999999999987406, 0.0)
    sketchHelpedGeometricConstraint1.SetHelpPoints(False, True, helpPoint1_1, helpPoint2_1)
    
    sketchHelpedDimensionalConstraint4 = theSession.ActiveSketch.FindObject("DimensionalConstraint p15")
    helpPoint1_2 = NXOpen.Point3d(-11.340448946099615, -15.155088632433488, 0.0)
    helpPoint2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint4.SetHelpPoints(True, False, helpPoint1_2, helpPoint2_2)
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId61)
    
    geoms1 = [NXOpen.SmartObject.Null] * 2 
    geoms1[0] = line1
    geoms1[1] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 2 
    geoms2[0] = line1
    geoms2[1] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms2)
    
    geoms3 = [NXOpen.SmartObject.Null] * 2 
    geoms3[0] = line1
    geoms3[1] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms3)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId63, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    parallelDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    startPoint4 = NXOpen.Point3d(0.0, 15.148341561035757, 0.0)
    endPoint4 = NXOpen.Point3d(0.0, -14.740595350402982, 0.0)
    line1.SetEndpoints(startPoint4, endPoint4)
    
    center4 = NXOpen.Point3d(-1.2895202891031659, 0.20387310531638825, -0.0)
    arc2.SetParameters(14.999999999999998, center4, ( 274.93169205807743 * math.pi/180.0 ), ( 445.06830794192257 * math.pi/180.0 ))
    
    helpPoint1_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    helpPoint2_3 = NXOpen.Point3d(1.8318679906315083e-15, 9.9999999999987406, 0.0)
    sketchHelpedGeometricConstraint1.SetHelpPoints(False, True, helpPoint1_3, helpPoint2_3)
    
    helpPoint1_4 = NXOpen.Point3d(-1.2895202891031685, -14.79612689468361, 0.0)
    helpPoint2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint4.SetHelpPoints(True, False, helpPoint1_4, helpPoint2_4)
    
    sketchHelpedDimensionalConstraint3.Refresh()
    
    nErrs7 = theSession.UpdateManager.DoUpdate(markId63)
    
    geoms4 = [NXOpen.SmartObject.Null] * 2 
    geoms4[0] = line1
    geoms4[1] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms4)
    
    geoms5 = [NXOpen.SmartObject.Null] * 2 
    geoms5[0] = line1
    geoms5[1] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms5)
    
    geoms6 = [NXOpen.SmartObject.Null] * 2 
    geoms6[0] = line1
    geoms6[1] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms6)
    
    scaleAboutPoint13 = NXOpen.Point3d(14.178988641119975, 2.273424339082498, 0.0)
    viewCenter13 = NXOpen.Point3d(-14.178988641120018, -2.2734243390825815, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(17.723735801399997, 2.8417804238531357, 0.0)
    viewCenter14 = NXOpen.Point3d(-17.723735801400011, -2.8417804238532267, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(22.154669751749999, 3.5522255298164196, 0.0)
    viewCenter15 = NXOpen.Point3d(-22.154669751749999, -3.5522255298165337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(27.69333718968749, 4.4402819122705237, 0.0)
    viewCenter16 = NXOpen.Point3d(-27.69333718968749, -4.4402819122706463, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(34.616671487109393, 5.5503523903381806, 0.0)
    viewCenter17 = NXOpen.Point3d(-34.616671487109393, -5.5503523903383076, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(27.69333718968749, 4.4402819122705237, 0.0)
    viewCenter18 = NXOpen.Point3d(-27.69333718968749, -4.4402819122706463, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(22.154669751749999, 3.5522255298164196, 0.0)
    viewCenter19 = NXOpen.Point3d(-22.154669751749999, -3.5522255298165337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(17.723735801399972, 2.8417804238531224, 0.0)
    viewCenter20 = NXOpen.Point3d(-17.723735801400021, -2.84178042385324, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(14.17898864112, 2.2734243390824775, 0.0)
    viewCenter21 = NXOpen.Point3d(-14.17898864112, -2.2734243390826028, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(11.343190912896002, 1.8187394712659739, 0.0)
    viewCenter22 = NXOpen.Point3d(-11.343190912896002, -1.8187394712660991, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(9.0745527303168014, 1.4549915770127593, 0.0)
    viewCenter23 = NXOpen.Point3d(-9.0745527303168014, -1.4549915770128927, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(7.2596421842534413, 1.1639932616101967, 0.0)
    viewCenter24 = NXOpen.Point3d(-7.2596421842534413, -1.1639932616103248, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(5.8077137474027536, 0.93119460928814457, 0.0)
    viewCenter25 = NXOpen.Point3d(-5.8077137474027536, -0.9311946092882728, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId65, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    startPoint5 = NXOpen.Point3d(0.0, 15.422798919562807, 0.0)
    endPoint5 = NXOpen.Point3d(0.0, -14.466137991875932, 0.0)
    line1.SetEndpoints(startPoint5, endPoint5)
    
    center5 = NXOpen.Point3d(-1.2895202891031814, 0.47833046384343714, -0.0)
    arc2.SetParameters(15.000000000000002, center5, ( 274.93169205807743 * math.pi/180.0 ), ( 445.06830794192257 * math.pi/180.0 ))
    
    helpPoint1_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    helpPoint2_5 = NXOpen.Point3d(1.8318679906315083e-15, 9.9999999999987406, 0.0)
    sketchHelpedGeometricConstraint1.SetHelpPoints(False, True, helpPoint1_5, helpPoint2_5)
    
    helpPoint1_6 = NXOpen.Point3d(-1.2895202891031841, -14.521669536156566, 0.0)
    helpPoint2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint4.SetHelpPoints(True, False, helpPoint1_6, helpPoint2_6)
    
    sketchHelpedDimensionalConstraint3.Refresh()
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId65)
    
    geoms7 = [NXOpen.SmartObject.Null] * 2 
    geoms7[0] = line1
    geoms7[1] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms7)
    
    geoms8 = [NXOpen.SmartObject.Null] * 2 
    geoms8[0] = line1
    geoms8[1] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms8)
    
    geoms9 = [NXOpen.SmartObject.Null] * 2 
    geoms9[0] = line1
    geoms9[1] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms9)
    
    scaleAboutPoint26 = NXOpen.Point3d(-5.8616250142562913, -0.54891471705416328, 0.0)
    viewCenter26 = NXOpen.Point3d(5.8616250142562913, 0.54891471705403339, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-4.6893000114050336, -0.43913177364334166, 0.0)
    viewCenter27 = NXOpen.Point3d(4.6893000114050336, 0.4391317736432131, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-3.7514400091240265, -0.35130541891468864, 0.0)
    viewCenter28 = NXOpen.Point3d(3.7514400091240265, 0.35130541891455952, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-3.0011520072992215, -0.28104433513176319, 0.0)
    viewCenter29 = NXOpen.Point3d(3.0011520072992215, 0.28104433513163535, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-3.7514400091240265, -0.35130541891468642, 0.0)
    viewCenter30 = NXOpen.Point3d(3.7514400091240265, 0.35130541891455952, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(-4.6893000114050318, -0.43913177364334149, 0.0)
    viewCenter31 = NXOpen.Point3d(4.6893000114050318, 0.43913177364321565, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-5.8616250142562896, -0.54891471705416317, 0.0)
    viewCenter32 = NXOpen.Point3d(5.861625014256286, 0.54891471705403327, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-7.3270312678203613, -0.68614339631768684, 0.0)
    viewCenter33 = NXOpen.Point3d(7.3270312678203613, 0.68614339631755861, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint33, viewCenter33)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines29 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines32)
    
    theSession.SetUndoMarkName(markId66, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    point1_52 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_52 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_52, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_52)
    
    point1_53 = NXOpen.Point3d(-1.2895202891031814, 0.47833046384343714, -0.0)
    point2_53 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_53, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_53)
    
    point1_54 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_54 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_54, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_54)
    
    point1_55 = NXOpen.Point3d(-1.2895202891031814, 0.47833046384343714, -0.0)
    point2_55 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_55, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_55)
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    point1_56 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_56 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_56, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_56)
    
    point1_57 = NXOpen.Point3d(-1.2895202891031814, 0.47833046384343714, -0.0)
    point2_57 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_57, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_57)
    
    point1_58 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_58 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_58, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_58)
    
    point1_59 = NXOpen.Point3d(-1.2895202891031814, 0.47833046384343714, -0.0)
    point2_59 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_59, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_59)
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Destroy()
    
    theSession.UndoToMark(markId66, None)
    
    theSession.DeleteUndoMark(markId66, None)
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = arc2
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys3 = feature6
    point11 = datumCsys3.FindObject("POINT 1")
    geom2_6.Geometry = point11
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    theSession.SetUndoMarkVisibility(markId68, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    startPoint6 = NXOpen.Point3d(0.0, 15.0, 0.0)
    endPoint6 = NXOpen.Point3d(0.0, -15.0, 0.0)
    line1.SetEndpoints(startPoint6, endPoint6)
    
    center6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc2.SetParameters(15.0, center6, ( 270.0 * math.pi/180.0 ), ( 450.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint3.Refresh()
    
    helpPoint1_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    helpPoint2_7 = NXOpen.Point3d(1.8318679906315083e-15, 9.9999999999987406, 0.0)
    sketchHelpedGeometricConstraint1.SetHelpPoints(False, True, helpPoint1_7, helpPoint2_7)
    
    helpPoint1_8 = NXOpen.Point3d(-2.6645352591003757e-15, -15.0, 0.0)
    helpPoint2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchHelpedDimensionalConstraint4.SetHelpPoints(True, False, helpPoint1_8, helpPoint2_8)
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId68)
    
    geoms10 = [NXOpen.SmartObject.Null] * 2 
    geoms10[0] = line1
    geoms10[1] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms10)
    
    geoms11 = [NXOpen.SmartObject.Null] * 2 
    geoms11[0] = line1
    geoms11[1] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms11)
    
    geoms12 = [NXOpen.SmartObject.Null] * 2 
    geoms12[0] = line1
    geoms12[1] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms12)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines33 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines36)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines37 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines40)
    
    theSession.SetUndoMarkName(markId69, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point1_60 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_60 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_60, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_60)
    
    point1_61 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_61 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_61, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_61)
    
    point1_62 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_62 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_62, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_62)
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point1_63 = NXOpen.Point3d(4.5924254968025744e-15, -15.0, 0.0)
    point2_63 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, arc2, workPart.ModelingViews.WorkView, point1_63, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_63)
    
    point1_64 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_64 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_64, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_64)
    
    point1_65 = NXOpen.Point3d(4.5924254968025744e-15, -15.0, 0.0)
    point2_65 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, arc2, workPart.ModelingViews.WorkView, point1_65, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_65)
    
    point1_66 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_66 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_66, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_66)
    
    point1_67 = NXOpen.Point3d(4.5924254968025744e-15, -15.0, 0.0)
    point2_67 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, arc2, workPart.ModelingViews.WorkView, point1_67, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_67)
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Destroy()
    
    theSession.UndoToMark(markId69, None)
    
    theSession.DeleteUndoMark(markId69, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines45 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines48)
    
    theSession.SetUndoMarkName(markId70, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits271 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits272 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits273 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits274 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits275 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits276 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits277 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits278 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    point1_68 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_68 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_68, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_68)
    
    point1_69 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_69 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_69, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_69)
    
    point1_70 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_70 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_70, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_70)
    
    dimensionlinearunits279 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits280 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits281 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits282 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits283 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits284 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    point1_71 = NXOpen.Point3d(8.5132458098516466, -12.350086873420908, 0.0)
    point2_71 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_71, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_71)
    
    point1_72 = NXOpen.Point3d(8.5132458098516466, -12.350086873420908, 0.0)
    point2_72 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_72, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_72)
    
    point1_73 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_73 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_73, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_73)
    
    dimensionlinearunits285 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits286 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits287 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits288 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits289 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits290 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits291 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits292 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits293 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits294 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits295 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits296 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point12 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point12
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
    sketchRapidDimensionBuilder7.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point13 = NXOpen.Point3d(9.85873575644864, -19.848497333332478, 0.0)
    sketchRapidDimensionBuilder7.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point13)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.TextCentered = False
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject9 = sketchRapidDimensionBuilder7.Commit()
    
    theSession.DeleteUndoMark(markId71, None)
    
    theSession.SetUndoMarkName(markId70, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId70, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines49 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines49)
    
    lines50 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines50)
    
    lines51 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines51)
    
    lines52 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines52)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId72, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits297 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits298 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits299 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits300 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits301 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits302 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits303 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits304 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits305 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits306 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits307 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits308 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits309 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits310 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits311 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits312 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits313 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits314 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits315 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits316 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Destroy()
    
    theSession.UndoToMark(markId72, None)
    
    theSession.DeleteUndoMark(markId72, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects5 = [NXOpen.NXObject.Null] * 1 
    holeDimension1 = nXObject9
    objects5[0] = holeDimension1
    errorList2 = theSession.ActiveSketch.DeleteObjects(objects5)
    
    errorList2.Dispose()
    theSession.DeleteUndoMark(markId73, None)
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId76, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId78, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId80, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId82, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects6 = [NXOpen.NXObject.Null] * 1 
    verticalDimension2 = nXObject8
    objects6[0] = verticalDimension2
    errorList3 = theSession.ActiveSketch.DeleteObjects(objects6)
    
    errorList3.Dispose()
    theSession.DeleteUndoMark(markId83, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects7 = [NXOpen.NXObject.Null] * 1 
    objects7[0] = verticalDimension2
    errorList4 = theSession.ActiveSketch.DeleteObjects(objects7)
    
    errorList4.Dispose()
    theSession.DeleteUndoMark(markId85, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects8 = [NXOpen.NXObject.Null] * 1 
    radiusDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    objects8[0] = radiusDimension1
    errorList5 = theSession.ActiveSketch.DeleteObjects(objects8)
    
    errorList5.Dispose()
    theSession.DeleteUndoMark(markId87, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects9 = [NXOpen.NXObject.Null] * 1 
    radiusDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    objects9[0] = radiusDimension2
    errorList6 = theSession.ActiveSketch.DeleteObjects(objects9)
    
    errorList6.Dispose()
    theSession.DeleteUndoMark(markId89, None)
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId92, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects10 = [NXOpen.NXObject.Null] * 1 
    radiusDimension3 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    objects10[0] = radiusDimension3
    errorList7 = theSession.ActiveSketch.DeleteObjects(objects10)
    
    errorList7.Dispose()
    theSession.DeleteUndoMark(markId93, None)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId38, None)
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
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
    
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 2 
    curves1[0] = arc2
    curves1[1] = line1
    seedPoint1 = NXOpen.Point3d(4.9999999999999991, 1.8369701987210296e-15, 0.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch5, curves1, seedPoint1, 0.01)
    
    section2.AllowSelfIntersection(False)
    
    rules3 = [None] * 1 
    rules3[0] = regionBoundaryRule1
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section2.AddToSection(rules3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId96, None)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    refs1 = section2.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression27)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    revolveBuilder1.Section = section2
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    direction5 = workPart.Directions.CreateDirection(line1, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1.Point = NXOpen.Point.Null
    
    axis1.Evaluate()
    
    revolveBuilder1.Axis = axis1
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.94797282226285962
    rotMatrix4.Xy = 0.088250862422058943
    rotMatrix4.Xz = -0.30587466964877325
    rotMatrix4.Yx = -0.28828239501412978
    rotMatrix4.Yy = -0.16964819924063129
    rotMatrix4.Yz = -0.94239734147509302
    rotMatrix4.Zx = -0.13505846502867036
    rotMatrix4.Zy = 0.98154534983166519
    rotMatrix4.Zz = -0.13538071224485909
    translation4 = NXOpen.Point3d(-0.54633164348151864, 36.058036201553172, 21.277842722225891)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 2.211238459495894)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.95785526471072713
    rotMatrix5.Xy = 0.14307289114216201
    rotMatrix5.Xz = -0.24908520567501383
    rotMatrix5.Yx = -0.24087630098279658
    rotMatrix5.Yy = -0.072365497852402996
    rotMatrix5.Yz = -0.96785424643662732
    rotMatrix5.Zx = -0.15649888015824689
    rotMatrix5.Zy = 0.98706300839449357
    rotMatrix5.Zz = -0.034852804312097196
    translation5 = NXOpen.Point3d(-2.5586689886827738, 36.830512640128497, 17.812966982403161)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 2.211238459495894)
    
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    theSession.DeleteUndoMark(markId97, None)
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    revolveBuilder1.ParentFeatureInternal = True
    
    feature7 = revolveBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId98, None)
    
    theSession.SetUndoMarkName(markId37, "Revolve")
    
    expression30 = revolveBuilder1.Limits.StartExtend.Value
    expression31 = revolveBuilder1.Limits.EndExtend.Value
    revolveBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression28)
    
    workPart.Expressions.Delete(expression29)
    
    scaleAboutPoint34 = NXOpen.Point3d(-15.555008635827887, 18.30704862524351, 0.0)
    viewCenter34 = NXOpen.Point3d(15.555008635827846, -18.307048625243603, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(-12.44400690866231, 14.645638900194809, 0.0)
    viewCenter35 = NXOpen.Point3d(12.444006908662276, -14.645638900194891, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-9.9552055269298485, 11.716511120155847, 0.0)
    viewCenter36 = NXOpen.Point3d(9.9552055269298219, -11.71651112015592, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-7.964164421543888, 9.3732088961246678, 0.0)
    viewCenter37 = NXOpen.Point3d(7.964164421543857, -9.3732088961247459, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(-6.3713315372351111, 7.4985671168997294, 0.0)
    viewCenter38 = NXOpen.Point3d(6.3713315372350694, -7.4985671168998005, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-7.9641644215438863, 9.3732088961246642, 0.0)
    viewCenter39 = NXOpen.Point3d(7.9641644215438445, -9.3732088961247371, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(-9.9552055269298592, 11.716511120155845, 0.0)
    viewCenter40 = NXOpen.Point3d(9.9552055269298201, -11.716511120155916, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-12.444006908662308, 14.645638900194815, 0.0)
    viewCenter41 = NXOpen.Point3d(12.444006908662258, -14.645638900194879, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(-15.555008635827882, 18.307048625243528, 0.0)
    viewCenter42 = NXOpen.Point3d(15.555008635827832, -18.307048625243588, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(-19.443760794784851, 22.88381078155442, 0.0)
    viewCenter43 = NXOpen.Point3d(19.443760794784801, -22.88381078155447, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(-24.304700993481031, 28.604763476943038, 0.0)
    viewCenter44 = NXOpen.Point3d(24.304700993481031, -28.604763476943084, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(-30.380876241851286, 35.755954346178797, 0.0)
    viewCenter45 = NXOpen.Point3d(30.380876241851286, -35.755954346178832, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(-37.976095302314107, 44.694942932723521, 0.0)
    viewCenter46 = NXOpen.Point3d(37.976095302314107, -44.694942932723521, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(36.880631014747301, 48.930738177981631, 0.0)
    viewCenter47 = NXOpen.Point3d(-36.880631014747301, -48.930738177981631, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(29.504504811797851, 39.144590542385316, 0.0)
    viewCenter48 = NXOpen.Point3d(-29.504504811797851, -39.144590542385316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(23.60360384943824, 31.315672433908251, 0.0)
    viewCenter49 = NXOpen.Point3d(-23.603603849438318, -31.315672433908251, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(29.212381001780066, 39.144590542385316, 0.0)
    viewCenter50 = NXOpen.Point3d(-29.212381001780066, -39.144590542385316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(36.515476252225085, 48.930738177981645, 0.0)
    viewCenter51 = NXOpen.Point3d(-36.515476252225085, -48.930738177981645, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(7.759538703597781, 64.814970347699543, 0.0)
    viewCenter52 = NXOpen.Point3d(-7.759538703597781, -64.814970347699543, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(9.6994233794972278, 81.018712934624432, 0.0)
    viewCenter53 = NXOpen.Point3d(-9.6994233794972278, -81.018712934624432, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(12.124279224371412, 101.27339116828054, 0.0)
    viewCenter54 = NXOpen.Point3d(-12.124279224371655, -101.27339116828054, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(14.263857911025225, 126.59173896035065, 0.0)
    viewCenter55 = NXOpen.Point3d(-14.263857911025529, -126.59173896035065, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(11.411086328820181, 101.27339116828054, 0.0)
    viewCenter56 = NXOpen.Point3d(-11.411086328820424, -101.27339116828054, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(9.1288690630561451, 81.018712934624432, 0.0)
    viewCenter57 = NXOpen.Point3d(-9.1288690630563405, -81.018712934624432, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(7.3030952504449154, 64.814970347699543, 0.0)
    viewCenter58 = NXOpen.Point3d(-7.3030952504450717, -64.814970347699543, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(5.8424762003559332, 51.85197627815964, 0.0)
    viewCenter59 = NXOpen.Point3d(-5.8424762003560575, -51.85197627815964, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(4.6739809602847471, 41.481581022527713, 0.0)
    viewCenter60 = NXOpen.Point3d(-4.6739809602848714, -41.481581022527713, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(3.7391847682277572, 33.185264818022169, 0.0)
    viewCenter61 = NXOpen.Point3d(-3.7391847682279167, -33.185264818022169, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(2.9913478145821744, 26.548211854417737, 0.0)
    viewCenter62 = NXOpen.Point3d(-2.9913478145823658, -26.548211854417737, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(2.3930782516657652, 21.238569483534192, 0.0)
    viewCenter63 = NXOpen.Point3d(-2.3930782516658926, -21.238569483534182, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(1.9144626013325714, 16.990855586827355, 0.0)
    viewCenter64 = NXOpen.Point3d(-1.9144626013327448, -16.990855586827355, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(2.3930782516657398, 21.238569483534192, 0.0)
    viewCenter65 = NXOpen.Point3d(-2.3930782516658926, -21.238569483534192, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(2.9913478145821748, 26.548211854417744, 0.0)
    viewCenter66 = NXOpen.Point3d(-2.9913478145823027, -26.548211854417744, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(3.7391847682277581, 33.185264818022176, 0.0)
    viewCenter67 = NXOpen.Point3d(-3.7391847682278776, -33.185264818022176, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(4.6739809602846965, 41.481581022527713, 0.0)
    viewCenter68 = NXOpen.Point3d(-4.6739809602848963, -41.481581022527713, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(5.8424762003558701, 51.851976278159633, 0.0)
    viewCenter69 = NXOpen.Point3d(-5.8424762003560566, -51.851976278159633, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(7.3030952504449145, 64.814970347699528, 0.0)
    viewCenter70 = NXOpen.Point3d(-7.3030952504450699, -64.814970347699528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(9.1288690630562392, 81.018712934624403, 0.0)
    viewCenter71 = NXOpen.Point3d(-9.1288690630563369, -81.018712934624403, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(7.3030952504449145, 64.814970347699528, 0.0)
    viewCenter72 = NXOpen.Point3d(-7.3030952504450699, -64.814970347699528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(5.8424762003559314, 51.851976278159619, 0.0)
    viewCenter73 = NXOpen.Point3d(-5.8424762003560557, -51.851976278159619, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(extrude2)
    
    section1.PrepareMappingData()
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId100, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("80")
    
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId101, None)
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature8 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId102, None)
    
    theSession.SetUndoMarkName(markId100, "Extrude")
    
    section1.CleanMappingData()
    
    expression34 = extrudeBuilder3.Limits.StartExtend.Value
    expression35 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression32)
    
    workPart.Expressions.Delete(expression33)
    
    theSession.DeleteUndoMark(markId100, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs10 = theSession.UpdateManager.DoUpdate(markId99)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    scaleAboutPoint74 = NXOpen.Point3d(-28.336009571726727, 29.796628621815671, 0.0)
    viewCenter74 = NXOpen.Point3d(28.336009571726603, -29.796628621815671, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(-22.668807657381425, 23.837302897452563, 0.0)
    viewCenter75 = NXOpen.Point3d(22.668807657381308, -23.837302897452542, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-17.948086887493744, 18.882883079550663, 0.0)
    viewCenter76 = NXOpen.Point3d(17.948086887493616, -18.882883079550645, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(-22.435108609367177, 23.603603849438326, 0.0)
    viewCenter77 = NXOpen.Point3d(22.43510860936706, -23.603603849438304, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-28.043885761708925, 29.504504811797883, 0.0)
    viewCenter78 = NXOpen.Point3d(28.043885761708825, -29.504504811797883, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-35.054857202136155, 36.880631014747351, 0.0)
    viewCenter79 = NXOpen.Point3d(35.054857202136027, -36.880631014747351, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-43.818571502670189, 46.100788768434143, 0.0)
    viewCenter80 = NXOpen.Point3d(43.818571502670032, -46.100788768434221, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects11 = [NXOpen.DisplayableObject.Null] * 2 
    objects11[0] = sketch2
    objects11[1] = arc1
    theSession.DisplayManager.BlankObjects(objects11)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()