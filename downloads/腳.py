# NX 1872
# Journal created by Reader on Wed Jun 19 20:09:02 2024 台北標準時間

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
    
    theSession.UndoToMark(markId4, None)
    
    theSession.DeleteUndoMark(markId4, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane2
    
    unit2 = workPart.UnitCollection.FindObject("MilliMeter")
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId5, "Create Sketch Dialog")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
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
        
    plane2.DestroyPlane()
    
    theSession.UndoToMark(markId5, None)
    
    theSession.DeleteUndoMark(markId5, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Sketch")
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    geometry1 = [NXOpen.NXObject.Null] * 1 
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XY plane")
    geometry1[0] = datumPlane1
    plane3 = workPart.Planes.CreatePlane(NXOpen.PlaneTypes.MethodType.Coincident, NXOpen.PlaneTypes.AlternateType.One, origin3, normal3, "", False, False, geometry1)
    
    plane3.Evaluate()
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    point2 = workPart.Points.CreatePoint(point1, NXOpen.Xform.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder3.PlaneReference = plane3
    
    sketchInPlaceBuilder3.AxisReference = direction1
    
    sketchInPlaceBuilder3.SketchOrigin = point2
    
    sketchInPlaceBuilder3.AxisOrientation = NXOpen.AxisOrientation.Horizontal
    
    sketchInPlaceBuilder3.PlaneOption = NXOpen.Sketch.PlaneOption.ExistingPlane
    
    sketchInPlaceBuilder3.OriginOption = NXOpen.OriginMethod.SpecifyPoint
    
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
    
    nXObject2 = sketchInPlaceBuilder3.Commit()
    
    sketchInPlaceBuilder3.Destroy()
    
    sketch1 = nXObject2
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId8, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 24.818492309121122, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point3 = datumCsys2.FindObject("POINT 1")
    geom2_1.Geometry = point3
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
    dimOrigin1 = NXOpen.Point3d(0.0, 3.3122699718553799, 0.0)
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
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId9, "Rapid Dimension Dialog")
    
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
    
    point1_1 = NXOpen.Point3d(17.131554047100707, 17.957377771522538, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc1, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(17.131554047100707, 17.957377771522538, 0.0)
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
    
    point5 = NXOpen.Point3d(28.628133381744448, 31.549371481922496, 0.0)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.SetUndoMarkName(markId9, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId9, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId11, "Rapid Dimension Dialog")
    
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
    expression6.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId11, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.30219402156205882)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId12, None)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId11, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder2.Destroy()
    
    theSession.UndoToMark(markId13, None)
    
    theSession.DeleteUndoMark(markId13, None)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    sketch2 = theSession.ActiveSketch
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit3 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit3)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId15, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = workPart.Features.FindObject("SKETCH(1)")
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(4.9591806925002349, -5.6042995528119643, 0.0)
    section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId17, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    unit4 = extrudeBuilder1.Offset.StartOffset.Units
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    theSession.DeleteUndoMark(markId16, None)
    
    extrudeBuilder1.Limits.SymmetricOption = True
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("50")
    
    extrudeBuilder1.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("7.5")
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId18, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature1 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId19, None)
    
    theSession.SetUndoMarkName(markId15, "Extrude")
    
    expression9 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression7)
    
    workPart.Expressions.Delete(expression8)
    
    scaleAboutPoint1 = NXOpen.Point3d(28.043885761708879, -10.224333350623045, 0.0)
    viewCenter1 = NXOpen.Point3d(-28.043885761708879, 10.224333350623045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(35.054857202136027, -12.780416688278804, 0.0)
    viewCenter2 = NXOpen.Point3d(-35.054857202136091, 12.780416688278804, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(43.81857150267011, -15.975520860348503, 0.0)
    viewCenter3 = NXOpen.Point3d(-43.81857150267011, 15.975520860348503, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(52.490997112573503, -18.257738126112578, 0.0)
    viewCenter4 = NXOpen.Point3d(-52.490997112573503, 18.257738126112578, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(53.489467166345342, -14.977050806576695, 0.0)
    viewCenter5 = NXOpen.Point3d(-53.489467166345342, 14.977050806576695, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(71.319289555126858, -17.829822388781828, 0.0)
    viewCenter6 = NXOpen.Point3d(-71.31928955512717, 17.829822388781828, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(57.055431644101489, -14.263857911025465, 0.0)
    viewCenter7 = NXOpen.Point3d(-57.055431644101738, 14.263857911025465, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(45.644345315281093, -11.411086328820371, 0.0)
    viewCenter8 = NXOpen.Point3d(-45.644345315281484, 11.411086328820371, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(36.515476252224879, -9.1288690630562979, 0.0)
    viewCenter9 = NXOpen.Point3d(-36.515476252225191, 9.1288690630562979, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(29.212381001779843, -7.3030952504450379, 0.0)
    viewCenter10 = NXOpen.Point3d(-29.212381001780216, 7.3030952504450379, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(23.369904801423875, -5.842476200356006, 0.0)
    viewCenter11 = NXOpen.Point3d(-23.369904801424198, 5.8424762003560309, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-8.413165728512821, 1.4021942880854636, 0.0)
    viewCenter12 = NXOpen.Point3d(8.413165728512503, -1.4021942880854437, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-6.5435733443989079, 1.121755430468371, 0.0)
    viewCenter13 = NXOpen.Point3d(6.5435733443985891, -1.121755430468339, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-4.9357238940609154, 0.74783695364559133, 0.0)
    viewCenter14 = NXOpen.Point3d(4.9357238940606099, -0.74783695364555303, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(4.1878869404150159, -3.5896173774987163, 0.0)
    viewCenter15 = NXOpen.Point3d(-4.1878869404153427, 3.5896173774987674, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(13.305515079261816, -5.2647721536647927, 0.0)
    viewCenter16 = NXOpen.Point3d(-13.305515079262143, 5.2647721536648495, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(11.103883087729251, -4.1352392188785121, 0.0)
    viewCenter17 = NXOpen.Point3d(-11.10388308772959, 4.1352392188785707, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(8.8831064701833675, -3.3081913751028038, 0.0)
    viewCenter18 = NXOpen.Point3d(-8.8831064701837068, 3.3081913751028664, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    theSession.SetUndoMarkName(markId20, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    extrude1 = feature1
    edge1 = extrude1.FindObject("EDGE * 130 * 140 {(-3.7500000000002,-6.4951905283836,7.5)(7.5000000000003,0,7.5)(-3.7500000000002,6.4951905283836,7.5) EXTRUDE(2)}")
    seedEdges1[0] = edge1
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules2 = [None] * 1 
    rules2[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules2, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    csIndex1 = edgeBlendBuilder1.AddChainset(scCollector1, "15")
    
    try:
        # Unable to terminate the blend faces. Blend adjacent edges first or reduce the radius.
        feature2 = edgeBlendBuilder1.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3620008)
        
    theSession.UndoToMarkWithStatus(markId21, None)
    
    theSession.DeleteUndoMark(markId21, None)
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression13)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression12)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    scCollector1.Destroy()
    
    workPart.Expressions.Delete(expression10)
    
    workPart.Expressions.Delete(expression11)
    
    theSession.UndoToMark(markId20, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(extrude1)
    
    section1.PrepareMappingData()
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit3)
    
    extrudeBuilder2.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("7.5")
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    theSession.SetUndoMarkName(markId23, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    extrudeBuilder2.Limits.SymmetricOption = False
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("-7.5")
    
    extrudeBuilder2.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Value
    
    extrudeBuilder2.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Value
    
    extrudeBuilder2.Limits.EndExtend.Target = NXOpen.DisplayableObject.Null
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("15")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("0")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId24, None)
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature3 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId25, None)
    
    theSession.SetUndoMarkName(markId23, "Extrude")
    
    section1.CleanMappingData()
    
    expression16 = extrudeBuilder2.Limits.StartExtend.Value
    expression17 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression14)
    
    workPart.Expressions.Delete(expression15)
    
    theSession.DeleteUndoMark(markId23, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId22)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder2 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    blendLimitsData2 = edgeBlendBuilder2.LimitsListData
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder2 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    theSession.SetUndoMarkName(markId26, "Edge Blend Dialog")
    
    scCollector2 = workPart.ScCollectors.CreateCollector()
    
    seedEdges2 = [NXOpen.Edge.Null] * 1 
    extrude2 = feature3
    edge2 = extrude2.FindObject("EDGE * 120 * 140 {(-3.7500000000002,6.4951905283836,15)(7.5000000000003,0,15)(-3.7500000000002,-6.4951905283836,15) EXTRUDE(2)}")
    seedEdges2[0] = edge2
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules3 = [None] * 1 
    rules3[0] = edgeMultipleSeedTangentRule2
    scCollector2.ReplaceRules(rules3, False)
    
    scCollector2.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.73660201426838179
    rotMatrix1.Xy = 0.676281177963449
    rotMatrix1.Xz = 0.0078256570413876726
    rotMatrix1.Yx = -0.40589810542008598
    rotMatrix1.Yy = 0.43278760814510869
    rotMatrix1.Yz = 0.80494820594397098
    rotMatrix1.Zx = 0.54098447352224721
    rotMatrix1.Zy = -0.59610288924681631
    rotMatrix1.Zz = 0.59329347277671129
    translation1 = NXOpen.Point3d(-2.9228039270060568, -1.471872569717994, -1.648278419426453)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 5.3985313952536478)
    
    scaleAboutPoint19 = NXOpen.Point3d(1.9113994611703606, 10.194130459576181, 0.0)
    viewCenter19 = NXOpen.Point3d(-1.9113994611706993, -10.194130459576115, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(2.3892493264629819, 12.742663074470221, 0.0)
    viewCenter20 = NXOpen.Point3d(-2.389249326463327, -12.742663074470153, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(2.9865616580787795, 15.92832884308776, 0.0)
    viewCenter21 = NXOpen.Point3d(-2.9865616580791188, -15.928328843087694, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(2.3892493264629819, 12.742663074470221, 0.0)
    viewCenter22 = NXOpen.Point3d(-2.389249326463327, -12.742663074470153, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(1.9113994611703604, 10.194130459576179, 0.0)
    viewCenter23 = NXOpen.Point3d(-1.9113994611706988, -10.194130459576117, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(1.529119568936248, 8.1553043676609462, 0.0)
    viewCenter24 = NXOpen.Point3d(-1.5291195689365957, -8.1553043676608823, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(1.223295655148966, 6.524243494128763, 0.0)
    viewCenter25 = NXOpen.Point3d(-1.2232956551493084, -6.5242434941286991, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-4.3662244922247844, 2.2082054903205277, 0.0)
    viewCenter26 = NXOpen.Point3d(4.3662244922244415, -2.2082054903204615, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-3.4929795937798582, 1.7665643922564291, 0.0)
    viewCenter27 = NXOpen.Point3d(3.4929795937795212, -1.7665643922563625, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-2.7943836750239197, 1.4132515138051489, 0.0)
    viewCenter28 = NXOpen.Point3d(2.7943836750235826, -1.4132515138050818, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-2.2355069400191683, 1.1306012110441266, 0.0)
    viewCenter29 = NXOpen.Point3d(2.2355069400188352, -1.1306012110440586, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-2.7943836750239193, 1.41325151380515, 0.0)
    viewCenter30 = NXOpen.Point3d(2.7943836750235853, -1.4132515138050816, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(-3.4929795937798547, 1.7665643922564289, 0.0)
    viewCenter31 = NXOpen.Point3d(3.4929795937795225, -1.7665643922563623, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-4.391317736432967, 2.2082054903205273, 0.0)
    viewCenter32 = NXOpen.Point3d(4.3913177364326312, -2.2082054903204611, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-5.5518802810616394, 2.7602568629006488, 0.0)
    viewCenter33 = NXOpen.Point3d(5.5518802810613019, -2.7602568629005844, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(-6.939850351327002, 3.4503210786258007, 0.0)
    viewCenter34 = NXOpen.Point3d(6.9398503513266681, -3.4503210786257372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint34, viewCenter34)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.72881855315359834
    rotMatrix2.Xy = 0.68465994594793278
    rotMatrix2.Xz = 0.0080171686814128357
    rotMatrix2.Yx = 0.029076908410801537
    rotMatrix2.Yy = -0.04264638592661741
    rotMatrix2.Yz = 0.99866702116604644
    rotMatrix2.Zx = 0.68408921200115491
    rotMatrix2.Zy = -0.7276139389689894
    rotMatrix2.Zz = -0.050989271829140051
    translation2 = NXOpen.Point3d(-8.0822639762854607, -5.5584415137114753, 3.3137118276213595)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 5.3985313952536504)
    
    seedEdges3 = [NXOpen.Edge.Null] * 2 
    seedEdges3[0] = edge2
    seedEdges3[1] = edge1
    edgeMultipleSeedTangentRule3 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges3, 0.5, True)
    
    rules4 = [None] * 1 
    rules4[0] = edgeMultipleSeedTangentRule3
    scCollector2.ReplaceRules(rules4, False)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId27, None)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder2.Tolerance = 0.01
    
    edgeBlendBuilder2.AllInstancesOption = False
    
    edgeBlendBuilder2.RemoveSelfIntersection = True
    
    edgeBlendBuilder2.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder2.LimitFailingAreas = True
    
    edgeBlendBuilder2.ConvexConcaveY = False
    
    edgeBlendBuilder2.RollOverSmoothEdge = True
    
    edgeBlendBuilder2.RollOntoEdge = True
    
    edgeBlendBuilder2.MoveSharpEdge = True
    
    edgeBlendBuilder2.TrimmingOption = False
    
    edgeBlendBuilder2.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder2.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder2.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder2.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex2 = edgeBlendBuilder2.AddChainset(scCollector2, "7.5")
    
    feature4 = edgeBlendBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId28, None)
    
    theSession.SetUndoMarkName(markId26, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder2)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression21)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression20)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression18)
    
    workPart.Expressions.Delete(expression19)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.94702385116829602
    rotMatrix3.Xy = 0.29803865000862773
    rotMatrix3.Xz = 0.11966113997199741
    rotMatrix3.Yx = -0.28169743008200504
    rotMatrix3.Yy = 0.59189550757983334
    rotMatrix3.Yz = 0.75518624589699679
    rotMatrix3.Zx = 0.15424779805091632
    rotMatrix3.Zy = -0.74888762254949715
    rotMatrix3.Zz = 0.64449588485000997
    translation3 = NXOpen.Point3d(-8.9195937609648475, -3.7323356991936025, -1.9024268474722663)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 5.3985313952536504)
    
    scaleAboutPoint35 = NXOpen.Point3d(-18.03576927463488, 4.5089423186587094, 0.0)
    viewCenter35 = NXOpen.Point3d(18.035769274634543, -4.5089423186586428, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-14.428615419707945, 3.6071538549269713, 0.0)
    viewCenter36 = NXOpen.Point3d(14.428615419707597, -3.6071538549269078, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-11.542892335766389, 2.8857230839415879, 0.0)
    viewCenter37 = NXOpen.Point3d(11.542892335766052, -2.8857230839415209, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(-9.0586611591558288, 2.132925757695963, 0.0)
    viewCenter38 = NXOpen.Point3d(9.0586611591554931, -2.1329257576958986, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-11.260593338424281, 2.5406909760790062, 0.0)
    viewCenter39 = NXOpen.Point3d(11.260593338423943, -2.5406909760789449, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(-14.075741673030304, 3.175863720098751, 0.0)
    viewCenter40 = NXOpen.Point3d(14.075741673029968, -3.1758637200986874, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-16.761502967187862, 3.2836862538058096, 0.0)
    viewCenter41 = NXOpen.Point3d(16.761502967187525, -3.2836862538057425, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.78532913503359214
    rotMatrix4.Xy = 0.61813578899026467
    rotMatrix4.Xz = 0.034151076656096901
    rotMatrix4.Yx = -0.011924586790919593
    rotMatrix4.Yy = -0.040050294708487318
    rotMatrix4.Yz = 0.99912650756729793
    rotMatrix4.Zx = 0.61896361274088829
    rotMatrix4.Zy = -0.78505039345454841
    rotMatrix4.Zz = -0.024081649436868927
    translation4 = NXOpen.Point3d(-12.265937664523236, -4.9789598363064531, 3.1119046596793263)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 4.3188251162029205)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.77487233311268677
    rotMatrix5.Xy = 0.61739296682061329
    rotMatrix5.Xz = -0.13564214646245171
    rotMatrix5.Yx = 0.14051611316610735
    rotMatrix5.Yy = 0.040977527029494282
    rotMatrix5.Yz = 0.9892300360478532
    rotMatrix5.Zx = 0.61630194654665016
    rotMatrix5.Zy = -0.78558689321995845
    rotMatrix5.Zz = -0.055001308019191696
    translation5 = NXOpen.Point3d(-10.992488491134123, -4.904736299910617, 3.3438020990467487)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 4.3188251162029205)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 2 
    objects1[0] = sketch2
    objects1[1] = arc1
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.98558650477148713
    rotMatrix6.Xy = -0.066681998026432571
    rotMatrix6.Xz = -0.15547589122278152
    rotMatrix6.Yx = 0.15317655254653509
    rotMatrix6.Yy = -0.038341164917493363
    rotMatrix6.Yz = 0.98745475786120185
    rotMatrix6.Zx = -0.07180658300096078
    rotMatrix6.Zy = -0.99703734444200354
    rotMatrix6.Zz = -0.027574416145294513
    translation6 = NXOpen.Point3d(-10.843735405431628, -4.8914217135107325, 3.1381004099925152)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 4.3188251162029205)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = -0.8659429280429003
    rotMatrix7.Xy = 0.3415464939281937
    rotMatrix7.Xz = -0.3653612429607796
    rotMatrix7.Yx = -0.44532268786209656
    rotMatrix7.Yy = -0.19400600172550808
    rotMatrix7.Yz = 0.87409917913801927
    rotMatrix7.Zx = 0.22766323604781963
    rotMatrix7.Zy = 0.91962365333860308
    rotMatrix7.Zz = 0.32009652789806115
    translation7 = NXOpen.Point3d(-9.2695952673966495, -4.0412548730868627, 0.53056832966734646)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 4.3188251162029205)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Sketch")
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    geometry2 = [NXOpen.NXObject.Null] * 1 
    geometry2[0] = datumPlane1
    plane6 = workPart.Planes.CreatePlane(NXOpen.PlaneTypes.MethodType.Coincident, NXOpen.PlaneTypes.AlternateType.One, origin6, normal6, "", False, False, geometry2)
    
    plane6.Evaluate()
    
    direction3 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point6 = workPart.Points.CreatePoint(point1, NXOpen.Xform.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder4.PlaneReference = plane6
    
    sketchInPlaceBuilder4.AxisReference = direction3
    
    sketchInPlaceBuilder4.SketchOrigin = point6
    
    sketchInPlaceBuilder4.AxisOrientation = NXOpen.AxisOrientation.Horizontal
    
    sketchInPlaceBuilder4.PlaneOption = NXOpen.Sketch.PlaneOption.ExistingPlane
    
    sketchInPlaceBuilder4.OriginOption = NXOpen.OriginMethod.SpecifyPoint
    
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
    
    nXObject4 = sketchInPlaceBuilder4.Commit()
    
    sketchInPlaceBuilder4.Destroy()
    
    sketch3 = nXObject4
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId32, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 5.1591865139433937, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = arc2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(0.0, 0.69463335960164552, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension2 = sketchDimensionalConstraint2.AssociatedDimension
    
    expression22 = sketchDimensionalConstraint2.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    scaleAboutPoint42 = NXOpen.Point3d(3.0018773588894301, 1.4703072778235196, 0.0)
    viewCenter42 = NXOpen.Point3d(-3.0018773588897747, -1.4703072778234516, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(3.7523466986118397, 1.7613055932260777, 0.0)
    viewCenter43 = NXOpen.Point3d(-3.7523466986121794, -1.7613055932260124, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(4.690433373264832, 2.2016319915325888, 0.0)
    viewCenter44 = NXOpen.Point3d(-4.6904333732651748, -2.2016319915325155, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(5.982695629164386, 2.7520399894157364, 0.0)
    viewCenter45 = NXOpen.Point3d(-5.9826956291647226, -2.7520399894156649, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(7.7775043179137437, 3.2904825960405391, 0.0)
    viewCenter46 = NXOpen.Point3d(-7.7775043179141008, -3.2904825960404622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(10.656676589449185, 3.9261440066392761, 0.0)
    viewCenter47 = NXOpen.Point3d(-10.656676589449535, -3.9261440066392121, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(8.9740434437466643, 3.1409152053114204, 0.0)
    viewCenter48 = NXOpen.Point3d(-8.9740434437470213, -3.1409152053113694, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(7.1792347549972915, 2.5127321642491367, 0.0)
    viewCenter49 = NXOpen.Point3d(-7.1792347549976592, -2.5127321642490856, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(5.9348340641310395, 2.0101857313993174, 0.0)
    viewCenter50 = NXOpen.Point3d(-5.9348340641314152, -2.0101857313992606, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(4.8244457553581208, 1.6081485851194672, 0.0)
    viewCenter51 = NXOpen.Point3d(-4.8244457553584867, -1.6081485851194084, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(3.982082210771738, 1.2865188680955788, 0.0)
    viewCenter52 = NXOpen.Point3d(-3.9820822107721141, -1.2865188680955162, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(-1.4212970352295535, 1.3232765500411681, 0.0)
    viewCenter53 = NXOpen.Point3d(1.4212970352291816, -1.3232765500411012, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-1.1370376281836829, 1.0586212400329378, 0.0)
    viewCenter54 = NXOpen.Point3d(1.1370376281833083, -1.0586212400328743, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-0.9096301025469784, 0.84689699202635826, 0.0)
    viewCenter55 = NXOpen.Point3d(0.90963010254661203, -0.84689699202629409, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-0.72770408203762116, 0.67751759362109298, 0.0)
    viewCenter56 = NXOpen.Point3d(0.72770408203725101, -0.67751759362102881, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId34, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    diameterDimension1 = dimension2
    theSession.UpdateManager.LogForUpdate(diameterDimension1)
    
    perpendicularDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    center3 = NXOpen.Point3d(1.711929324526964, 0.30738464113380159, 0.0)
    arc2.SetParameters(5.1591865139433937, center3, 0.0, ( 360.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint1 = theSession.ActiveSketch.FindObject("ENTITY 243 2 1")
    sketchHelpedDimensionalConstraint1.Refresh()
    
    sketchHelpedDimensionalConstraint2 = theSession.ActiveSketch.FindObject("ENTITY 243 1 1")
    sketchHelpedDimensionalConstraint2.Refresh()
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId34)
    
    geoms1 = [NXOpen.SmartObject.Null] * 1 
    geoms1[0] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 1 
    geoms2[0] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms2)
    
    geoms3 = [NXOpen.SmartObject.Null] * 1 
    geoms3[0] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms3)
    
    scaleAboutPoint57 = NXOpen.Point3d(-0.62231245636323396, -0.58216326562991716, 0.0)
    viewCenter57 = NXOpen.Point3d(0.62231245636286414, 0.58216326562998055, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-0.77789057045399967, -0.72770408203740511, 0.0)
    viewCenter58 = NXOpen.Point3d(0.77789057045362309, 0.72770408203746928, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-0.97236321306745133, -0.90963010254676424, 0.0)
    viewCenter59 = NXOpen.Point3d(0.97236321306707685, 0.90963010254682852, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(-1.215454016334274, -1.1370376281834653, 0.0)
    viewCenter60 = NXOpen.Point3d(1.2154540163338994, 1.1370376281835288, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-1.5193175204177838, -1.4212970352293357, 0.0)
    viewCenter61 = NXOpen.Point3d(1.5193175204174119, 1.4212970352293983, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(-1.2154540163342669, -1.1370376281834651, 0.0)
    viewCenter62 = NXOpen.Point3d(1.2154540163338925, 1.1370376281835286, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(-0.97236321306745099, -0.90963010254676668, 0.0)
    viewCenter63 = NXOpen.Point3d(0.97236321306707663, 0.90963010254682553, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(-0.77789057045399512, -0.727704082037407, 0.0)
    viewCenter64 = NXOpen.Point3d(0.77789057045362708, 0.72770408203746684, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(-0.62231245636323373, -0.58216326562991871, 0.0)
    viewCenter65 = NXOpen.Point3d(0.62231245636286403, 0.58216326562997867, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(-0.49784996509062263, -0.46573061250392955, 0.0)
    viewCenter66 = NXOpen.Point3d(0.49784996509025425, 0.46573061250398978, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(-0.3725844900033517, -0.37258449000313704, 0.0)
    viewCenter67 = NXOpen.Point3d(0.37258449000298255, 0.37258449000319838, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId36, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    theSession.UpdateManager.LogForUpdate(diameterDimension1)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    center4 = NXOpen.Point3d(-0.012558715841145762, 0.00096601745877722411, 0.0)
    arc2.SetParameters(5.1591865139433937, center4, 0.0, ( 360.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint1.Refresh()
    
    sketchHelpedDimensionalConstraint2.Refresh()
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId36)
    
    geoms4 = [NXOpen.SmartObject.Null] * 1 
    geoms4[0] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms4)
    
    geoms5 = [NXOpen.SmartObject.Null] * 1 
    geoms5[0] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms5)
    
    geoms6 = [NXOpen.SmartObject.Null] * 1 
    geoms6[0] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms6)
    
    scaleAboutPoint68 = NXOpen.Point3d(-0.1747292780706371, 0.10278192827676669, 0.0)
    viewCenter68 = NXOpen.Point3d(0.1747292780702655, -0.10278192827670446, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-0.13978342245654615, 0.082225542621418957, 0.0)
    viewCenter69 = NXOpen.Point3d(0.13978342245617525, -0.08222554262135727, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(-0.11182673796527506, 0.065780434097141335, 0.0)
    viewCenter70 = NXOpen.Point3d(0.11182673796490264, -0.065780434097080204, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-0.084198955644487816, 0.057886782005487927, 0.0)
    viewCenter71 = NXOpen.Point3d(0.084198955644116294, -0.0578867820054269, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(-0.067359164515627595, 0.046309425604396805, 0.0)
    viewCenter72 = NXOpen.Point3d(0.067359164515255351, -0.046309425604335423, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-0.053887331612539405, 0.037047540483523475, 0.0)
    viewCenter73 = NXOpen.Point3d(0.053887331612167237, -0.037047540483462017, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(-0.067359164515627595, 0.046309425604396805, 0.0)
    viewCenter74 = NXOpen.Point3d(0.067359164515255351, -0.046309425604335423, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(-0.084198955644487802, 0.057886782005487913, 0.0)
    viewCenter75 = NXOpen.Point3d(0.08419895564411628, -0.057886782005426886, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-0.10524869455556263, 0.072358477506852023, 0.0)
    viewCenter76 = NXOpen.Point3d(0.10524869455519133, -0.072358477506790891, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(-0.1315608681944084, 0.09044809688355801, 0.0)
    viewCenter77 = NXOpen.Point3d(0.13156086819403681, -0.090448096883497017, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-0.16445108524296315, 0.11306012110443962, 0.0)
    viewCenter78 = NXOpen.Point3d(0.16445108524259158, -0.1130601211043774, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-0.20556385655365794, 0.14132515138054186, 0.0)
    viewCenter79 = NXOpen.Point3d(0.20556385655328768, -0.14132515138048052, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-0.25695482069202585, 0.17665643922567048, 0.0)
    viewCenter80 = NXOpen.Point3d(0.25695482069165337, -0.17665643922560748, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-0.10037297683293567, 0.80298381466202962, 0.0)
    viewCenter81 = NXOpen.Point3d(0.10037297683256595, -0.80298381466196633, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(-0.12546622104112251, 1.0037297683275284, 0.0)
    viewCenter82 = NXOpen.Point3d(0.12546622104075236, -1.0037297683274642, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId38, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    theSession.UpdateManager.LogForUpdate(diameterDimension1)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension2)
    
    center5 = NXOpen.Point3d(1.3618513466714299, 0.11753204619638069, 0.0)
    arc2.SetParameters(5.1591865139433937, center5, 0.0, ( 360.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint1.Refresh()
    
    sketchHelpedDimensionalConstraint2.Refresh()
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId38)
    
    geoms7 = [NXOpen.SmartObject.Null] * 1 
    geoms7[0] = arc2
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms7)
    
    geoms8 = [NXOpen.SmartObject.Null] * 1 
    geoms8[0] = arc2
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms8)
    
    geoms9 = [NXOpen.SmartObject.Null] * 1 
    geoms9[0] = arc2
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms9)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId40, "Class Selection Dialog")
    
    theSession.SetUndoMarkName(markId40, "Class Selection")
    
    theSession.DeleteUndoMark(markId40, None)
    
    theSession.DeleteUndoMark(markId39, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = arc2
    nErrs5 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs6 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId41, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Show")
    
    objects3 = [NXOpen.DisplayableObject.Null] * 2 
    objects3[0] = sketch2
    objects3[1] = arc1
    theSession.DisplayManager.ShowObjects(objects3, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId45, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix3 = theSession.ActiveSketch.Orientation
    
    center6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc3 = workPart.Curves.CreateArc(center6, nXMatrix3, 3.9756183432051966, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = arc3
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(0.0, 0.35565228011604216, 0.0)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression23 = sketchDimensionalConstraint3.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId46, "Rapid Dimension Dialog")
    
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
    
    point1_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    point1_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc3, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometryFromLeader(True)
    
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
    sketchRapidDimensionBuilder3.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point8 = NXOpen.Point3d(7.9174613960603883, 4.6970491141905839, 0.0)
    sketchRapidDimensionBuilder3.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point8)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.TextCentered = False
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject5 = sketchRapidDimensionBuilder3.Commit()
    
    theSession.DeleteUndoMark(markId47, None)
    
    theSession.SetUndoMarkName(markId46, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId46, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId48, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits75 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits77 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits79 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits83 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    expression24 = workPart.Expressions.FindObject("p12")
    expression24.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId48, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(1.2576659951642091)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId49, None)
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId48, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder4.Destroy()
    
    theSession.UndoToMark(markId50, None)
    
    theSession.DeleteUndoMark(markId50, None)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    sketch4 = theSession.ActiveSketch
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects4 = [NXOpen.DisplayableObject.Null] * 2 
    objects4[0] = sketch2
    objects4[1] = arc1
    theSession.DisplayManager.BlankObjects(objects4)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section2
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit3)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("7.5")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("7.5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId53, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = workPart.Features.FindObject("SKETCH(4)")
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section2.AllowSelfIntersection(True)
    
    rules5 = [None] * 1 
    rules5[0] = curveFeatureRule2
    helpPoint2 = NXOpen.Point3d(3.6622629758345537, 3.3988451542217009, 0.0)
    section2.AddToSection(rules5, arc3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId55, None)
    
    direction4 = workPart.Directions.CreateDirection(sketch4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction4
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies4[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies4)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies5)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    theSession.DeleteUndoMark(markId54, None)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("100")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies6)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = -0.95294203553116585
    rotMatrix8.Xy = -0.1659340584043332
    rotMatrix8.Xz = -0.25370724305621178
    rotMatrix8.Yx = -0.28438419792452868
    rotMatrix8.Yy = 0.77920628120017865
    rotMatrix8.Yz = 0.55853665887657566
    rotMatrix8.Zx = 0.10501002280039395
    rotMatrix8.Zy = 0.60440339145280464
    rotMatrix8.Zz = -0.78972744381324722
    translation8 = NXOpen.Point3d(-12.913230885434825, 4.4268969931640934, 15.478767477323023)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 4.3188251162029179)
    
    scaleAboutPoint83 = NXOpen.Point3d(-24.505121297058228, 11.333618599889386, 0.0)
    viewCenter83 = NXOpen.Point3d(24.505121297057883, -11.333618599889316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(-19.261025339487794, 9.0668948799115121, 0.0)
    viewCenter84 = NXOpen.Point3d(19.26102533948746, -9.0668948799114464, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(-15.055946524912638, 7.4103486802303866, 0.0)
    viewCenter85 = NXOpen.Point3d(15.05594652491229, -7.41034868023032, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(-11.825191333108499, 5.9910120547047869, 0.0)
    viewCenter86 = NXOpen.Point3d(11.825191333108165, -5.9910120547047176, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(-9.1590341359885841, 4.918275864804774, 0.0)
    viewCenter87 = NXOpen.Point3d(9.1590341359882501, -4.9182758648047038, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(-7.3071527134243501, 3.934620691843826, 0.0)
    viewCenter88 = NXOpen.Point3d(7.307152713424018, -3.9346206918437541, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(-9.1339408917803961, 4.918275864804774, 0.0)
    viewCenter89 = NXOpen.Point3d(9.1339408917800622, -4.9182758648047011, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(-11.417426114725451, 6.1478448310059566, 0.0)
    viewCenter90 = NXOpen.Point3d(11.417426114725119, -6.1478448310058873, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(-14.271782643406782, 7.6848060387574364, 0.0)
    viewCenter91 = NXOpen.Point3d(14.271782643406434, -7.6848060387573662, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(-17.839728304258426, 9.6060075484467902, 0.0)
    viewCenter92 = NXOpen.Point3d(17.839728304258088, -9.6060075484467191, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(-22.299660380322997, 12.007509435558475, 0.0)
    viewCenter93 = NXOpen.Point3d(22.299660380322653, -12.007509435558402, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(-27.874575475403699, 15.009386794448083, 0.0)
    viewCenter94 = NXOpen.Point3d(27.874575475403358, -15.009386794448012, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-34.843219344254585, 18.76173349306011, 0.0)
    viewCenter95 = NXOpen.Point3d(34.843219344254237, -18.761733493060021, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-43.554024180318159, 23.452166866325122, 0.0)
    viewCenter96 = NXOpen.Point3d(43.554024180317832, -23.452166866325019, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(-53.545125881022962, 32.605691178946898, 0.0)
    viewCenter97 = NXOpen.Point3d(53.545125881022642, -32.605691178946799, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(-66.931407351278665, 40.944073212094999, 0.0)
    viewCenter98 = NXOpen.Point3d(66.931407351278338, -40.944073212094899, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-83.664259189098303, 51.180091515118754, 0.0)
    viewCenter99 = NXOpen.Point3d(83.66425918909799, -51.180091515118633, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(-104.58032398637283, 63.975114393898423, 0.0)
    viewCenter100 = NXOpen.Point3d(104.58032398637249, -63.975114393898323, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(-135.47241689575529, 111.00704780676431, 0.0)
    viewCenter101 = NXOpen.Point3d(135.47241689575492, -111.00704780676425, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(-101.07483826615925, 88.513514435393645, 0.0)
    viewCenter102 = NXOpen.Point3d(101.07483826615885, -88.513514435393589, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(-80.392472516898991, 70.577112500300686, 0.0)
    viewCenter103 = NXOpen.Point3d(80.392472516898522, -70.577112500300629, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(-64.127018775107842, 56.461690000240559, 0.0)
    viewCenter104 = NXOpen.Point3d(64.127018775107388, -56.461690000240509, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(-88.338240149383182, 78.055482036756402, 0.0)
    viewCenter105 = NXOpen.Point3d(88.338240149382699, -78.055482036756345, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(-110.42280018672892, 97.569352545945449, 0.0)
    viewCenter106 = NXOpen.Point3d(110.4228001867284, -97.569352545945421, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(-146.06190500890068, 133.64664308314383, 0.0)
    viewCenter107 = NXOpen.Point3d(146.06190500890006, -133.64664308314383, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint107, viewCenter107)
    
    scaleAboutPoint108 = NXOpen.Point3d(-116.84952400712054, 106.91731446651507, 0.0)
    viewCenter108 = NXOpen.Point3d(116.84952400712002, -106.91731446651507, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint108, viewCenter108)
    
    scaleAboutPoint109 = NXOpen.Point3d(-93.245920157682264, 85.533851573212047, 0.0)
    viewCenter109 = NXOpen.Point3d(93.245920157681752, -85.533851573212075, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(-76.092410033437005, 69.922755165860778, 0.0)
    viewCenter110 = NXOpen.Point3d(76.092410033436494, -69.922755165860806, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint110, viewCenter110)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.98470868986983873
    rotMatrix9.Xy = 0.15937276335845055
    rotMatrix9.Xz = 0.070349970819545526
    rotMatrix9.Yx = -0.15196088814889727
    rotMatrix9.Yy = 0.98326602777303573
    rotMatrix9.Yz = -0.10047789359072903
    rotMatrix9.Zx = -0.085186175919674118
    rotMatrix9.Zy = 0.088251010911621353
    rotMatrix9.Zz = 0.9924490286686044
    translation9 = NXOpen.Point3d(-62.904209259945084, 27.340576014726103, -75.368567890959113)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 1.7689907675967165)
    
    scaleAboutPoint111 = NXOpen.Point3d(-45.468486781650903, 27.221265112698742, 0.0)
    viewCenter111 = NXOpen.Point3d(45.468486781650391, -27.221265112698742, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint111, viewCenter111)
    
    scaleAboutPoint112 = NXOpen.Point3d(-36.374789425320778, 21.777012090159001, 0.0)
    viewCenter112 = NXOpen.Point3d(36.374789425320273, -21.777012090159001, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint112, viewCenter112)
    
    scaleAboutPoint113 = NXOpen.Point3d(-29.09983154025668, 17.421609672127197, 0.0)
    viewCenter113 = NXOpen.Point3d(29.099831540256158, -17.421609672127197, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(-23.279865232205406, 13.937287737701755, 0.0)
    viewCenter114 = NXOpen.Point3d(23.27986523220488, -13.937287737701755, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint114, viewCenter114)
    
    scaleAboutPoint115 = NXOpen.Point3d(-29.09983154025668, 17.421609672127197, 0.0)
    viewCenter115 = NXOpen.Point3d(29.099831540256151, -17.421609672127197, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(-36.374789425320792, 21.777012090158998, 0.0)
    viewCenter116 = NXOpen.Point3d(36.374789425320252, -21.777012090158998, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint116, viewCenter116)
    
    scaleAboutPoint117 = NXOpen.Point3d(-45.468486781650931, 27.221265112698742, 0.0)
    viewCenter117 = NXOpen.Point3d(45.46848678165037, -27.221265112698742, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(-56.835608477063573, 34.026581390873432, 0.0)
    viewCenter118 = NXOpen.Point3d(56.835608477063062, -34.026581390873432, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint118, viewCenter118)
    
    scaleAboutPoint119 = NXOpen.Point3d(-71.511908692357892, 42.533226738591786, 0.0)
    viewCenter119 = NXOpen.Point3d(71.51190869235738, -42.533226738591786, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint119, viewCenter119)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.98606244891277839
    rotMatrix10.Xy = -0.090578280380769718
    rotMatrix10.Xz = 0.13955795200341695
    rotMatrix10.Yx = 0.12785106449665354
    rotMatrix10.Yy = -0.12423804196615877
    rotMatrix10.Yz = -0.98398120624099505
    rotMatrix10.Zx = 0.10646573228601711
    rotMatrix10.Zy = 0.98810955063275774
    rotMatrix10.Zz = -0.1109259383423214
    translation10 = NXOpen.Point3d(-111.20780744764102, 89.70212192448075, -16.349409934991808)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 0.90572327300951894)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId56, None)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder3.ParentFeatureInternal = False
    
    feature5 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId57, None)
    
    theSession.SetUndoMarkName(markId53, "Extrude")
    
    expression27 = extrudeBuilder3.Limits.StartExtend.Value
    expression28 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression25)
    
    workPart.Expressions.Delete(expression26)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder3 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    blendLimitsData3 = edgeBlendBuilder3.LimitsListData
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder3 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    theSession.SetUndoMarkName(markId58, "Edge Blend Dialog")
    
    scCollector3 = workPart.ScCollectors.CreateCollector()
    
    seedEdges4 = [NXOpen.Edge.Null] * 1 
    extrude3 = feature5
    edge3 = extrude3.FindObject("EDGE * 120 * 140 {(-2.5000000000001,4.3301270189224,100)(5.0000000000002,0,100)(-2.5000000000001,-4.3301270189224,100) EXTRUDE(2)}")
    seedEdges4[0] = edge3
    edgeMultipleSeedTangentRule4 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges4, 0.5, True)
    
    rules6 = [None] * 1 
    rules6[0] = edgeMultipleSeedTangentRule4
    scCollector3.ReplaceRules(rules6, False)
    
    scCollector3.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    scaleAboutPoint120 = NXOpen.Point3d(-89.389885865447269, -5.8424762003560309, 0.0)
    viewCenter120 = NXOpen.Point3d(89.389885865446743, 5.8424762003560309, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(-97.861476355963561, -13.875880975845554, 0.0)
    viewCenter121 = NXOpen.Point3d(97.861476355962935, 13.875880975845554, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(-122.3268454449543, -10.954642875667528, 0.0)
    viewCenter122 = NXOpen.Point3d(122.32684544495383, 10.954642875667528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint122, viewCenter122)
    
    scaleAboutPoint123 = NXOpen.Point3d(-152.90855680619288, -13.693303594584457, 0.0)
    viewCenter123 = NXOpen.Point3d(152.90855680619239, 13.693303594584409, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint123, viewCenter123)
    
    scaleAboutPoint124 = NXOpen.Point3d(-122.3268454449543, -10.954642875667567, 0.0)
    viewCenter124 = NXOpen.Point3d(122.32684544495383, 10.954642875667528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint124, viewCenter124)
    
    scaleAboutPoint125 = NXOpen.Point3d(-97.861476355963518, -8.7637143005340548, 0.0)
    viewCenter125 = NXOpen.Point3d(97.861476355963021, 8.7637143005340228, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint125, viewCenter125)
    
    scaleAboutPoint126 = NXOpen.Point3d(-78.289181084770817, -7.0109714404272188, 0.0)
    viewCenter126 = NXOpen.Point3d(78.289181084770362, 7.0109714404271939, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint126, viewCenter126)
    
    scaleAboutPoint127 = NXOpen.Point3d(-70.810811548315144, 0.70109714404270196, 0.0)
    viewCenter127 = NXOpen.Point3d(70.810811548314661, -0.7010971440427417, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint127, viewCenter127)
    
    scaleAboutPoint128 = NXOpen.Point3d(-56.648649238652155, 0.56087771523417751, 0.0)
    viewCenter128 = NXOpen.Point3d(56.648649238651707, -0.5608777152341935, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(-45.318919390921764, 0.44870217218734193, 0.0)
    viewCenter129 = NXOpen.Point3d(45.318919390921309, -0.4487021721873547, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint129, viewCenter129)
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId59, None)
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder3.Tolerance = 0.01
    
    edgeBlendBuilder3.AllInstancesOption = False
    
    edgeBlendBuilder3.RemoveSelfIntersection = True
    
    edgeBlendBuilder3.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder3.LimitFailingAreas = True
    
    edgeBlendBuilder3.ConvexConcaveY = False
    
    edgeBlendBuilder3.RollOverSmoothEdge = True
    
    edgeBlendBuilder3.RollOntoEdge = True
    
    edgeBlendBuilder3.MoveSharpEdge = True
    
    edgeBlendBuilder3.TrimmingOption = False
    
    edgeBlendBuilder3.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder3.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder3.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder3.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex3 = edgeBlendBuilder3.AddChainset(scCollector3, "4")
    
    feature6 = edgeBlendBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId60, None)
    
    theSession.SetUndoMarkName(markId58, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder3)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression32)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression31)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression29)
    
    workPart.Expressions.Delete(expression30)
    
    scaleAboutPoint130 = NXOpen.Point3d(-35.537212037237715, 14.7174312477448, 0.0)
    viewCenter130 = NXOpen.Point3d(35.537212037237268, -14.717431247744841, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint130, viewCenter130)
    
    scaleAboutPoint131 = NXOpen.Point3d(-28.429769629790226, 11.773944998195832, 0.0)
    viewCenter131 = NXOpen.Point3d(28.429769629789767, -11.773944998195898, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint131, viewCenter131)
    
    scaleAboutPoint132 = NXOpen.Point3d(-22.743815703832219, 9.4191559985566524, 0.0)
    viewCenter132 = NXOpen.Point3d(22.743815703831768, -9.419155998556711, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(-18.195052563065826, 7.5353247988453163, 0.0)
    viewCenter133 = NXOpen.Point3d(18.195052563065367, -7.535324798845374, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(-14.556042050452705, 6.0282598390762452, 0.0)
    viewCenter134 = NXOpen.Point3d(14.556042050452254, -6.0282598390763082, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint134, viewCenter134)
    
    scaleAboutPoint135 = NXOpen.Point3d(-11.80166641666338, 4.7441914831104084, 0.0)
    viewCenter135 = NXOpen.Point3d(11.801666416662938, -4.7441914831104652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint135, viewCenter135)
    
    scaleAboutPoint136 = NXOpen.Point3d(-14.752083020829167, 5.9302393538880196, 0.0)
    viewCenter136 = NXOpen.Point3d(14.752083020828728, -5.9302393538880773, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint136, viewCenter136)
    
    scaleAboutPoint137 = NXOpen.Point3d(-18.440103776036409, 7.4127991923600351, 0.0)
    viewCenter137 = NXOpen.Point3d(18.440103776035969, -7.4127991923600876, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(-23.050129720045458, 9.2659989904500435, 0.0)
    viewCenter138 = NXOpen.Point3d(23.050129720045014, -9.2659989904501021, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint138, viewCenter138)
    
    scaleAboutPoint139 = NXOpen.Point3d(-28.812662150056759, 11.582498738062572, 0.0)
    viewCenter139 = NXOpen.Point3d(28.812662150056337, -11.582498738062629, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(-36.015827687570891, 14.478123422578214, 0.0)
    viewCenter140 = NXOpen.Point3d(36.015827687570471, -14.478123422578266, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(-45.019784609463557, 18.097654278222791, 0.0)
    viewCenter141 = NXOpen.Point3d(45.019784609463144, -18.09765427822283, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint141, viewCenter141)
    
    scaleAboutPoint142 = NXOpen.Point3d(-56.274730761829375, 22.622067847778489, 0.0)
    viewCenter142 = NXOpen.Point3d(56.274730761828991, -22.622067847778521, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint142, viewCenter142)
    
    scaleAboutPoint143 = NXOpen.Point3d(-70.810811548315144, 41.598430546534829, 0.0)
    viewCenter143 = NXOpen.Point3d(70.810811548314746, -41.598430546534871, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint143, viewCenter143)
    
    scaleAboutPoint144 = NXOpen.Point3d(-88.513514435393887, 51.998038183168539, 0.0)
    viewCenter144 = NXOpen.Point3d(88.513514435393489, -51.998038183168561, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(-110.64189304424227, 64.997547728960697, 0.0)
    viewCenter145 = NXOpen.Point3d(110.64189304424187, -64.997547728960726, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint145, viewCenter145)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = -0.55006710706393014
    rotMatrix11.Xy = 0.83201980544404686
    rotMatrix11.Xz = 0.071897295325775892
    rotMatrix11.Yx = 0.1305339994890381
    rotMatrix11.Yy = 0.17069328848897355
    rotMatrix11.Yz = -0.97663948120184496
    rotMatrix11.Zx = -0.8248557769111563
    rotMatrix11.Zy = -0.52783221255779988
    rotMatrix11.Zz = -0.20249963625306361
    translation11 = NXOpen.Point3d(-162.5273619521314, 142.6962507603007, -11.770725039454716)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 0.57966289472609211)
    
    scaleAboutPoint146 = NXOpen.Point3d(-142.86680083683092, 126.89127997648222, 0.0)
    viewCenter146 = NXOpen.Point3d(142.86680083683061, -126.89127997648227, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint146, viewCenter146)
    
    scaleAboutPoint147 = NXOpen.Point3d(-178.58350104603861, 158.61409997060275, 0.0)
    viewCenter147 = NXOpen.Point3d(178.58350104603821, -158.61409997060281, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint147, viewCenter147)
    
    scaleAboutPoint148 = NXOpen.Point3d(-223.22937630754828, 199.69401075435607, 0.0)
    viewCenter148 = NXOpen.Point3d(223.2293763075478, -199.69401075435607, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(-279.03672038443534, 253.18347792070145, 0.0)
    viewCenter149 = NXOpen.Point3d(279.03672038443489, -253.18347792070145, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    scaleAboutPoint150 = NXOpen.Point3d(-222.51618341199699, 202.54678233656117, 0.0)
    viewCenter150 = NXOpen.Point3d(222.51618341199651, -202.54678233656117, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(-178.01294672959767, 162.03742586924889, 0.0)
    viewCenter151 = NXOpen.Point3d(178.01294672959708, -162.03742586924889, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint151, viewCenter151)
    
    scaleAboutPoint152 = NXOpen.Point3d(-142.41035738367825, 129.62994069539914, 0.0)
    viewCenter152 = NXOpen.Point3d(142.41035738367762, -129.62994069539914, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint152, viewCenter152)
    
    scaleAboutPoint153 = NXOpen.Point3d(-113.92828590694272, 103.70395255631932, 0.0)
    viewCenter153 = NXOpen.Point3d(113.92828590694197, -103.70395255631932, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint153, viewCenter153)
    
    scaleAboutPoint154 = NXOpen.Point3d(-100.19846683610609, 89.974133485482653, 0.0)
    viewCenter154 = NXOpen.Point3d(100.19846683610534, -89.974133485482653, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint154, viewCenter154)
    
    scaleAboutPoint155 = NXOpen.Point3d(-80.158773468884974, 71.97930678838614, 0.0)
    viewCenter155 = NXOpen.Point3d(80.15877346888422, -71.97930678838614, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint155, viewCenter155)
    
    scaleAboutPoint156 = NXOpen.Point3d(-64.12701877510807, 57.583445430708913, 0.0)
    viewCenter156 = NXOpen.Point3d(64.127018775107274, -57.583445430708913, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint156, viewCenter156)
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects5 = [NXOpen.DisplayableObject.Null] * 2 
    objects5[0] = sketch4
    objects5[1] = arc3
    theSession.DisplayManager.BlankObjects(objects5)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    scaleAboutPoint157 = NXOpen.Point3d(-52.498154145919443, 22.285541218637999, 0.0)
    viewCenter157 = NXOpen.Point3d(52.498154145918633, -22.285541218637999, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint157, viewCenter157)
    
    scaleAboutPoint158 = NXOpen.Point3d(-46.066756344567523, 16.631893849077482, 0.0)
    viewCenter158 = NXOpen.Point3d(46.066756344566741, -16.631893849077482, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint158, viewCenter158)
    
    scaleAboutPoint159 = NXOpen.Point3d(-36.853405075654116, 13.305515079261994, 0.0)
    viewCenter159 = NXOpen.Point3d(36.85340507565332, -13.305515079261978, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint159, viewCenter159)
    
    scaleAboutPoint160 = NXOpen.Point3d(-29.482724060523367, 10.644412063409593, 0.0)
    viewCenter160 = NXOpen.Point3d(29.482724060522557, -10.644412063409574, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint160, viewCenter160)
    
    scaleAboutPoint161 = NXOpen.Point3d(-23.58617924841877, 8.5155296507276823, 0.0)
    viewCenter161 = NXOpen.Point3d(23.586179248417977, -8.515529650727661, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint161, viewCenter161)
    
    scaleAboutPoint162 = NXOpen.Point3d(-29.48272406052336, 10.644412063409597, 0.0)
    viewCenter162 = NXOpen.Point3d(29.482724060522571, -10.644412063409577, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint162, viewCenter162)
    
    scaleAboutPoint163 = NXOpen.Point3d(-36.853405075654116, 13.305515079261994, 0.0)
    viewCenter163 = NXOpen.Point3d(36.85340507565332, -13.305515079261978, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint163, viewCenter163)
    
    scaleAboutPoint164 = NXOpen.Point3d(-46.066756344567516, 16.631893849077482, 0.0)
    viewCenter164 = NXOpen.Point3d(46.066756344566734, -16.631893849077461, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint164, viewCenter164)
    
    scaleAboutPoint165 = NXOpen.Point3d(-57.583445430709297, 20.789867311346864, 0.0)
    viewCenter165 = NXOpen.Point3d(57.583445430708529, -20.789867311346839, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint165, viewCenter165)
    
    scaleAboutPoint166 = NXOpen.Point3d(-71.979306788386509, 25.987334139183577, 0.0)
    viewCenter166 = NXOpen.Point3d(71.979306788385756, -25.987334139183545, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint166, viewCenter166)
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId62, "Name Parts Dialog")
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    theSession.DeleteUndoMark(markId63, None)
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    workPart.AssignPermanentName("C:\\Users\\Reader\\Desktop\\嚴\腳\\腳.prt")
    
    theSession.DeleteUndoMark(markId64, None)
    
    theSession.SetUndoMarkName(markId62, "Name Parts")
    
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()