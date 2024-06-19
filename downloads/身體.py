# NX 1872
# Journal created by Reader on Wed Jun 19 20:28:40 2024 台北標準時間

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
    
    rotMatrix1.Xx = 0.98839996117533213
    rotMatrix1.Xy = -0.037763252618032074
    rotMatrix1.Xz = 0.14710354686515101
    rotMatrix1.Yx = 0.0074185799812137758
    rotMatrix1.Yy = 0.97944218795853777
    rotMatrix1.Yz = 0.20158860364130182
    rotMatrix1.Zx = -0.15169206116228784
    rotMatrix1.Zy = -0.1981588685845129
    rotMatrix1.Zz = 0.96836077026159906
    translation1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.90572327300951838)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Sketch")
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    geometry1 = [NXOpen.NXObject.Null] * 1 
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XY plane")
    geometry1[0] = datumPlane1
    plane1 = workPart.Planes.CreatePlane(NXOpen.PlaneTypes.MethodType.Coincident, NXOpen.PlaneTypes.AlternateType.One, origin1, normal1, "", False, False, geometry1)
    
    plane1.Evaluate()
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    point2 = workPart.Points.CreatePoint(point1, NXOpen.Xform.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    sketchInPlaceBuilder1.AxisReference = direction1
    
    sketchInPlaceBuilder1.SketchOrigin = point2
    
    sketchInPlaceBuilder1.AxisOrientation = NXOpen.AxisOrientation.Horizontal
    
    sketchInPlaceBuilder1.PlaneOption = NXOpen.Sketch.PlaneOption.ExistingPlane
    
    sketchInPlaceBuilder1.OriginOption = NXOpen.OriginMethod.SpecifyPoint
    
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
    
    sketchInPlaceBuilder1.Destroy()
    
    sketch1 = nXObject2
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Rectangle...
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId6, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(-46.999999999999901, -41.48158102252772, 0.0)
    endPoint1 = NXOpen.Point3d(47.000000000000099, -41.48158102252772, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(47.000000000000099, -41.48158102252772, 0.0)
    endPoint2 = NXOpen.Point3d(47.0, 41.48158102252772, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(47.0, 41.48158102252772, 0.0)
    endPoint3 = NXOpen.Point3d(-47.0, 41.48158102252772, 0.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(-47.0, 41.48158102252772, 0.0)
    endPoint4 = NXOpen.Point3d(-46.999999999999901, -41.48158102252772, 0.0)
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
    
    geom1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1.Geometry = line1
    geom1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom1)
    
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
    point3 = datumCsys2.FindObject("POINT 1")
    conGeom1_5.Geometry = point3
    conGeom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_5.SplineDefiningPointIndex = 0
    conGeom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_5.Geometry = line1
    conGeom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_5, conGeom2_5)
    
    conGeom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_6.Geometry = point3
    conGeom1_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_6.SplineDefiningPointIndex = 0
    conGeom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_6.Geometry = line2
    conGeom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_6, conGeom2_6)
    
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
    dimOrigin1 = NXOpen.Point3d(9.9475983006414026e-14, -51.418390938093864, 0.0)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression1 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
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
    dimOrigin2 = NXOpen.Point3d(56.936809915566187, 1.1914612581449168e-14, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression2 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
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
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId7, "Rapid Dimension Dialog")
    
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
    
    point4 = NXOpen.Point3d(-14.606190500890058, 41.48158102252772, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(line3, workPart.ModelingViews.WorkView, point4)
    
    point1_1 = NXOpen.Point3d(-47.0, 41.48158102252772, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line3, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(47.0, 41.48158102252772, 0.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line3, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
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
    point5 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point5
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
    
    point6 = NXOpen.Point3d(-5.5503523903382241, 68.649095354183217, 0.0)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point6)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = True
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId8, None)
    
    theSession.SetUndoMarkName(markId7, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId7, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId9, "Rapid Dimension Dialog")
    
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
    
    expression3 = workPart.Expressions.FindObject("p0")
    expression3.SetFormula("50")
    
    theSession.SetUndoMarkVisibility(markId9, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.53191489361702127)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId10, None)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId9, "Edit Driving Value")
    
    point7 = NXOpen.Point3d(-24.999999999999982, 8.7637143005340228, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line4, workPart.ModelingViews.WorkView, point7)
    
    point1_3 = NXOpen.Point3d(-25.0, 22.064670756663681, 0.0)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line4, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(-24.999999999999947, -22.064670756663681, 0.0)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line4, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
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
    sketchRapidDimensionBuilder2.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point9 = NXOpen.Point3d(-44.402819122705743, 3.7976095302313948, 0.0)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point9)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = True
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject4 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId12, None)
    
    theSession.SetUndoMarkName(markId11, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId11, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId13, "Rapid Dimension Dialog")
    
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
    
    expression4 = workPart.Expressions.FindObject("p1")
    expression4.SetFormula("50")
    
    theSession.SetUndoMarkVisibility(markId13, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId13, "Edit Driving Value")
    
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId15, None)
    
    theSession.DeleteUndoMark(markId15, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.99874156166697503
    rotMatrix2.Xy = 0.00452178622814419
    rotMatrix2.Xz = 0.049948437896683393
    rotMatrix2.Yx = -0.049087978608718115
    rotMatrix2.Yy = -0.11598941930146499
    rotMatrix2.Yz = 0.99203670545308864
    rotMatrix2.Zx = 0.0102792682191829
    rotMatrix2.Zy = -0.99324015628618967
    rotMatrix2.Zz = -0.11562148842435023
    translation2 = NXOpen.Point3d(-0.078437481088053929, 15.570189794061656, 14.426040097399706)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.90572327300951838)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.99698891367200904
    rotMatrix3.Xy = -0.051955442499884187
    rotMatrix3.Xz = 0.057565076302808507
    rotMatrix3.Yx = -0.023072559917371772
    rotMatrix3.Yy = 0.50997475890468058
    rotMatrix3.Yz = 0.8598798766449709
    rotMatrix3.Zx = -0.074032175396689701
    rotMatrix3.Zy = -0.85861887777683465
    rotMatrix3.Zz = 0.50724043582041078
    translation3 = NXOpen.Point3d(0.71723348084269389, 6.8207987945046398, 11.597404336246599)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.90572327300951838)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit1 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("100")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId17, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.98028870700453785
    rotMatrix4.Xy = 0.14158216511421315
    rotMatrix4.Xz = 0.13779891669001251
    rotMatrix4.Yx = -0.13650828203553725
    rotMatrix4.Yy = -0.018835472826781319
    rotMatrix4.Yz = 0.99045984971582357
    rotMatrix4.Zx = 0.14282695773233994
    rotMatrix4.Zy = -0.98974729880154588
    rotMatrix4.Zz = 0.00086293682342857318
    translation4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.90572327300951838)
    
    extrudeBuilder1.Limits.SymmetricOption = True
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("7.5")
    
    extrudeBuilder1.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    targetBodies3 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = workPart.Features.FindObject("SKETCH(1)")
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(-17.181035933086736, -24.999999999999819, -5.5129512066542929e-15)
    section1.AddToSection(rules1, line1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId19, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    unit2 = extrudeBuilder1.Offset.StartOffset.Units
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.DeleteUndoMark(markId18, None)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("180")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("180")
    
    scaleAboutPoint1 = NXOpen.Point3d(-27.459638141673285, 33.0099905320115, 0.0)
    viewCenter1 = NXOpen.Point3d(27.459638141673285, -33.0099905320115, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(-5.1413790563133013, 30.147177193837027, 0.0)
    viewCenter2 = NXOpen.Point3d(5.1413790563133013, -30.147177193837049, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(-4.1131032450506417, 24.117741755069627, 0.0)
    viewCenter3 = NXOpen.Point3d(4.1131032450506417, -24.117741755069659, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(-3.2904825960405004, 19.294193404055701, 0.0)
    viewCenter4 = NXOpen.Point3d(3.2904825960405262, -19.294193404055736, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(-2.6323860768323906, 15.435354723244552, 0.0)
    viewCenter5 = NXOpen.Point3d(2.6323860768324314, -15.435354723244602, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(-2.1059088614659207, 12.348283778595633, 0.0)
    viewCenter6 = NXOpen.Point3d(2.1059088614659371, -12.34828377859569, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(-1.8378840972793407, 9.8020485188231881, 0.0)
    viewCenter7 = NXOpen.Point3d(1.8378840972793669, -9.8020485188232467, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(-2.3930782516658198, 12.156837518462366, 0.0)
    viewCenter8 = NXOpen.Point3d(2.3930782516658358, -12.156837518462423, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-2.9913478145822645, 15.196046898077958, 0.0)
    viewCenter9 = NXOpen.Point3d(2.9913478145823054, -15.196046898078018, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-3.739184768227843, 18.995058622597469, 0.0)
    viewCenter10 = NXOpen.Point3d(3.7391847682278683, -18.995058622597522, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-4.6739809602848199, 23.743823278246822, 0.0)
    viewCenter11 = NXOpen.Point3d(4.6739809602848199, -23.743823278246886, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-5.8424762003560238, 29.679779097808545, 0.0)
    viewCenter12 = NXOpen.Point3d(5.8424762003560238, -29.679779097808602, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-6.4267238203916266, 37.391847682278481, 0.0)
    viewCenter13 = NXOpen.Point3d(6.4267238203916266, -37.391847682278531, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-8.3985595380117939, 46.009500077803601, 0.0)
    viewCenter14 = NXOpen.Point3d(8.3985595380117939, -46.009500077803658, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-10.498199422514741, 57.511875097254489, 0.0)
    viewCenter15 = NXOpen.Point3d(10.498199422514741, -57.511875097254567, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-13.122749278143427, 71.889843871568161, 0.0)
    viewCenter16 = NXOpen.Point3d(13.122749278143427, -71.889843871568161, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-16.403436597679406, 89.862304839460208, 0.0)
    viewCenter17 = NXOpen.Point3d(16.403436597679164, -89.862304839460208, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-20.504295747099256, 112.32788104932524, 0.0)
    viewCenter18 = NXOpen.Point3d(20.504295747098951, -112.32788104932524, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-25.630369683874065, 140.40985131165655, 0.0)
    viewCenter19 = NXOpen.Point3d(25.630369683873688, -140.40985131165655, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-32.037962104842585, 175.51231413957069, 0.0)
    viewCenter20 = NXOpen.Point3d(32.037962104842109, -175.51231413957069, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-25.630369683874065, 140.40985131165655, 0.0)
    viewCenter21 = NXOpen.Point3d(25.630369683873688, -140.40985131165655, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.99907179629506238
    rotMatrix5.Xy = 0.022733090200186275
    rotMatrix5.Xz = 0.03658896633828701
    rotMatrix5.Yx = -0.036060804062010614
    rotMatrix5.Yy = -0.023224349909860782
    rotMatrix5.Yz = 0.99907970051525874
    rotMatrix5.Zx = 0.02356192390606867
    rotMatrix5.Zy = -0.99947177858166925
    rotMatrix5.Zz = -0.022383019470797641
    translation5 = NXOpen.Point3d(-7.9373885465333025, 78.83383548679447, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.29678740209975907)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("80")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("80")
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature1 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId17, "Extrude")
    
    expression7 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression5)
    
    workPart.Expressions.Delete(expression6)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.97775846540435196
    rotMatrix6.Xy = -0.20595627252536272
    rotMatrix6.Xz = 0.039628236619663477
    rotMatrix6.Yx = -0.006562872321005702
    rotMatrix6.Yy = 0.1588082910201781
    rotMatrix6.Yz = 0.98728762547200322
    rotMatrix6.Zx = -0.20963137178634234
    rotMatrix6.Zy = -0.96558890865145297
    rotMatrix6.Zz = 0.15392448620108318
    translation6 = NXOpen.Point3d(-7.9373885465333025, 78.83383548679447, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.29678740209975907)
    
    scaleAboutPoint22 = NXOpen.Point3d(45.466047091393399, 79.342709630078915, 0.0)
    viewCenter22 = NXOpen.Point3d(-45.466047091393705, -79.342709630078915, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(34.54528087826445, 66.86183395793168, 0.0)
    viewCenter23 = NXOpen.Point3d(-34.545280878264833, -66.86183395793168, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(40.395691349583338, 80.791382699167556, 0.0)
    viewCenter24 = NXOpen.Point3d(-40.395691349583814, -80.791382699167329, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(32.316553079666669, 64.633106159334048, 0.0)
    viewCenter25 = NXOpen.Point3d(-32.316553079667045, -64.633106159333849, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(25.853242463733334, 51.706484927467237, 0.0)
    viewCenter26 = NXOpen.Point3d(-25.85324246373364, -51.706484927467088, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(20.682593970986666, 41.365187941973787, 0.0)
    viewCenter27 = NXOpen.Point3d(-20.682593970986908, -41.365187941973666, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(16.546075176789234, 33.092150353579029, 0.0)
    viewCenter28 = NXOpen.Point3d(-16.546075176789525, -33.09215035357888, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(12.323973235125814, 13.236860141431663, 0.0)
    viewCenter29 = NXOpen.Point3d(-12.323973235126127, -13.236860141431507, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.92840397059363178
    rotMatrix7.Xy = -0.37154868850608125
    rotMatrix7.Xz = 0.0041999351645270995
    rotMatrix7.Yx = 0.00016453183162074784
    rotMatrix7.Yy = 0.011714208864135489
    rotMatrix7.Yz = 0.99993137276513189
    rotMatrix7.Zx = -0.37157238906470352
    rotMatrix7.Zy = -0.92833956577326515
    rotMatrix7.Zz = 0.010936649608082999
    translation7 = NXOpen.Point3d(-17.558182409295355, 58.419936939206416, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 0.72457861840761506)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane2
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId22, "Create Sketch Dialog")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression9)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression8)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane2.DestroyPlane()
    
    theSession.UndoToMark(markId22, None)
    
    theSession.DeleteUndoMark(markId22, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 5 
    objects1[0] = sketch2
    objects1[1] = line1
    objects1[2] = line2
    objects1[3] = line3
    objects1[4] = line4
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.76433089924142716
    rotMatrix8.Xy = -0.64457848178642652
    rotMatrix8.Xz = 0.017800485462270258
    rotMatrix8.Yx = 0.039431284308075125
    rotMatrix8.Yy = 0.074274871627349609
    rotMatrix8.Yz = 0.99645793552088957
    rotMatrix8.Zx = -0.64361747201470743
    rotMatrix8.Zy = -0.7609216939098542
    rotMatrix8.Zz = 0.082187136796162186
    translation8 = NXOpen.Point3d(-17.558182409295355, 58.419936939206416, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 0.72457861840761506)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.88053902423058972
    rotMatrix9.Xy = -0.46473444152565974
    rotMatrix9.Xz = -0.093128543781552428
    rotMatrix9.Yx = 0.0127846779404274
    rotMatrix9.Yy = -0.17312500802864811
    rotMatrix9.Yz = 0.98481687820885588
    rotMatrix9.Zx = -0.47380120178931395
    rotMatrix9.Zy = -0.86836031142314996
    rotMatrix9.Zz = -0.14650184547672856
    translation9 = NXOpen.Point3d(-17.558182409295355, 58.419936939206416, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 0.72457861840761506)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.91453613768534081
    rotMatrix10.Xy = -0.31074164652916147
    rotMatrix10.Xz = -0.25896579306912793
    rotMatrix10.Yx = -0.30137239013223865
    rotMatrix10.Yy = -0.95045759566643817
    rotMatrix10.Yz = 0.076190821664744113
    rotMatrix10.Zx = -0.26981166641484883
    rotMatrix10.Zy = 0.0083658802473867179
    rotMatrix10.Zz = -0.96287677130260096
    translation10 = NXOpen.Point3d(-17.558182409295355, 58.419936939206416, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 0.72457861840761506)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.PlaneReference = plane3
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId24, "Create Sketch Dialog")
    
    sketchInPlaceBuilder3.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression11)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression10)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane3.DestroyPlane()
    
    theSession.UndoToMark(markId24, None)
    
    theSession.DeleteUndoMark(markId24, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder4.PlaneReference = plane4
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId25, "Create Sketch Dialog")
    
    sketchInPlaceBuilder4.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
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
        
    plane4.DestroyPlane()
    
    theSession.UndoToMark(markId25, None)
    
    theSession.DeleteUndoMark(markId25, None)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.93245167822631969
    rotMatrix11.Xy = -0.14701997107055695
    rotMatrix11.Xz = -0.33002878038033573
    rotMatrix11.Yx = -0.024470903634124491
    rotMatrix11.Yy = -0.93706354274268511
    rotMatrix11.Yz = 0.34830028960346465
    rotMatrix11.Zx = -0.36046503665161311
    rotMatrix11.Zy = -0.31669708708628908
    rotMatrix11.Zz = -0.87736418457947685
    translation11 = NXOpen.Point3d(-17.558182409295355, 58.419936939206416, -2.9247832021614677)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 0.72457861840761506)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    revolveBuilder1.BooleanOperation.SetTargetBodies(targetBodies4)
    
    revolveBuilder1.Offset.StartOffset.SetFormula("0")
    
    revolveBuilder1.Offset.EndOffset.SetFormula("5")
    
    revolveBuilder1.Tolerance = 0.01
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder1.Section = section2
    
    smartVolumeProfileBuilder2 = revolveBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId26, "Revolve Dialog")
    
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
    
    scalar1 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude1 = feature1
    edge1 = extrude1.FindObject("EDGE * 120 * 170 {(-25,25,-80)(-25,0,-80)(-25,-25,-80) EXTRUDE(2)}")
    point10 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge2 = extrude1.FindObject("EDGE * 120 * 140 {(-25,-25,-80)(0,-25,-80)(25,-25,-80) EXTRUDE(2)}")
    direction3 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 120 {(0,0,-80) EXTRUDE(2)}")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point10, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem1
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature2 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder5 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder5.Csystem = cartesianCoordinateSystem1
    
    sketchInPlaceBuilder5.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject5 = sketchInPlaceBuilder5.Commit()
    
    sketchInPlaceBuilder5.Destroy()
    
    sketch3 = nXObject5
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId28, None, True)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint30 = NXOpen.Point3d(23.917636945207295, 21.178976226290661, 0.0)
    viewCenter30 = NXOpen.Point3d(-23.917636945207551, -21.178976226290501, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(29.897046181509193, 26.017276829710458, 0.0)
    viewCenter31 = NXOpen.Point3d(-29.897046181509392, -26.017276829710298, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(37.371307726886492, 32.521596037138067, 0.0)
    viewCenter32 = NXOpen.Point3d(-37.371307726886691, -32.521596037137869, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(29.897046181509193, 26.017276829710458, 0.0)
    viewCenter33 = NXOpen.Point3d(-29.897046181509392, -26.017276829710298, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(23.917636945207292, 20.813821463768399, 0.0)
    viewCenter34 = NXOpen.Point3d(-23.917636945207548, -20.813821463768207, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(19.134109556165836, 16.65105717101472, 0.0)
    viewCenter35 = NXOpen.Point3d(-19.134109556166063, -16.651057171014592, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(15.307287644932629, 13.320845736811776, 0.0)
    viewCenter36 = NXOpen.Point3d(-15.307287644932874, -13.320845736811634, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(12.245830115946104, 10.656676589449422, 0.0)
    viewCenter37 = NXOpen.Point3d(-12.245830115946315, -10.656676589449308, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    expression14 = workPart.Expressions.CreateSystemExpression("7.5")
    
    workPart.Expressions.Delete(expression14)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    expression15 = workPart.Expressions.CreateSystemExpression("15")
    
    workPart.Expressions.Delete(expression15)
    
    theSession.DeleteUndoMark(markId32, "Curve")
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId34, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(-25.000000000000007, 0.0, -80.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 11.519905779692367, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = arc1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_5.Geometry = edge1
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = arc1
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(-25.000000000000007, -1.6958822255899537, -80.0)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression16 = sketchDimensionalConstraint3.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId35, "Rapid Dimension Dialog")
    
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
    
    point1_5 = NXOpen.Point3d(-25.000000000000007, 0.0, -80.0)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(-25.000000000000007, 0.0, -80.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    point1_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
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
    
    point12 = NXOpen.Point3d(-39.222047690716664, -19.05504572687957, -80.0)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point12)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = False
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject6 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId36, None)
    
    theSession.SetUndoMarkName(markId35, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId35, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId37, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    expression17 = workPart.Expressions.FindObject("p8")
    expression17.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId37, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId38, None)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId37, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Line...
    # ----------------------------------------------
    sketchRapidDimensionBuilder5.Destroy()
    
    theSession.UndoToMark(markId39, None)
    
    theSession.DeleteUndoMark(markId39, None)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId41, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint5 = NXOpen.Point3d(-24.870519527180736, 7.4988822371843185, -80.0)
    endPoint5 = NXOpen.Point3d(-25.000000000000004, 0.0, -80.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_7.Geometry = line5
    conGeom1_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_7.SplineDefiningPointIndex = 0
    conGeom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_7.Geometry = arc1
    conGeom2_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_7.SplineDefiningPointIndex = 0
    help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help1.Point.X = -24.870519527180736
    help1.Point.Y = 7.4988822371843185
    help1.Point.Z = -80.0
    help1.Parameter = 0.0
    sketchHelpedGeometricConstraint1 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_7, conGeom2_7, help1)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line5
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = arc1
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = line5
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_3.Geometry = line5
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 0.0
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(-19.848371324457123, 3.6616076656260876, -80.0)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_4, dimObject2_3, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint4
    dimension4 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression18 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis2 = workPart.Datums.FindObject("SKETCH(3:1B) X axis")
    dimObject1_5.Geometry = datumAxis2
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 3.5749999999999922
    dimObject1_5.HelpPoint.Y = 24.999999999999993
    dimObject1_5.HelpPoint.Z = -80.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line5
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = -25.000000000000004
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = -80.0
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(-8.7323138099083106, 8.8881844417405453, -80.0)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_5, dimObject2_4, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension5 = sketchDimensionalConstraint5.AssociatedDimension
    
    expression19 = sketchDimensionalConstraint5.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Edit->Curve->Quick Extend...
    # ----------------------------------------------
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchQuickExtendBuilder1 = workPart.Sketches.CreateQuickExtendBuilder()
    
    theSession.SetUndoMarkName(markId42, "Quick Extend Dialog")
    
    # ----------------------------------------------
    #   Menu: Edit->Curve->Quick Trim...
    # ----------------------------------------------
    sketchQuickExtendBuilder1.Destroy()
    
    theSession.UndoToMark(markId42, None)
    
    theSession.DeleteUndoMark(markId42, None)
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchQuickTrimBuilder1 = workPart.Sketches.CreateQuickTrimBuilder()
    
    theSession.SetUndoMarkName(markId43, "Quick Trim Dialog")
    
    point13 = NXOpen.Point3d(-19.882982773010383, -5.4712984687724679, -80.0)
    added1 = sketchQuickTrimBuilder1.TrimmedCurves.Add(arc1, workPart.ModelingViews.WorkView, point13)
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Quick Trim")
    
    added2 = sketchQuickTrimBuilder1.BoundaryObjects.Add(line5)
    
    sketchQuickTrimBuilder1.ExtendBound = False
    
    nXObject7 = sketchQuickTrimBuilder1.Commit()
    
    sketchQuickTrimBuilder1.ExtendBound = True
    
    sketchQuickTrimBuilder1.BoundaryObjects.Clear()
    
    sketchQuickTrimBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId44, None)
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Quick Trim")
    
    sketchQuickTrimBuilder2 = workPart.Sketches.CreateQuickTrimBuilder()
    
    sketchQuickTrimBuilder2.ExtendBound = True
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    sketchQuickTrimBuilder2.Destroy()
    
    theSession.DeleteUndoMark(markId45, None)
    
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Arc...
    # ----------------------------------------------
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId48, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(-146.48351209786509, -1.1725697057357143, -80.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 121.48917083981988, ( 355.90933951035424 * math.pi/180.0 ), ( 362.98464687592241 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_8.Geometry = arc2
    conGeom1_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_8.SplineDefiningPointIndex = 0
    conGeom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_8.Geometry = arc1
    conGeom2_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_8.SplineDefiningPointIndex = 0
    help2 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help2.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help2.Point.X = -25.303844137511238
    help2.Point.Y = 7.4938427218684041
    help2.Point.Z = -80.0
    help2.Parameter = 0.0
    sketchHelpedGeometricConstraint2 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_8, conGeom2_8, help2)
    
    geom2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2.Geometry = arc2
    geom2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2.SplineDefiningPointIndex = 0
    try:
        # Invalid object type
        sketchGeometricConstraint14 = theSession.ActiveSketch.CreateVerticalConstraint(geom2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(875033)
        
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = arc2
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = arc1
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    conGeom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_9.Geometry = arc2
    conGeom1_9.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_9.SplineDefiningPointIndex = 0
    conGeom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_9.Geometry = arc1
    conGeom2_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_9.SplineDefiningPointIndex = 0
    help3 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help3.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help3.Point.X = -25.159138526620207
    help3.Point.Y = -7.4983114718811947
    help3.Point.Z = -80.0
    help3.Parameter = 0.0
    sketchHelpedGeometricConstraint3 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_9, conGeom2_9, help3)
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = arc2
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(-85.733396671449995, -2.6572077212296583, -80.0)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateRadialDimension(dimObject1_6, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension6 = sketchDimensionalConstraint6.AssociatedDimension
    
    expression20 = sketchDimensionalConstraint6.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Arc
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled2, undoUnavailable2 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId47, "Curve")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    theSession.DeleteUndoMark(markId49, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Settings...
    # ----------------------------------------------
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId50, "Sketch Settings Dialog")
    
    theSession.UndoToMark(markId50, None)
    
    theSession.DeleteUndoMark(markId50, None)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Edit->Object Display...
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Edit->Settings...
    # ----------------------------------------------
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId51, "Sketch Settings Dialog")
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.UndoToMark(markId51, None)
    
    theSession.DeleteUndoMark(markId51, None)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId53, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix3 = theSession.ActiveSketch.Orientation
    
    center3 = NXOpen.Point3d(-25.000000000000007, 0.0, -80.0)
    arc3 = workPart.Curves.CreateArc(center3, nXMatrix3, 15.105140702868459, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = arc3
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = edge1
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = arc3
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = 0.0
    dimObject1_7.HelpPoint.Y = 0.0
    dimObject1_7.HelpPoint.Z = 0.0
    dimObject1_7.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(-25.000000000000007, -1.6958822255899537, -80.0)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_7, dimOrigin7, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension7 = sketchDimensionalConstraint7.AssociatedDimension
    
    expression21 = sketchDimensionalConstraint7.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
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
    
    datumCsys3 = feature2
    nErrs1 = theSession.UpdateManager.AddToDeleteList(datumCsys3)
    
    revolveBuilder1.Destroy()
    
    section2.Destroy()
    
    try:
        # Undo mark is missing
        theSession.UndoToMark(markId26, None)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1055008)
        
    theSession.DeleteUndoMark(markId26, None)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects2 = [NXOpen.DisplayableObject.Null] * 8 
    objects2[0] = point1
    cartesianCoordinateSystem2 = datumCsys1.FindObject("CSYSTEM 1")
    objects2[1] = cartesianCoordinateSystem2
    objects2[2] = datumAxis1
    datumAxis3 = workPart.Datums.FindObject("DATUM_CSYS(0) Y axis")
    objects2[3] = datumAxis3
    datumAxis4 = workPart.Datums.FindObject("DATUM_CSYS(0) Z axis")
    objects2[4] = datumAxis4
    objects2[5] = datumPlane1
    datumPlane2 = workPart.Datums.FindObject("DATUM_CSYS(0) YZ plane")
    objects2[6] = datumPlane2
    datumPlane3 = workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane")
    objects2[7] = datumPlane3
    theSession.DisplayManager.BlankObjects(objects2)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects3 = [NXOpen.DisplayableObject.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    objects3[0] = body1
    theSession.DisplayManager.BlankObjects(objects3)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show")
    
    objects4 = [NXOpen.DisplayableObject.Null] * 8 
    objects4[0] = point1
    objects4[1] = cartesianCoordinateSystem2
    objects4[2] = datumAxis1
    objects4[3] = datumAxis3
    objects4[4] = datumAxis4
    objects4[5] = datumPlane1
    objects4[6] = datumPlane2
    objects4[7] = datumPlane3
    theSession.DisplayManager.ShowObjects(objects4, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show")
    
    objects5 = [NXOpen.DisplayableObject.Null] * 5 
    objects5[0] = sketch2
    objects5[1] = line1
    objects5[2] = line2
    objects5[3] = line3
    objects5[4] = line4
    theSession.DisplayManager.ShowObjects(objects5, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show")
    
    objects6 = [NXOpen.DisplayableObject.Null] * 1 
    objects6[0] = body1
    theSession.DisplayManager.ShowObjects(objects6, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(extrude1)
    
    section1.PrepareMappingData()
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder2.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("80")
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId60, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = 0.98133169474953863
    rotMatrix12.Xy = 0.020814151792917384
    rotMatrix12.Xz = 0.19119329477034186
    rotMatrix12.Yx = -0.033070498281721886
    rotMatrix12.Yy = -0.96105686326235562
    rotMatrix12.Yz = 0.27436480772817734
    rotMatrix12.Zx = 0.1894582989034686
    rotMatrix12.Zy = -0.27556573927370281
    rotMatrix12.Zz = -0.94242722600481998
    translation12 = NXOpen.Point3d(10.398375991207869, 11.922327340080326, -74.220806105382593)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation12, 1.7689907675967165)
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId61, None)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId62, None)
    
    expression24 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression22)
    
    workPart.Expressions.Delete(expression23)
    
    theSession.UndoToMark(markId60, None)
    
    theSession.DeleteUndoMark(markId60, None)
    
    theSession.DeleteUndoMark(markId60, None)
    
    theSession.UndoToMarkWithStatus(markId59, None)
    
    theSession.DeleteUndoMarksUpToMark(markId59, None, False)
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = 0.99916134140150659
    rotMatrix13.Xy = -0.026772163160219353
    rotMatrix13.Xz = -0.030981690213139096
    rotMatrix13.Yx = -0.022742368018979078
    rotMatrix13.Yy = -0.99204507559430533
    rotMatrix13.Yz = 0.12381176311634172
    rotMatrix13.Zx = -0.034049941932838321
    rotMatrix13.Zy = -0.12300333031593197
    rotMatrix13.Zz = -0.9918219508488183
    translation13 = NXOpen.Point3d(10.398375991207869, 11.922327340080326, -74.220806105382593)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation13, 1.7689907675967165)
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = 0.96680576624372594
    rotMatrix14.Xy = -0.057065038413148604
    rotMatrix14.Xz = -0.24905861107134053
    rotMatrix14.Yx = -0.011877793441450801
    rotMatrix14.Yy = -0.9837252347115949
    rotMatrix14.Yz = 0.17928630905503579
    rotMatrix14.Zx = -0.25523622074627622
    rotMatrix14.Zy = -0.17037677066584309
    rotMatrix14.Zz = -0.95174903605763173
    translation14 = NXOpen.Point3d(10.398375991207869, 11.922327340080326, -74.220806105382593)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation14, 1.7689907675967165)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder2 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder2.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder2.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = NXOpen.Body.Null
    revolveBuilder2.BooleanOperation.SetTargetBodies(targetBodies5)
    
    revolveBuilder2.Offset.StartOffset.SetFormula("0")
    
    revolveBuilder2.Offset.EndOffset.SetFormula("5")
    
    revolveBuilder2.Tolerance = 0.01
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder2.Section = section3
    
    smartVolumeProfileBuilder3 = revolveBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId63, "Revolve Dialog")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint3 = [None] * 3 
    starthelperpoint3[0] = 0.0
    starthelperpoint3[1] = 0.0
    starthelperpoint3[2] = 0.0
    revolveBuilder2.SetStartLimitHelperPoint(starthelperpoint3)
    
    endhelperpoint3 = [None] * 3 
    endhelperpoint3[0] = 0.0
    endhelperpoint3[1] = 0.0
    endhelperpoint3[2] = 0.0
    revolveBuilder2.SetEndLimitHelperPoint(endhelperpoint3)
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar2 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point14 = workPart.Points.CreatePoint(edge2, scalar2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction4 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction4, point14, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder2 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder2.Csys = cartesianCoordinateSystem3
    
    datumCsysBuilder2.DisplayScaleFactor = 1.25
    
    feature3 = datumCsysBuilder2.CommitFeature()
    
    datumCsysBuilder2.Destroy()
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder6 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder6.Csystem = cartesianCoordinateSystem3
    
    sketchInPlaceBuilder6.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject8 = sketchInPlaceBuilder6.Commit()
    
    sketchInPlaceBuilder6.Destroy()
    
    sketch4 = nXObject8
    sketch4.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId65, None, True)
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint38 = NXOpen.Point3d(7.2540184503619187, -31.259584662384771, 0.0)
    viewCenter38 = NXOpen.Point3d(-7.2540184503621408, 31.259584662384874, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(8.5066453477182407, -39.074480827980977, 0.0)
    viewCenter39 = NXOpen.Point3d(-8.5066453477184538, 39.074480827981077, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(20.682365749260111, -45.571314362776867, 0.0)
    viewCenter40 = NXOpen.Point3d(-20.682365749260438, 45.571314362776945, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(16.545892599408088, -36.457051490221474, 0.0)
    viewCenter41 = NXOpen.Point3d(-16.545892599408365, 36.457051490221573, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(13.236714079526447, -29.165641192177183, 0.0)
    viewCenter42 = NXOpen.Point3d(-13.236714079526735, 29.165641192177262, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint42, viewCenter42)
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    expression25 = workPart.Expressions.CreateSystemExpression("15")
    
    workPart.Expressions.Delete(expression25)
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId71, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix4 = theSession.ActiveSketch.Orientation
    
    center4 = NXOpen.Point3d(-24.85596986985399, -0.87371492807488949, -80.0)
    arc4 = workPart.Curves.CreateArc(center4, nXMatrix4, 9.1274215358135429, ( 90.90416127556891 * math.pi/180.0 ), ( 269.09583872443108 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_10.Geometry = arc4
    conGeom1_10.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_10.SplineDefiningPointIndex = 0
    conGeom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_10.Geometry = edge1
    conGeom2_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_10.SplineDefiningPointIndex = 0
    help4 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help4.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help4.Point.X = -25.000000000000007
    help4.Point.Y = 8.2525701438502139
    help4.Point.Z = -80.0
    help4.Parameter = 0.0
    sketchHelpedGeometricConstraint4 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_10, conGeom2_10, help4)
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_8.Geometry = arc4
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = 0.0
    dimObject1_8.HelpPoint.Y = 0.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(-29.154494106336017, 1.1734284318906136, -80.0)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateRadialDimension(dimObject1_8, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension8 = sketchDimensionalConstraint8.AssociatedDimension
    
    expression26 = sketchDimensionalConstraint8.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.ActiveSketch.Update()
    
    theSession.DeleteUndoMark(markId72, "Curve")
    
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    radiusDimension1 = dimension8
    sketchRadialDimensionBuilder1 = workPart.Sketches.CreateRadialDimensionBuilder(radiusDimension1)
    
    sketchRadialDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Inferred
    
    sketchRadialDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId73, "Radial Dimension Dialog")
    
    sketchRadialDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits119 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRadialDimensionBuilder1.Style.OrdinateStyle.DoglegCreationOption = NXOpen.Annotations.OrdinateDoglegCreationOption.No
    
    dimensionlinearunits121 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRadialDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRadialDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRadialDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRadialDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    dimensionlinearunits125 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits129 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits135 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRadialDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    # ----------------------------------------------
    #   Dialog Begin Radial Dimension
    # ----------------------------------------------
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Radial Dimension")
    
    theSession.DeleteUndoMark(markId74, None)
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Radial Dimension")
    
    sketchRadialDimensionBuilder1.Driving.ExpressionValue.SetFormula("7.5")
    
    sketchRadialDimensionBuilder1.Driving.ExpressionValue.SetFormula("7.5")
    
    sketchRadialDimensionBuilder1.Driving.ExpressionMode = NXOpen.Annotations.DrivingValueBuilder.DrivingExpressionMode.KeepExpression
    
    nXObject9 = sketchRadialDimensionBuilder1.Commit()
    
    point1_8 = NXOpen.Point3d(-24.855969869853986, -2.5013831060914775, -80.0)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRadialDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc4, NXOpen.View.Null, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    theSession.SetUndoMarkName(markId75, "Radial Dimension - =")
    
    theSession.SetUndoMarkVisibility(markId75, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId73, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Radial Dimension")
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Radial Dimension")
    
    nXObject10 = sketchRadialDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId77, None)
    
    theSession.SetUndoMarkName(markId73, "Radial Dimension")
    
    expression27 = sketchRadialDimensionBuilder1.Driving.ExpressionValue
    sketchRadialDimensionBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId76, None)
    
    theSession.SetUndoMarkVisibility(markId73, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.DeleteUndoMark(markId75, None)
    
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    geom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_9.Geometry = arc4
    geom1_9.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_9.SplineDefiningPointIndex = 0
    geom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_9.Geometry = edge1
    geom2_9.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_9, geom2_9)
    
    theSession.SetUndoMarkVisibility(markId79, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    horizontalDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    theSession.UpdateManager.LogForUpdate(horizontalDimension1)
    
    horizontalDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    theSession.UpdateManager.LogForUpdate(horizontalDimension2)
    
    center5 = NXOpen.Point3d(-25.000000000000007, 0.0, -80.0)
    arc4.SetParameters(7.5000000000000018, center5, ( 91.503178734768767 * math.pi/180.0 ), ( 270.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint4 = theSession.ActiveSketch.FindObject("ENTITY 243 4 1")
    sketchHelpedDimensionalConstraint4.Refresh()
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId79)
    
    geoms3 = [NXOpen.SmartObject.Null] * 1 
    geoms3[0] = arc4
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 1 
    geoms4[0] = arc4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms4)
    
    geoms5 = [NXOpen.SmartObject.Null] * 1 
    geoms5[0] = arc4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms5)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Line...
    # ----------------------------------------------
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId81, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint6 = NXOpen.Point3d(-25.196743064829413, -7.4974190336702904, -80.0)
    endPoint6 = NXOpen.Point3d(-25.000000000000032, 7.5, -80.0)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_10.Geometry = line6
    geom1_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_10.SplineDefiningPointIndex = 0
    geom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_10.Geometry = arc4
    geom2_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint18 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_10, geom2_10)
    
    geom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_11.Geometry = line6
    geom1_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_11.SplineDefiningPointIndex = 0
    geom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_11.Geometry = arc4
    geom2_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint19 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_11, geom2_11)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId64, None)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    starthelperpoint4 = [None] * 3 
    starthelperpoint4[0] = 0.0
    starthelperpoint4[1] = 0.0
    starthelperpoint4[2] = 0.0
    revolveBuilder2.SetStartLimitHelperPoint(starthelperpoint4)
    
    endhelperpoint4 = [None] * 3 
    endhelperpoint4[0] = 0.0
    endhelperpoint4[1] = 0.0
    endhelperpoint4[2] = 0.0
    revolveBuilder2.SetEndLimitHelperPoint(endhelperpoint4)
    
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 2 
    curves1[0] = line6
    curves1[1] = arc4
    seedPoint1 = NXOpen.Point3d(-27.565365931829614, 0.033653654319050839, -80.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch4, curves1, seedPoint1, 0.01)
    
    section3.AllowSelfIntersection(False)
    
    rules2 = [None] * 1 
    rules2[0] = regionBoundaryRule1
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section3.AddToSection(rules2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId83, None)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs1 = section3.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression28)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    revolveBuilder2.Section = section3
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    scaleAboutPoint43 = NXOpen.Point3d(18.546356450409995, 1.7948086887494186, 0.0)
    viewCenter43 = NXOpen.Point3d(-18.546356450410251, -1.7948086887493164, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(23.182945563012559, 2.2435108609367576, 0.0)
    viewCenter44 = NXOpen.Point3d(-23.182945563012783, -2.2435108609366456, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(28.978681953765697, 2.8043885761709468, 0.0)
    viewCenter45 = NXOpen.Point3d(-28.978681953765939, -2.8043885761708269, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(36.223352442207172, 3.5054857202136582, 0.0)
    viewCenter46 = NXOpen.Point3d(-36.223352442207393, -3.5054857202135339, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(45.279190552758962, 4.3818571502670727, 0.0)
    viewCenter47 = NXOpen.Point3d(-45.279190552759211, -4.3818571502669483, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(56.59898819094871, 5.4773214378338029, 0.0)
    viewCenter48 = NXOpen.Point3d(-56.598988190949022, -5.4773214378337247, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(45.279190552758969, 4.3818571502670736, 0.0)
    viewCenter49 = NXOpen.Point3d(-45.279190552759225, -4.3818571502669492, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(36.22335244220718, 3.5054857202136591, 0.0)
    viewCenter50 = NXOpen.Point3d(-36.223352442207407, -3.5054857202135596, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(28.978681953765705, 2.8043885761709473, 0.0)
    viewCenter51 = NXOpen.Point3d(-28.978681953765943, -2.8043885761708274, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(23.182945563012531, 2.243510860936774, 0.0)
    viewCenter52 = NXOpen.Point3d(-23.182945563012787, -2.2435108609366461, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(18.695923841139102, 1.7948086887494188, 0.0)
    viewCenter53 = NXOpen.Point3d(-18.695923841139333, -1.7948086887493166, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(15.076392985494593, 1.4358469509995457, 0.0)
    viewCenter54 = NXOpen.Point3d(-15.076392985494806, -1.4358469509994436, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    direction5 = workPart.Directions.CreateDirection(line6, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    axis1.Point = NXOpen.Point.Null
    
    axis1.Evaluate()
    
    revolveBuilder2.Axis = axis1
    
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    theSession.DeleteUndoMark(markId84, None)
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    revolveBuilder2.ParentFeatureInternal = True
    
    feature4 = revolveBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId85, None)
    
    theSession.SetUndoMarkName(markId63, "Revolve")
    
    expression31 = revolveBuilder2.Limits.StartExtend.Value
    expression32 = revolveBuilder2.Limits.EndExtend.Value
    revolveBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression29)
    
    workPart.Expressions.Delete(expression30)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    revolve1 = feature4
    revolveBuilder3 = workPart.Features.CreateRevolveBuilder(revolve1)
    
    section3.PrepareMappingData()
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId87, "Revolve Dialog")
    
    sketchFeature2 = workPart.Features.FindObject("REVOLVED(3:1B)")
    revolveBuilder3.ShowInternalParentFeatureForEdit(sketchFeature2)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    revolveBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = NXOpen.Body.Null
    revolveBuilder3.BooleanOperation.SetTargetBodies(targetBodies6)
    
    expression34 = revolveBuilder3.Limits.StartExtend.Value
    expression35 = revolveBuilder3.Limits.EndExtend.Value
    revolveBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression33)
    
    theSession.UndoToMark(markId87, None)
    
    theSession.DeleteUndoMark(markId87, None)
    
    theSession.DeleteUndoMark(markId87, None)
    
    theSession.UndoToMarkWithStatus(markId86, None)
    
    theSession.DeleteUndoMarksUpToMark(markId86, None, False)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    revolveBuilder4 = workPart.Features.CreateRevolveBuilder(revolve1)
    
    section3.PrepareMappingData()
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId89, "Revolve Dialog")
    
    revolveBuilder4.ShowInternalParentFeatureForEdit(sketchFeature2)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    revolveBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Intersect
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    targetBodies7[0] = NXOpen.Body.Null
    revolveBuilder4.BooleanOperation.SetTargetBodies(targetBodies7)
    
    revolveBuilder4.Limits.StartExtend.Value.SetFormula("0")
    
    expression37 = revolveBuilder4.Limits.StartExtend.Value
    
    expression37.RightHandSide = "0"
    
    expression38 = revolveBuilder4.Limits.EndExtend.Value
    
    expression38.RightHandSide = "360"
    
    revolveBuilder4.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.UntilSelected
    
    revolveBuilder4.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    starthelperpoint5 = [None] * 3 
    starthelperpoint5[0] = 0.0
    starthelperpoint5[1] = 0.0
    starthelperpoint5[2] = 0.0
    revolveBuilder4.SetStartLimitHelperPoint(starthelperpoint5)
    
    expression39 = revolveBuilder4.Limits.EndExtend.Value
    
    expression39.RightHandSide = "360"
    
    revolveBuilder4.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Value
    
    revolveBuilder4.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    expression40 = revolveBuilder4.Limits.StartExtend.Value
    
    expression40.RightHandSide = "0"
    
    expression41 = revolveBuilder4.Limits.EndExtend.Value
    
    expression41.RightHandSide = "360"
    
    expression41.SetFormula("360")
    
    expression42 = revolveBuilder4.Limits.StartExtend.Value
    
    expression42.RightHandSide = "0"
    
    expression43 = revolveBuilder4.Limits.EndExtend.Value
    
    expression43.RightHandSide = "360"
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = 0.92776589426516709
    rotMatrix15.Xy = -0.14062435671379861
    rotMatrix15.Xz = -0.34565189965799575
    rotMatrix15.Yx = 0.16338103171774043
    rotMatrix15.Yy = -0.67970219152423073
    rotMatrix15.Yz = 0.71506053541780734
    rotMatrix15.Zx = -0.33549528150660779
    rotMatrix15.Zy = -0.71988174107695313
    rotMatrix15.Zz = -0.60762915906892678
    translation15 = NXOpen.Point3d(3.0479310136030628, 14.329712160185718, -73.437614437391019)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation15, 2.7640480743698679)
    
    scaleAboutPoint55 = NXOpen.Point3d(-2.1059088614660428, -10.433821177262949, 0.0)
    viewCenter55 = NXOpen.Point3d(2.1059088614658141, 10.433821177263047, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-1.5315700810662627, -8.4236354458636491, 0.0)
    viewCenter56 = NXOpen.Point3d(1.5315700810660147, 8.4236354458637521, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(-0.98020485188244877, -6.7389083566909127, 0.0)
    viewCenter57 = NXOpen.Point3d(0.98020485188220852, 6.7389083566910122, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-0.19604097037659113, -5.3911266853527229, 0.0)
    viewCenter58 = NXOpen.Point3d(0.19604097037634038, 5.3911266853528232, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(3.0190309437974259, -5.4499389764656563, 0.0)
    viewCenter59 = NXOpen.Point3d(-3.0190309437976599, 5.4499389764657593, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(5.0480549871938294, -7.3025261465232498, 0.0)
    viewCenter60 = NXOpen.Point3d(-5.0480549871940799, 7.3025261465233502, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(6.6776455534481878, -9.25068328963936, 0.0)
    viewCenter61 = NXOpen.Point3d(-6.6776455534484276, 9.2506832896394595, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(8.3470569418102745, -11.563354112049215, 0.0)
    viewCenter62 = NXOpen.Point3d(-8.3470569418105161, 11.563354112049312, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(10.433821177262857, -14.454192640061532, 0.0)
    viewCenter63 = NXOpen.Point3d(-10.433821177263118, 14.454192640061622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(13.04227647157861, -18.067740800076923, 0.0)
    viewCenter64 = NXOpen.Point3d(-13.042276471578864, 18.067740800077011, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(23.631647735199863, -35.148336821341736, 0.0)
    viewCenter65 = NXOpen.Point3d(-23.631647735200119, 35.148336821341843, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(29.539559668999861, -43.93542102667719, 0.0)
    viewCenter66 = NXOpen.Point3d(-29.539559669000131, 43.935421026677297, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(36.924449586249828, -54.91927628334647, 0.0)
    viewCenter67 = NXOpen.Point3d(-36.924449586250148, 54.919276283346612, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(46.155561982812394, -68.649095354183146, 0.0)
    viewCenter68 = NXOpen.Point3d(-46.155561982812664, 68.649095354183274, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(66.458166779049492, -106.99034541901946, 0.0)
    viewCenter69 = NXOpen.Point3d(-66.458166779049748, 106.99034541901959, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(53.166533423239599, -85.592276335215573, 0.0)
    viewCenter70 = NXOpen.Point3d(-53.166533423239798, 85.592276335215672, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(41.832129594548952, -69.408617260229406, 0.0)
    viewCenter71 = NXOpen.Point3d(-41.832129594549109, 69.408617260229519, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(33.465703675639169, -56.274730761829076, 0.0)
    viewCenter72 = NXOpen.Point3d(-33.465703675639325, 56.274730761829204, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(26.772562940511307, -45.019784609463251, 0.0)
    viewCenter73 = NXOpen.Point3d(-26.77256294051146, 45.019784609463372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(21.418050352409026, -36.015827687570592, 0.0)
    viewCenter74 = NXOpen.Point3d(-21.418050352409189, 36.01582768757072, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(17.134440281927205, -28.812662150056454, 0.0)
    viewCenter75 = NXOpen.Point3d(-17.134440281927375, 28.812662150056585, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(12.55887466474214, -22.667237199778615, 0.0)
    viewCenter76 = NXOpen.Point3d(-12.55887466474231, 22.667237199778747, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(15.698593330927711, -28.334046499723293, 0.0)
    viewCenter77 = NXOpen.Point3d(-15.698593330927883, 28.334046499723438, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(19.623241663659659, -35.417558124654128, 0.0)
    viewCenter78 = NXOpen.Point3d(-19.623241663659822, 35.417558124654271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(24.529052079574594, -44.271947655817677, 0.0)
    viewCenter79 = NXOpen.Point3d(-24.52905207957475, 44.27194765581779, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(30.661315099468279, -55.339934569772133, 0.0)
    viewCenter80 = NXOpen.Point3d(-30.661315099468439, 55.339934569772247, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    expression42.SetFormula("0")
    
    expression44 = revolveBuilder4.Limits.StartExtend.Value
    
    expression44.RightHandSide = "0"
    
    expression45 = revolveBuilder4.Limits.EndExtend.Value
    
    expression45.RightHandSide = "360"
    
    revolveBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Intersect
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = body1
    revolveBuilder4.BooleanOperation.SetTargetBodies(targetBodies8)
    
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = 0.93602365903712803
    rotMatrix16.Xy = -0.13440861406265894
    rotMatrix16.Xz = -0.32525994863877306
    rotMatrix16.Yx = -0.043465111151838126
    rotMatrix16.Yy = -0.9612730980981854
    rotMatrix16.Yz = 0.27214851641203452
    rotMatrix16.Zx = -0.34924274342540124
    rotMatrix16.Zy = -0.24059999031269227
    rotMatrix16.Zz = -0.90561644796581697
    translation16 = NXOpen.Point3d(23.644435797148866, -12.550082247018121, -74.843490939702463)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation16, 1.1321540912618986)
    
    revolveBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression36)
    
    theSession.UndoToMark(markId89, None)
    
    theSession.DeleteUndoMark(markId89, None)
    
    theSession.DeleteUndoMark(markId89, None)
    
    theSession.UndoToMarkWithStatus(markId88, None)
    
    theSession.DeleteUndoMarksUpToMark(markId88, None, False)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = revolve1
    nErrs3 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs4 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId90, None)
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.93749995196637526
    rotMatrix17.Xy = -0.073018658157011918
    rotMatrix17.Xz = -0.34023832180398483
    rotMatrix17.Yx = -0.085774085185356563
    rotMatrix17.Yy = -0.99605872486085112
    rotMatrix17.Yz = -0.022579259048702161
    rotMatrix17.Zx = -0.33724864176695718
    rotMatrix17.Zy = 0.050351685071331941
    rotMatrix17.Zz = -0.9400681153176168
    translation17 = NXOpen.Point3d(23.644435797148866, -12.550082247018121, -74.843490939702463)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation17, 1.1321540912618977)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section4 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section4
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("80")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("80")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies10)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("80")
    
    smartVolumeProfileBuilder4 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder4.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder4.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId92, "Extrude Dialog")
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    section4.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar3 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point15 = workPart.Points.CreatePoint(edge2, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction6 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction6, point15, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder3 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder3.Csys = cartesianCoordinateSystem4
    
    datumCsysBuilder3.DisplayScaleFactor = 1.25
    
    feature5 = datumCsysBuilder3.CommitFeature()
    
    datumCsysBuilder3.Destroy()
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder7 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder7.Csystem = cartesianCoordinateSystem4
    
    sketchInPlaceBuilder7.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject11 = sketchInPlaceBuilder7.Commit()
    
    sketchInPlaceBuilder7.Destroy()
    
    sketch5 = nXObject11
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId94, None, True)
    
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint81 = NXOpen.Point3d(16.943180981032359, -34.120061010079105, 0.0)
    viewCenter81 = NXOpen.Point3d(-16.943180981032523, 34.120061010079212, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(20.886852416272639, -41.189457212509893, 0.0)
    viewCenter82 = NXOpen.Point3d(-20.886852416272845, 41.189457212509971, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(25.743410757818605, -43.818571502670096, 0.0)
    viewCenter83 = NXOpen.Point3d(-25.743410757818733, 43.81857150267016, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(20.594728606254883, -35.054857202136077, 0.0)
    viewCenter84 = NXOpen.Point3d(-20.594728606255011, 35.054857202136155, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(16.475782885003905, -28.043885761708836, 0.0)
    viewCenter85 = NXOpen.Point3d(-16.475782885004005, 28.043885761708918, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(13.18062630800309, -22.435108609367067, 0.0)
    viewCenter86 = NXOpen.Point3d(-13.180626308003221, 22.435108609367148, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Rectangle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId96, "Curve")
    
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId98, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint7 = NXOpen.Point3d(-35.000000000000007, 7.1880428079746466, -80.0)
    endPoint7 = NXOpen.Point3d(-15.000000000000004, 7.1880428079746466, -80.0)
    line7 = workPart.Curves.CreateLine(startPoint7, endPoint7)
    
    startPoint8 = NXOpen.Point3d(-15.000000000000004, 7.1880428079746466, -80.0)
    endPoint8 = NXOpen.Point3d(-15.00000000000002, -7.1880428079746439, -80.0)
    line8 = workPart.Curves.CreateLine(startPoint8, endPoint8)
    
    startPoint9 = NXOpen.Point3d(-15.00000000000002, -7.1880428079746439, -80.0)
    endPoint9 = NXOpen.Point3d(-35.000000000000021, -7.188042807974643, -80.0)
    line9 = workPart.Curves.CreateLine(startPoint9, endPoint9)
    
    startPoint10 = NXOpen.Point3d(-35.000000000000021, -7.188042807974643, -80.0)
    endPoint10 = NXOpen.Point3d(-35.000000000000007, 7.1880428079746466, -80.0)
    line10 = workPart.Curves.CreateLine(startPoint10, endPoint10)
    
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line9, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line10, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_12.Geometry = line7
    geom1_12.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_12.SplineDefiningPointIndex = 0
    geom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_12.Geometry = line8
    geom2_12.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint20 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_12, geom2_12)
    
    geom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_13.Geometry = line8
    geom1_13.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_13.SplineDefiningPointIndex = 0
    geom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_13.Geometry = line9
    geom2_13.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint21 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_13, geom2_13)
    
    geom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_14.Geometry = line9
    geom1_14.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_14.SplineDefiningPointIndex = 0
    geom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_14.Geometry = line10
    geom2_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint22 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_14, geom2_14)
    
    geom1_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_15.Geometry = line10
    geom1_15.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_15.SplineDefiningPointIndex = 0
    geom2_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_15.Geometry = line7
    geom2_15.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_15.SplineDefiningPointIndex = 0
    sketchGeometricConstraint23 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_15, geom2_15)
    
    geom3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom3.Geometry = line7
    geom3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint24 = theSession.ActiveSketch.CreateHorizontalConstraint(geom3)
    
    conGeom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_11.Geometry = line7
    conGeom1_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_11.SplineDefiningPointIndex = 0
    conGeom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_11.Geometry = line8
    conGeom2_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint25 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_11, conGeom2_11)
    
    conGeom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_12.Geometry = line8
    conGeom1_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_12.SplineDefiningPointIndex = 0
    conGeom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_12.Geometry = line9
    conGeom2_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint26 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_12, conGeom2_12)
    
    conGeom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_13.Geometry = line9
    conGeom1_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_13.SplineDefiningPointIndex = 0
    conGeom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_13.Geometry = line10
    conGeom2_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint27 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_13, conGeom2_13)
    
    conGeom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_14.Geometry = line10
    conGeom1_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_14.SplineDefiningPointIndex = 0
    conGeom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_14.Geometry = line7
    conGeom2_14.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint28 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_14, conGeom2_14)
    
    conGeom1_15 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_15.Geometry = edge1
    conGeom1_15.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    conGeom1_15.SplineDefiningPointIndex = 0
    conGeom2_15 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_15.Geometry = line7
    conGeom2_15.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_15.SplineDefiningPointIndex = 0
    sketchGeometricConstraint29 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_15, conGeom2_15)
    
    conGeom1_16 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_16.Geometry = edge1
    conGeom1_16.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    conGeom1_16.SplineDefiningPointIndex = 0
    conGeom2_16 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_16.Geometry = line8
    conGeom2_16.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_16.SplineDefiningPointIndex = 0
    sketchGeometricConstraint30 = theSession.ActiveSketch.CreateMidpointConstraint(conGeom1_16, conGeom2_16)
    
    dimObject1_9 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_9.Geometry = line7
    dimObject1_9.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_9.AssocValue = 0
    dimObject1_9.HelpPoint.X = 0.0
    dimObject1_9.HelpPoint.Y = 0.0
    dimObject1_9.HelpPoint.Z = 0.0
    dimObject1_9.View = NXOpen.NXObject.Null
    dimObject2_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_5.Geometry = line7
    dimObject2_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_5.AssocValue = 0
    dimObject2_5.HelpPoint.X = 0.0
    dimObject2_5.HelpPoint.Y = 0.0
    dimObject2_5.HelpPoint.Z = 0.0
    dimObject2_5.View = NXOpen.NXObject.Null
    dimOrigin9 = NXOpen.Point3d(-25.000000000000007, 12.275689484744511, -80.0)
    sketchDimensionalConstraint9 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_9, dimObject2_5, dimOrigin9, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint5 = sketchDimensionalConstraint9
    dimension9 = sketchHelpedDimensionalConstraint5.AssociatedDimension
    
    expression47 = sketchHelpedDimensionalConstraint5.AssociatedExpression
    
    dimObject1_10 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_10.Geometry = line8
    dimObject1_10.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_10.AssocValue = 0
    dimObject1_10.HelpPoint.X = 0.0
    dimObject1_10.HelpPoint.Y = 0.0
    dimObject1_10.HelpPoint.Z = 0.0
    dimObject1_10.View = NXOpen.NXObject.Null
    dimObject2_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_6.Geometry = line8
    dimObject2_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_6.AssocValue = 0
    dimObject2_6.HelpPoint.X = 0.0
    dimObject2_6.HelpPoint.Y = 0.0
    dimObject2_6.HelpPoint.Z = 0.0
    dimObject2_6.View = NXOpen.NXObject.Null
    dimOrigin10 = NXOpen.Point3d(-9.9123533232301462, -4.3255509108702123e-15, -80.0)
    sketchDimensionalConstraint10 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_10, dimObject2_6, dimOrigin10, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint6 = sketchDimensionalConstraint10
    dimension10 = sketchHelpedDimensionalConstraint6.AssociatedDimension
    
    expression48 = sketchHelpedDimensionalConstraint6.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms6 = [NXOpen.SmartObject.Null] * 4 
    geoms6[0] = line7
    geoms6[1] = line8
    geoms6[2] = line9
    geoms6[3] = line10
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms6)
    
    geoms7 = [NXOpen.SmartObject.Null] * 4 
    geoms7[0] = line7
    geoms7[1] = line8
    geoms7[2] = line9
    geoms7[3] = line10
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms7)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId99, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point16 = NXOpen.Point3d(-19.18381494254572, -7.188042807974643, -80.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(line9, workPart.ModelingViews.WorkView, point16)
    
    point1_9 = NXOpen.Point3d(-15.00000000000002, -7.1880428079746439, -80.0)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line9, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    point1_10 = NXOpen.Point3d(-35.000000000000021, -7.188042807974643, -80.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line9, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point17 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point17
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
    
    point18 = NXOpen.Point3d(-36.683199657852072, -14.06814278151389, -80.0)
    sketchRapidDimensionBuilder6.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point18)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.TextCentered = False
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject12 = sketchRapidDimensionBuilder6.Commit()
    
    theSession.DeleteUndoMark(markId100, None)
    
    theSession.SetUndoMarkName(markId99, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId99, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId101, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    expression49 = workPart.Expressions.FindObject("p11")
    expression49.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId101, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId102, None)
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId101, "Edit Driving Value")
    
    point1_11 = NXOpen.Point3d(-32.500000000000014, 1.7763568394002505e-15, -80.0)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line10, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    theSession.UndoToMark(markId103, None)
    
    theSession.DeleteUndoMark(markId103, None)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines45 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines48)
    
    theSession.SetUndoMarkName(markId104, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    point19 = NXOpen.Point3d(-32.500000000000014, -2.8505884768303336, -80.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(line10, workPart.ModelingViews.WorkView, point19)
    
    point1_12 = NXOpen.Point3d(-32.500000000000014, -7.188042807974643, -80.0)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line10, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(-32.500000000000014, 7.1880428079746466, -80.0)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line10, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin5 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin5.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin5.View = NXOpen.View.Null
    assocOrigin5.ViewOfGeometry = workPart.ModelingViews.WorkView
    point20 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin5.PointOnGeometry = point20
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
    sketchRapidDimensionBuilder8.Origin.SetAssociativeOrigin(assocOrigin5)
    
    point21 = NXOpen.Point3d(-39.524980081705245, -3.1497232582885673, -80.0)
    sketchRapidDimensionBuilder8.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point21)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.TextCentered = False
    
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject13 = sketchRapidDimensionBuilder8.Commit()
    
    theSession.DeleteUndoMark(markId105, None)
    
    theSession.SetUndoMarkName(markId104, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId104, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder9 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines49 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines49)
    
    lines50 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines50)
    
    lines51 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines51)
    
    lines52 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines52)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder9.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId106, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder9.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder9.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    expression50 = workPart.Expressions.FindObject("p12")
    expression50.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId106, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId107, None)
    
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId106, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder9.Destroy()
    
    theSession.UndoToMark(markId108, None)
    
    theSession.DeleteUndoMark(markId108, None)
    
    sketchRapidDimensionBuilder9.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId93, None)
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves2 = [NXOpen.ICurve.Null] * 4 
    curves2[0] = line7
    curves2[1] = line8
    curves2[2] = line9
    curves2[3] = line10
    seedPoint2 = NXOpen.Point3d(-22.500000000000011, -2.5, -80.0)
    regionBoundaryRule2 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch5, curves2, seedPoint2, 0.01)
    
    section4.AllowSelfIntersection(True)
    
    rules3 = [None] * 1 
    rules3[0] = regionBoundaryRule2
    helpPoint3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section4.AddToSection(rules3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId110, None)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs2 = section4.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression51)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction7 = workPart.Directions.CreateDirection(sketch5, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction7
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies11)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies12)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId111, None)
    
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder3.ParentFeatureInternal = True
    
    feature6 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId112, None)
    
    theSession.SetUndoMarkName(markId92, "Extrude")
    
    expression53 = extrudeBuilder3.Limits.StartExtend.Value
    expression54 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression46)
    
    workPart.Expressions.Delete(expression52)
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder4 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section5 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder4.Section = section5
    
    extrudeBuilder4.AllowSelfIntersectingSection(True)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder4.DistanceTolerance = 0.01
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies13 = [NXOpen.Body.Null] * 1 
    targetBodies13[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies13)
    
    extrudeBuilder4.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("80")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies14 = [NXOpen.Body.Null] * 1 
    targetBodies14[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies14)
    
    extrudeBuilder4.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder4.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder5 = extrudeBuilder4.SmartVolumeProfile
    
    smartVolumeProfileBuilder5.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder5.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId113, "Extrude Dialog")
    
    section5.DistanceTolerance = 0.01
    
    section5.ChainingTolerance = 0.0094999999999999998
    
    section5.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    rotMatrix18 = NXOpen.Matrix3x3()
    
    rotMatrix18.Xx = 0.92095229989332283
    rotMatrix18.Xy = -0.089963884033029254
    rotMatrix18.Xz = -0.37914820438832181
    rotMatrix18.Yx = 0.12469116709261559
    rotMatrix18.Yy = -0.8537916722694483
    rotMatrix18.Yz = 0.50546205912255815
    rotMatrix18.Zx = -0.36918690953266187
    rotMatrix18.Zy = -0.51278287796398558
    rotMatrix18.Zz = -0.7750837025100511
    translation18 = NXOpen.Point3d(22.025986798501439, 9.3608151758746843, -68.363882931521218)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix18, translation18, 1.1321540912618977)
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies15 = [NXOpen.Body.Null] * 1 
    targetBodies15[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies15)
    
    targetBodies16 = []
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies16)
    
    extrudeBuilder4.Destroy()
    
    section5.Destroy()
    
    workPart.Expressions.Delete(expression55)
    
    theSession.UndoToMark(markId113, None)
    
    theSession.DeleteUndoMark(markId113, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrude2 = feature6
    extrudeBuilder5 = workPart.Features.CreateExtrudeBuilder(extrude2)
    
    section4.PrepareMappingData()
    
    extrudeBuilder5.AllowSelfIntersectingSection(True)
    
    targetBodies17 = [NXOpen.Body.Null] * 1 
    targetBodies17[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies17)
    
    targetBodies18 = [NXOpen.Body.Null] * 1 
    targetBodies18[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies18)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId115, "Extrude Dialog")
    
    sketchFeature3 = workPart.Features.FindObject("EXTRUDE(3:1B)")
    extrudeBuilder5.ShowInternalParentFeatureForEdit(sketchFeature3)
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    direction8 = extrudeBuilder5.Direction
    
    success1 = direction8.ReverseDirection()
    
    extrudeBuilder5.Direction = direction8
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("49")
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies19 = [NXOpen.Body.Null] * 1 
    targetBodies19[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies19)
    
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId116, None)
    
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature7 = extrudeBuilder5.CommitFeature()
    
    theSession.DeleteUndoMark(markId117, None)
    
    theSession.SetUndoMarkName(markId115, "Extrude")
    
    section4.CleanMappingData()
    
    expression58 = extrudeBuilder5.Limits.StartExtend.Value
    expression59 = extrudeBuilder5.Limits.EndExtend.Value
    extrudeBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression56)
    
    workPart.Expressions.Delete(expression57)
    
    theSession.DeleteUndoMark(markId115, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs5 = theSession.UpdateManager.DoUpdate(markId114)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    rotMatrix19 = NXOpen.Matrix3x3()
    
    rotMatrix19.Xx = 0.99757665166916931
    rotMatrix19.Xy = 0.031651413783790307
    rotMatrix19.Xz = -0.061959761539361217
    rotMatrix19.Yx = 0.03604016389497066
    rotMatrix19.Yy = -0.99682171694790478
    rotMatrix19.Yz = 0.071046261037818415
    rotMatrix19.Zx = -0.059514121273449717
    rotMatrix19.Zy = -0.073107131160492708
    rotMatrix19.Zz = -0.99554679284427749
    translation19 = NXOpen.Point3d(22.025986798501439, 9.3608151758746843, -68.363882931521218)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix19, translation19, 1.1321540912618977)
    
    scaleAboutPoint87 = NXOpen.Point3d(15.891535264968264, 2.8043885761709286, 0.0)
    viewCenter87 = NXOpen.Point3d(-15.891535264968422, -2.8043885761708287, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(19.864419081210329, 3.505485720213636, 0.0)
    viewCenter88 = NXOpen.Point3d(-19.864419081210528, -3.5054857202135614, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(24.830523851512972, 4.3818571502670753, 0.0)
    viewCenter89 = NXOpen.Point3d(-24.830523851513096, -4.381857150266951, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(31.038154814391213, 5.4773214378338055, 0.0)
    viewCenter90 = NXOpen.Point3d(-31.038154814391369, -5.4773214378337274, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(24.830523851513032, 4.3818571502670753, 0.0)
    viewCenter91 = NXOpen.Point3d(-24.830523851513032, -4.381857150266951, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(19.864419081210453, 3.5054857202136604, 0.0)
    viewCenter92 = NXOpen.Point3d(-19.864419081210404, -3.5054857202135361, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(15.891535264968359, 2.8043885761709482, 0.0)
    viewCenter93 = NXOpen.Point3d(-15.89153526496832, -2.8043885761708283, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(12.713228211974689, 2.2435108609367749, 0.0)
    viewCenter94 = NXOpen.Point3d(-12.713228211974657, -2.243510860936647, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(10.170582569579752, 1.7948086887494323, 0.0)
    viewCenter95 = NXOpen.Point3d(-10.170582569579725, -1.7948086887493049, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint95, viewCenter95)
    
    rotMatrix20 = NXOpen.Matrix3x3()
    
    rotMatrix20.Xx = 0.99881241505499307
    rotMatrix20.Xy = -0.041234656597191853
    rotMatrix20.Xz = -0.025951158496715223
    rotMatrix20.Yx = -0.035030146653361405
    rotMatrix20.Yy = -0.97798612403600793
    rotMatrix20.Yz = 0.2057086046291364
    rotMatrix20.Zx = -0.033862196583417013
    rotMatrix20.Zy = -0.20455523529925629
    rotMatrix20.Zz = -0.97826913850647879
    translation20 = NXOpen.Point3d(14.270917589196999, 7.9922735507032723, -68.363882931521218)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix20, translation20, 2.211238459495894)
    
    rotMatrix21 = NXOpen.Matrix3x3()
    
    rotMatrix21.Xx = 0.97995628516741817
    rotMatrix21.Xy = 0.017756745455310925
    rotMatrix21.Xz = -0.19841969950512681
    rotMatrix21.Yx = -0.0046248794109975729
    rotMatrix21.Yy = -0.99372328318750414
    rotMatrix21.Yz = -0.11177051016021637
    rotMatrix21.Zx = -0.19915895573963874
    rotMatrix21.Zy = 0.11044788111085053
    rotMatrix21.Zz = -0.97372325427033601
    translation21 = NXOpen.Point3d(14.270917589196999, 7.9922735507032723, -68.363882931521218)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix21, translation21, 2.211238459495894)
    
    scaleAboutPoint96 = NXOpen.Point3d(6.3416573669144434, 12.802968646412227, 0.0)
    viewCenter96 = NXOpen.Point3d(-6.3416573669144025, -12.802968646412095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(7.92707170864304, 16.003710808015256, 0.0)
    viewCenter97 = NXOpen.Point3d(-7.9270717086430151, -16.003710808015153, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(9.9088396358038011, 20.00463851001907, 0.0)
    viewCenter98 = NXOpen.Point3d(-9.9088396358037691, -20.004638510018946, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(12.38604954475475, 25.005798137523836, 0.0)
    viewCenter99 = NXOpen.Point3d(-12.386049544754711, -25.005798137523698, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(9.9088396358038011, 20.004638510019088, 0.0)
    viewCenter100 = NXOpen.Point3d(-9.9088396358037691, -20.004638510018946, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(7.9270717086430533, 16.003710808015281, 0.0)
    viewCenter101 = NXOpen.Point3d(-7.9270717086430018, -16.003710808015128, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(6.341657366914454, 12.802968646412237, 0.0)
    viewCenter102 = NXOpen.Point3d(-6.3416573669144025, -12.802968646412095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(5.073325893531563, 10.242374917129807, 0.0)
    viewCenter103 = NXOpen.Point3d(-5.0733258935315142, -10.242374917129659, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint103, viewCenter103)
    
    rotMatrix22 = NXOpen.Matrix3x3()
    
    rotMatrix22.Xx = 0.93284542943955628
    rotMatrix22.Xy = -0.010817322377110323
    rotMatrix22.Xz = -0.36011441280558953
    rotMatrix22.Yx = 0.097591367624167022
    rotMatrix22.Yy = -0.95459249132557122
    rotMatrix22.Yz = 0.28147664284994578
    rotMatrix22.Zx = -0.34680733806966924
    rotMatrix22.Zy = -0.29771825782343464
    rotMatrix22.Zz = -0.88943156522556566
    translation22 = NXOpen.Point3d(11.987920937107889, 3.383204837994878, -68.363882931521218)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix22, translation22, 3.4550600929623343)
    
    scaleAboutPoint104 = NXOpen.Point3d(5.2073382756248598, 7.5812719012773995, 0.0)
    viewCenter104 = NXOpen.Point3d(-5.2073382756247941, -7.5812719012772627, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(4.165870620499903, 6.0650175210219297, 0.0)
    viewCenter105 = NXOpen.Point3d(-4.1658706204998195, -6.0650175210218045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(3.3326964963999353, 4.8520140168175567, 0.0)
    viewCenter106 = NXOpen.Point3d(-3.3326964963998473, -4.852014016817435, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(4.1658706204998968, 6.0650175210219279, 0.0)
    viewCenter107 = NXOpen.Point3d(-4.165870620499823, -6.065017521021808, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint107, viewCenter107)
    
    scaleAboutPoint108 = NXOpen.Point3d(5.2073382756248652, 7.5812719012773977, 0.0)
    viewCenter108 = NXOpen.Point3d(-5.2073382756247737, -7.5812719012772734, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint108, viewCenter108)
    
    scaleAboutPoint109 = NXOpen.Point3d(6.5091728445310739, 9.4765898765967247, 0.0)
    viewCenter109 = NXOpen.Point3d(-6.5091728445309922, -9.476589876596611, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(8.1364660556638331, 11.845737345745885, 0.0)
    viewCenter110 = NXOpen.Point3d(-8.1364660556637514, -11.845737345745773, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint110, viewCenter110)
    
    scaleAboutPoint111 = NXOpen.Point3d(10.170582569579777, 14.807171682182341, 0.0)
    viewCenter111 = NXOpen.Point3d(-10.1705825695797, -14.807171682182227, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint111, viewCenter111)
    
    scaleAboutPoint112 = NXOpen.Point3d(12.713228211974721, 18.508964602727914, 0.0)
    viewCenter112 = NXOpen.Point3d(-12.713228211974625, -18.508964602727801, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint112, viewCenter112)
    
    rotMatrix23 = NXOpen.Matrix3x3()
    
    rotMatrix23.Xx = 0.98156028486969227
    rotMatrix23.Xy = 0.077088502330477884
    rotMatrix23.Xz = -0.17491932418967227
    rotMatrix23.Yx = 0.074568000984262098
    rotMatrix23.Yy = -0.99699591807692101
    rotMatrix23.Yz = -0.020946421345082351
    rotMatrix23.Zx = -0.1760085804605527
    rotMatrix23.Zy = 0.0075167909641375144
    rotMatrix23.Zz = -0.98435993287915713
    translation23 = NXOpen.Point3d(22.672117926451456, 18.93813869012736, -68.363882931521218)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix23, translation23, 1.1321540912618979)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit with Rollback...
    # ----------------------------------------------
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Redefine Feature")
    
    extrude3 = feature7
    editWithRollbackManager1 = workPart.Features.StartEditWithRollbackManager(extrude3, markId118)
    
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder6 = workPart.Features.CreateExtrudeBuilder(extrude3)
    
    section4.PrepareMappingData()
    
    extrudeBuilder6.AllowSelfIntersectingSection(True)
    
    targetBodies20 = [NXOpen.Body.Null] * 1 
    targetBodies20[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies20)
    
    targetBodies21 = [NXOpen.Body.Null] * 1 
    targetBodies21[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies21)
    
    expression60 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId119, "Extrude Dialog")
    
    extrudeBuilder6.ShowInternalParentFeatureForEdit(sketchFeature3)
    
    refs3 = section4.EvaluateAndAskOutputEntities()
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    rotMatrix24 = NXOpen.Matrix3x3()
    
    rotMatrix24.Xx = 0.99314618360411
    rotMatrix24.Xy = 0.036024756584360336
    rotMatrix24.Xz = 0.1111884657040753
    rotMatrix24.Yx = 0.062692119132283522
    rotMatrix24.Yy = -0.96707676770142847
    rotMatrix24.Yz = -0.24664189338159362
    rotMatrix24.Zx = 0.098642567846201179
    rotMatrix24.Zy = 0.25192209566687745
    rotMatrix24.Zz = -0.96270706942637041
    translation24 = NXOpen.Point3d(22.765439256922946, 18.842481622829112, -66.151641036175903)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix24, translation24, 1.1321540912618979)
    
    scaleAboutPoint113 = NXOpen.Point3d(7.7120685844699821, 39.495139114406733, 0.0)
    viewCenter113 = NXOpen.Point3d(-7.7120685844698631, -39.495139114406612, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(9.6400857305874528, 49.368923893008407, 0.0)
    viewCenter114 = NXOpen.Point3d(-9.6400857305873018, -49.368923893008287, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint114, viewCenter114)
    
    scaleAboutPoint115 = NXOpen.Point3d(12.050107163234284, 61.711154866260479, 0.0)
    viewCenter115 = NXOpen.Point3d(-12.050107163234284, -61.711154866260358, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(14.606190500889987, 69.835848332380536, 0.0)
    viewCenter116 = NXOpen.Point3d(-14.606190500889987, -69.835848332380465, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint116, viewCenter116)
    
    scaleAboutPoint117 = NXOpen.Point3d(11.684952400711991, 55.868678665904469, 0.0)
    viewCenter117 = NXOpen.Point3d(-11.684952400711991, -55.868678665904348, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(9.3479619205695936, 44.694942932723599, 0.0)
    viewCenter118 = NXOpen.Point3d(-9.3479619205695936, -44.694942932723478, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint118, viewCenter118)
    
    scaleAboutPoint119 = NXOpen.Point3d(7.4783695364556744, 35.755954346178861, 0.0)
    viewCenter119 = NXOpen.Point3d(-7.4783695364556744, -35.755954346178783, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint119, viewCenter119)
    
    scaleAboutPoint120 = NXOpen.Point3d(5.9826956291645397, 28.604763476943106, 0.0)
    viewCenter120 = NXOpen.Point3d(-5.9826956291645397, -28.60476347694301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(-5.5339934569772113, 27.669967284886152, 0.0)
    viewCenter121 = NXOpen.Point3d(5.5339934569772113, -27.669967284886049, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(-4.4271947655817794, 22.135973827908924, 0.0)
    viewCenter122 = NXOpen.Point3d(4.4271947655817794, -22.135973827908831, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint122, viewCenter122)
    
    scaleAboutPoint123 = NXOpen.Point3d(-3.5417558124654231, 17.70877906232716, 0.0)
    viewCenter123 = NXOpen.Point3d(3.5417558124654231, -17.708779062327046, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint123, viewCenter123)
    
    scaleAboutPoint124 = NXOpen.Point3d(-2.8334046499723318, 14.167023249861746, 0.0)
    viewCenter124 = NXOpen.Point3d(2.833404649972338, -14.167023249861622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint124, viewCenter124)
    
    rotMatrix25 = NXOpen.Matrix3x3()
    
    rotMatrix25.Xx = 0.99690889208951272
    rotMatrix25.Xy = 0.070712975342915582
    rotMatrix25.Xz = 0.034239392386676656
    rotMatrix25.Yx = 0.071622551950630109
    rotMatrix25.Yy = -0.99709003126176665
    rotMatrix25.Yz = -0.026108994819481982
    rotMatrix25.Zx = 0.032293512118317338
    rotMatrix25.Zy = 0.028480601759033105
    rotMatrix25.Zz = -0.99907256212874718
    translation25 = NXOpen.Point3d(23.593547981261487, -6.7301678852483633, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix25, translation25, 4.3188251162029179)
    
    scaleAboutPoint125 = NXOpen.Point3d(-1.1027304583676014, 9.8020485188232733, 0.0)
    viewCenter125 = NXOpen.Point3d(1.1027304583676065, -9.8020485188231579, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint125, viewCenter125)
    
    expression62 = extrudeBuilder6.Limits.StartExtend.Value
    expression63 = extrudeBuilder6.Limits.EndExtend.Value
    extrudeBuilder6.Destroy()
    
    workPart.Expressions.Delete(expression60)
    
    workPart.Expressions.Delete(expression61)
    
    theSession.UndoToMark(markId119, None)
    
    theSession.DeleteUndoMark(markId119, None)
    
    theSession.DeleteUndoMark(markId119, None)
    
    editWithRollbackManager1.UpdateFeature(True)
    
    editWithRollbackManager1.Stop()
    
    theSession.UndoToMarkWithStatus(markId118, None)
    
    theSession.DeleteUndoMarksUpToMark(markId118, None, False)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit with Rollback...
    # ----------------------------------------------
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Redefine Feature")
    
    editWithRollbackManager2 = workPart.Features.StartEditWithRollbackManager(extrude3, markId120)
    
    markId121 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder7 = workPart.Features.CreateExtrudeBuilder(extrude3)
    
    section4.PrepareMappingData()
    
    extrudeBuilder7.AllowSelfIntersectingSection(True)
    
    targetBodies22 = [NXOpen.Body.Null] * 1 
    targetBodies22[0] = body1
    extrudeBuilder7.BooleanOperation.SetTargetBodies(targetBodies22)
    
    targetBodies23 = [NXOpen.Body.Null] * 1 
    targetBodies23[0] = body1
    extrudeBuilder7.BooleanOperation.SetTargetBodies(targetBodies23)
    
    expression64 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId121, "Extrude Dialog")
    
    extrudeBuilder7.ShowInternalParentFeatureForEdit(sketchFeature3)
    
    refs4 = section4.EvaluateAndAskOutputEntities()
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    extrudeBuilder7.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder7.Limits.StartExtend.Value.SetFormula("0")
    
    expression66 = extrudeBuilder7.Limits.StartExtend.Value
    expression67 = extrudeBuilder7.Limits.EndExtend.Value
    extrudeBuilder7.Destroy()
    
    workPart.Expressions.Delete(expression64)
    
    workPart.Expressions.Delete(expression65)
    
    theSession.UndoToMark(markId121, None)
    
    theSession.DeleteUndoMark(markId121, None)
    
    theSession.DeleteUndoMark(markId121, None)
    
    editWithRollbackManager2.UpdateFeature(True)
    
    editWithRollbackManager2.Stop()
    
    theSession.UndoToMarkWithStatus(markId120, None)
    
    theSession.DeleteUndoMarksUpToMark(markId120, None, False)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId122 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId123 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    objects8[0] = extrude3
    nErrs6 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs7 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId122, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId124 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder8 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section6 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder8.Section = section6
    
    extrudeBuilder8.AllowSelfIntersectingSection(True)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder8.DistanceTolerance = 0.01
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies24 = [NXOpen.Body.Null] * 1 
    targetBodies24[0] = NXOpen.Body.Null
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies24)
    
    extrudeBuilder8.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder8.Limits.EndExtend.Value.SetFormula("80")
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies25 = [NXOpen.Body.Null] * 1 
    targetBodies25[0] = NXOpen.Body.Null
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies25)
    
    extrudeBuilder8.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder8.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder8.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder8.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder6 = extrudeBuilder8.SmartVolumeProfile
    
    smartVolumeProfileBuilder6.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder6.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId124, "Extrude Dialog")
    
    section6.DistanceTolerance = 0.01
    
    section6.ChainingTolerance = 0.0094999999999999998
    
    section6.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar4 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point22 = workPart.Points.CreatePoint(edge2, scalar4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction9 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction9, point22, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem5 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder4 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder4.Csys = cartesianCoordinateSystem5
    
    datumCsysBuilder4.DisplayScaleFactor = 1.25
    
    feature8 = datumCsysBuilder4.CommitFeature()
    
    datumCsysBuilder4.Destroy()
    
    markId125 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder8 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder8.Csystem = cartesianCoordinateSystem5
    
    sketchInPlaceBuilder8.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject14 = sketchInPlaceBuilder8.Commit()
    
    sketchInPlaceBuilder8.Destroy()
    
    sketch6 = nXObject14
    sketch6.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId126 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId126, None, True)
    
    markId127 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId128 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint126 = NXOpen.Point3d(9.7993031965136872, -2.7313461232335787, 0.0)
    viewCenter126 = NXOpen.Point3d(-9.7993031965136694, 2.731346123233704, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint126, viewCenter126)
    
    scaleAboutPoint127 = NXOpen.Point3d(7.8394425572109458, -2.1850768985868458, 0.0)
    viewCenter127 = NXOpen.Point3d(-7.8394425572109387, 2.1850768985869764, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint127, viewCenter127)
    
    scaleAboutPoint128 = NXOpen.Point3d(6.271554045768756, -1.7480615188694686, 0.0)
    viewCenter128 = NXOpen.Point3d(-6.2715540457687506, 1.7480615188695916, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(2.7600971350571566, -3.6555953166534088, 0.0)
    viewCenter129 = NXOpen.Point3d(-2.7600971350571477, 3.6555953166535393, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint129, viewCenter129)
    
    scaleAboutPoint130 = NXOpen.Point3d(3.4807891647665232, -4.63082963770694, 0.0)
    viewCenter130 = NXOpen.Point3d(-3.4807891647665179, 4.6308296377070679, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint130, viewCenter130)
    
    scaleAboutPoint131 = NXOpen.Point3d(4.3893211383895006, -5.7885370471336879, 0.0)
    viewCenter131 = NXOpen.Point3d(-4.3893211383894943, 5.7885370471338184, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint131, viewCenter131)
    
    scaleAboutPoint132 = NXOpen.Point3d(5.5345697760260633, -7.2835896619563183, 0.0)
    viewCenter132 = NXOpen.Point3d(-5.5345697760260633, 7.2835896619564435, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(6.9182122200325828, -9.1044870774454125, 0.0)
    viewCenter133 = NXOpen.Point3d(-6.9182122200325722, 9.1044870774455369, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(8.6477652750407348, -11.380608846806778, 0.0)
    viewCenter134 = NXOpen.Point3d(-8.6477652750407223, 11.380608846806902, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint134, viewCenter134)
    
    scaleAboutPoint135 = NXOpen.Point3d(10.809706593800909, -14.225761058508487, 0.0)
    viewCenter135 = NXOpen.Point3d(-10.809706593800893, 14.225761058508619, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint135, viewCenter135)
    
    scaleAboutPoint136 = NXOpen.Point3d(20.765399571424883, -33.107651147680194, 0.0)
    viewCenter136 = NXOpen.Point3d(-20.765399571424883, 33.107651147680315, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint136, viewCenter136)
    
    scaleAboutPoint137 = NXOpen.Point3d(25.810514256031624, -41.384563934600251, 0.0)
    viewCenter137 = NXOpen.Point3d(-25.810514256031624, 41.384563934600379, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(31.897554799415875, -51.91349892856217, 0.0)
    viewCenter138 = NXOpen.Point3d(-31.897554799415875, 51.913498928562312, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint138, viewCenter138)
    
    scaleAboutPoint139 = NXOpen.Point3d(39.87194349926984, -64.891873660702728, 0.0)
    viewCenter139 = NXOpen.Point3d(-39.87194349926984, 64.891873660702871, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(49.554313732975046, -81.1148420758784, 0.0)
    viewCenter140 = NXOpen.Point3d(-49.554313732975046, 81.114842075878556, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(76.22367422183126, -115.31731509907014, 0.0)
    viewCenter141 = NXOpen.Point3d(-76.223674221831146, 115.31731509907027, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint141, viewCenter141)
    
    scaleAboutPoint142 = NXOpen.Point3d(60.978939377465061, -92.253852079256092, 0.0)
    viewCenter142 = NXOpen.Point3d(-60.978939377464862, 92.25385207925622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint142, viewCenter142)
    
    scaleAboutPoint143 = NXOpen.Point3d(48.78315150197205, -73.803081663404882, 0.0)
    viewCenter143 = NXOpen.Point3d(-48.783151501971894, 73.803081663404996, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint143, viewCenter143)
    
    scaleAboutPoint144 = NXOpen.Point3d(39.026521201577687, -59.042465330723878, 0.0)
    viewCenter144 = NXOpen.Point3d(-39.026521201577459, 59.042465330723985, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(30.928746544763239, -45.917855390333855, 0.0)
    viewCenter145 = NXOpen.Point3d(-30.928746544762983, 45.917855390333969, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint145, viewCenter145)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Rectangle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId128, "Curve")
    
    markId129 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId130 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId130, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint11 = NXOpen.Point3d(-9.2714716941067561, 7.6967551229884421, -80.0)
    endPoint11 = NXOpen.Point3d(-25.000000000000004, 7.6967551229884279, -80.0)
    line11 = workPart.Curves.CreateLine(startPoint11, endPoint11)
    
    startPoint12 = NXOpen.Point3d(-25.000000000000004, 7.6967551229884279, -80.0)
    endPoint12 = NXOpen.Point3d(-25.000000000000007, -7.6967551229884421, -80.0)
    line12 = workPart.Curves.CreateLine(startPoint12, endPoint12)
    
    startPoint13 = NXOpen.Point3d(-25.000000000000007, -7.6967551229884421, -80.0)
    endPoint13 = NXOpen.Point3d(-9.2714716941067579, -7.6967551229884279, -80.0)
    line13 = workPart.Curves.CreateLine(startPoint13, endPoint13)
    
    startPoint14 = NXOpen.Point3d(-9.2714716941067579, -7.6967551229884279, -80.0)
    endPoint14 = NXOpen.Point3d(-9.2714716941067561, 7.6967551229884421, -80.0)
    line14 = workPart.Curves.CreateLine(startPoint14, endPoint14)
    
    theSession.ActiveSketch.AddGeometry(line11, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line12, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line13, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line14, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_16.Geometry = line11
    geom1_16.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_16.SplineDefiningPointIndex = 0
    geom2_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_16.Geometry = line12
    geom2_16.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_16.SplineDefiningPointIndex = 0
    sketchGeometricConstraint31 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_16, geom2_16)
    
    geom1_17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_17.Geometry = line12
    geom1_17.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_17.SplineDefiningPointIndex = 0
    geom2_17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_17.Geometry = line13
    geom2_17.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_17.SplineDefiningPointIndex = 0
    sketchGeometricConstraint32 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_17, geom2_17)
    
    geom1_18 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_18.Geometry = line13
    geom1_18.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_18.SplineDefiningPointIndex = 0
    geom2_18 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_18.Geometry = line14
    geom2_18.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_18.SplineDefiningPointIndex = 0
    sketchGeometricConstraint33 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_18, geom2_18)
    
    geom1_19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_19.Geometry = line14
    geom1_19.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_19.SplineDefiningPointIndex = 0
    geom2_19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_19.Geometry = line11
    geom2_19.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_19.SplineDefiningPointIndex = 0
    sketchGeometricConstraint34 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_19, geom2_19)
    
    geom4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom4.Geometry = line11
    geom4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint35 = theSession.ActiveSketch.CreateHorizontalConstraint(geom4)
    
    conGeom1_17 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_17.Geometry = line11
    conGeom1_17.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_17.SplineDefiningPointIndex = 0
    conGeom2_17 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_17.Geometry = line12
    conGeom2_17.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_17.SplineDefiningPointIndex = 0
    sketchGeometricConstraint36 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_17, conGeom2_17)
    
    conGeom1_18 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_18.Geometry = line12
    conGeom1_18.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_18.SplineDefiningPointIndex = 0
    conGeom2_18 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_18.Geometry = line13
    conGeom2_18.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_18.SplineDefiningPointIndex = 0
    sketchGeometricConstraint37 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_18, conGeom2_18)
    
    conGeom1_19 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_19.Geometry = line13
    conGeom1_19.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_19.SplineDefiningPointIndex = 0
    conGeom2_19 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_19.Geometry = line14
    conGeom2_19.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_19.SplineDefiningPointIndex = 0
    sketchGeometricConstraint38 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_19, conGeom2_19)
    
    conGeom1_20 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_20.Geometry = line14
    conGeom1_20.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_20.SplineDefiningPointIndex = 0
    conGeom2_20 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_20.Geometry = line11
    conGeom2_20.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_20.SplineDefiningPointIndex = 0
    sketchGeometricConstraint39 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_20, conGeom2_20)
    
    geom5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom5.Geometry = line11
    geom5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom5.SplineDefiningPointIndex = 0
    try:
        # Constraint already exists.
        sketchGeometricConstraint40 = theSession.ActiveSketch.CreateHorizontalConstraint(geom5)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(910023)
        
    dimObject1_11 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_11.Geometry = line11
    dimObject1_11.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_11.AssocValue = 0
    dimObject1_11.HelpPoint.X = 0.0
    dimObject1_11.HelpPoint.Y = 0.0
    dimObject1_11.HelpPoint.Z = 0.0
    dimObject1_11.View = NXOpen.NXObject.Null
    dimObject2_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_7.Geometry = line11
    dimObject2_7.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_7.AssocValue = 0
    dimObject2_7.HelpPoint.X = 0.0
    dimObject2_7.HelpPoint.Y = 0.0
    dimObject2_7.HelpPoint.Z = 0.0
    dimObject2_7.View = NXOpen.NXObject.Null
    dimOrigin11 = NXOpen.Point3d(-17.135735847053375, 3.7173151252705443, -80.0)
    sketchDimensionalConstraint11 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_11, dimObject2_7, dimOrigin11, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint7 = sketchDimensionalConstraint11
    dimension11 = sketchHelpedDimensionalConstraint7.AssociatedDimension
    
    expression69 = sketchHelpedDimensionalConstraint7.AssociatedExpression
    
    dimObject1_12 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_12.Geometry = line12
    dimObject1_12.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_12.AssocValue = 0
    dimObject1_12.HelpPoint.X = 0.0
    dimObject1_12.HelpPoint.Y = 0.0
    dimObject1_12.HelpPoint.Z = 0.0
    dimObject1_12.View = NXOpen.NXObject.Null
    dimObject2_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_8.Geometry = line12
    dimObject2_8.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_8.AssocValue = 0
    dimObject2_8.HelpPoint.X = 0.0
    dimObject2_8.HelpPoint.Y = 0.0
    dimObject2_8.HelpPoint.Z = 0.0
    dimObject2_8.View = NXOpen.NXObject.Null
    dimOrigin12 = NXOpen.Point3d(-21.020560002282117, -8.0238540639172644e-15, -80.0)
    sketchDimensionalConstraint12 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_12, dimObject2_8, dimOrigin12, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint8 = sketchDimensionalConstraint12
    dimension12 = sketchHelpedDimensionalConstraint8.AssociatedDimension
    
    expression70 = sketchHelpedDimensionalConstraint8.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms8 = [NXOpen.SmartObject.Null] * 4 
    geoms8[0] = line11
    geoms8[1] = line12
    geoms8[2] = line13
    geoms8[3] = line14
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms8)
    
    geoms9 = [NXOpen.SmartObject.Null] * 4 
    geoms9[0] = line11
    geoms9[1] = line12
    geoms9[2] = line13
    geoms9[3] = line14
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms9)
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId131 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder10 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines53 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBefore(lines53)
    
    lines54 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAfter(lines54)
    
    lines55 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAbove(lines55)
    
    lines56 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBelow(lines56)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder10.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines57 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBefore(lines57)
    
    lines58 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAfter(lines58)
    
    lines59 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAbove(lines59)
    
    lines60 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBelow(lines60)
    
    theSession.SetUndoMarkName(markId131, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder10.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder10.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    point23 = NXOpen.Point3d(-13.860067182265228, -7.6967551229884315, -80.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(line13, workPart.ModelingViews.WorkView, point23)
    
    point1_14 = NXOpen.Point3d(-9.2714716941067579, -7.6967551229884279, -80.0)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line13, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    point1_15 = NXOpen.Point3d(-25.000000000000007, -7.6967551229884421, -80.0)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line13, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin6 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin6.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin6.View = NXOpen.View.Null
    assocOrigin6.ViewOfGeometry = workPart.ModelingViews.WorkView
    point24 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin6.PointOnGeometry = point24
    assocOrigin6.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.DimensionLine = 0
    assocOrigin6.AssociatedView = NXOpen.View.Null
    assocOrigin6.AssociatedPoint = NXOpen.Point.Null
    assocOrigin6.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.XOffsetFactor = 0.0
    assocOrigin6.YOffsetFactor = 0.0
    assocOrigin6.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder10.Origin.SetAssociativeOrigin(assocOrigin6)
    
    point25 = NXOpen.Point3d(-13.15813818266777, -12.259293620371938, -80.0)
    sketchRapidDimensionBuilder10.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point25)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.TextCentered = False
    
    markId132 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject15 = sketchRapidDimensionBuilder10.Commit()
    
    theSession.DeleteUndoMark(markId132, None)
    
    theSession.SetUndoMarkName(markId131, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId131, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder10.Destroy()
    
    markId133 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder11 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines61 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBefore(lines61)
    
    lines62 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAfter(lines62)
    
    lines63 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAbove(lines63)
    
    lines64 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBelow(lines64)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder11.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId133, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder11.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder11.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits271 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits272 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits273 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits274 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    expression71 = workPart.Expressions.FindObject("p11")
    expression71.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId133, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId134 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.95368108880109392)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId134, None)
    
    markId135 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId133, "Edit Driving Value")
    
    point26 = NXOpen.Point3d(-9.9999999999969074, -5.5909681241960598, -80.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(line14, workPart.ModelingViews.WorkView, point26)
    
    point1_16 = NXOpen.Point3d(-9.9999999999969074, -8.4982225858996543, -80.0)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line14, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(-9.9999999999969056, 6.1822770259543631, -80.0)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line14, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    dimensionlinearunits275 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits276 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits277 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits278 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits279 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits280 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin7 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin7.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin7.View = NXOpen.View.Null
    assocOrigin7.ViewOfGeometry = workPart.ModelingViews.WorkView
    point27 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin7.PointOnGeometry = point27
    assocOrigin7.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.DimensionLine = 0
    assocOrigin7.AssociatedView = NXOpen.View.Null
    assocOrigin7.AssociatedPoint = NXOpen.Point.Null
    assocOrigin7.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.XOffsetFactor = 0.0
    assocOrigin7.YOffsetFactor = 0.0
    assocOrigin7.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder11.Origin.SetAssociativeOrigin(assocOrigin7)
    
    point28 = NXOpen.Point3d(-5.0859546872969617, -6.0589207905943674, -80.0)
    sketchRapidDimensionBuilder11.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point28)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.TextCentered = False
    
    markId136 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject16 = sketchRapidDimensionBuilder11.Commit()
    
    theSession.DeleteUndoMark(markId136, None)
    
    theSession.SetUndoMarkName(markId135, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId135, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder11.Destroy()
    
    markId137 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder12 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines65 = []
    sketchRapidDimensionBuilder12.AppendedText.SetBefore(lines65)
    
    lines66 = []
    sketchRapidDimensionBuilder12.AppendedText.SetAfter(lines66)
    
    lines67 = []
    sketchRapidDimensionBuilder12.AppendedText.SetAbove(lines67)
    
    lines68 = []
    sketchRapidDimensionBuilder12.AppendedText.SetBelow(lines68)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder12.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId137, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder12.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits281 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits282 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits283 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits284 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits285 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits286 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits287 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits288 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits289 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits290 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder12.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits291 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits292 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits293 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits294 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits295 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits296 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits297 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits298 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits299 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits300 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    expression72 = workPart.Expressions.FindObject("p12")
    expression72.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId137, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId138 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId138, None)
    
    markId139 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId137, "Edit Driving Value")
    
    scaleAboutPoint146 = NXOpen.Point3d(24.976973569009761, -24.801491319110227, 0.0)
    viewCenter146 = NXOpen.Point3d(-24.976973569009537, 24.80149131911034, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint146, viewCenter146)
    
    scaleAboutPoint147 = NXOpen.Point3d(19.981578855207836, -19.841193055288176, 0.0)
    viewCenter147 = NXOpen.Point3d(-19.981578855207609, 19.841193055288294, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint147, viewCenter147)
    
    scaleAboutPoint148 = NXOpen.Point3d(15.985263084166284, -15.872954444230519, 0.0)
    viewCenter148 = NXOpen.Point3d(-15.985263084166062, 15.872954444230636, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(12.788210467333057, -12.698363555384413, 0.0)
    viewCenter149 = NXOpen.Point3d(-12.788210467332826, 12.698363555384526, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    scaleAboutPoint150 = NXOpen.Point3d(10.230568373866467, -10.158690844307518, 0.0)
    viewCenter150 = NXOpen.Point3d(-10.230568373866241, 10.158690844307639, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(12.788210467333059, -12.698363555384409, 0.0)
    viewCenter151 = NXOpen.Point3d(-12.788210467332828, 12.69836355538453, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint151, viewCenter151)
    
    scaleAboutPoint152 = NXOpen.Point3d(15.985263084166283, -15.872954444230523, 0.0)
    viewCenter152 = NXOpen.Point3d(-15.985263084166073, 15.872954444230647, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint152, viewCenter152)
    
    scaleAboutPoint153 = NXOpen.Point3d(19.981578855207818, -19.841193055288169, 0.0)
    viewCenter153 = NXOpen.Point3d(-19.981578855207623, 19.841193055288301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint153, viewCenter153)
    
    scaleAboutPoint154 = NXOpen.Point3d(24.976973569009754, -24.801491319110234, 0.0)
    viewCenter154 = NXOpen.Point3d(-24.976973569009552, 24.801491319110355, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint154, viewCenter154)
    
    scaleAboutPoint155 = NXOpen.Point3d(31.221216961262165, -31.001864148887801, 0.0)
    viewCenter155 = NXOpen.Point3d(-31.221216961261963, 31.001864148887929, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint155, viewCenter155)
    
    scaleAboutPoint156 = NXOpen.Point3d(39.026521201577673, -38.752330186109766, 0.0)
    viewCenter156 = NXOpen.Point3d(-39.026521201577516, 38.75233018610988, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint156, viewCenter156)
    
    scaleAboutPoint157 = NXOpen.Point3d(48.78315150197205, -48.440412732637228, 0.0)
    viewCenter157 = NXOpen.Point3d(-48.783151501971894, 48.440412732637348, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint157, viewCenter157)
    
    scaleAboutPoint158 = NXOpen.Point3d(60.978939377465061, -60.550515915796531, 0.0)
    viewCenter158 = NXOpen.Point3d(-60.978939377464862, 60.550515915796659, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint158, viewCenter158)
    
    scaleAboutPoint159 = NXOpen.Point3d(88.362338969101813, -112.81817823933795, 0.0)
    viewCenter159 = NXOpen.Point3d(-88.362338969101685, 112.81817823933814, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint159, viewCenter159)
    
    scaleAboutPoint160 = NXOpen.Point3d(70.68987117528151, -90.254542591470369, 0.0)
    viewCenter160 = NXOpen.Point3d(-70.689871175281311, 90.254542591470511, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint160, viewCenter160)
    
    scaleAboutPoint161 = NXOpen.Point3d(56.551896940225205, -72.203634073176289, 0.0)
    viewCenter161 = NXOpen.Point3d(-56.551896940225049, 72.203634073176431, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint161, viewCenter161)
    
    scaleAboutPoint162 = NXOpen.Point3d(37.929757139706652, -48.440412732637235, 0.0)
    viewCenter162 = NXOpen.Point3d(-37.929757139706489, 48.440412732637384, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint162, viewCenter162)
    
    scaleAboutPoint163 = NXOpen.Point3d(30.782511336513743, -38.606094977860302, 0.0)
    viewCenter163 = NXOpen.Point3d(-30.78251133651354, 38.60609497786043, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint163, viewCenter163)
    
    point29 = NXOpen.Point3d(-15.262782718895696, -8.4982225858996578, -80.0)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(line13, workPart.ModelingViews.WorkView, point29)
    
    point1_18 = NXOpen.Point3d(-9.9999999999969074, -8.4982225858996543, -80.0)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line13, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    point1_19 = NXOpen.Point3d(-25.000000000000007, -8.4982225858996649, -80.0)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line13, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    dimensionlinearunits301 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits302 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits303 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits304 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits305 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits306 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits307 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits308 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits309 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits310 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits311 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits312 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder12.Destroy()
    
    theSession.UndoToMark(markId139, None)
    
    theSession.DeleteUndoMark(markId139, None)
    
    sketchRapidDimensionBuilder12.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId140 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder13 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines69 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBefore(lines69)
    
    lines70 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAfter(lines70)
    
    lines71 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAbove(lines71)
    
    lines72 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBelow(lines72)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder13.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines73 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBefore(lines73)
    
    lines74 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAfter(lines74)
    
    lines75 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAbove(lines75)
    
    lines76 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBelow(lines76)
    
    theSession.SetUndoMarkName(markId140, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder13.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits313 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits314 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits315 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits316 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits317 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits318 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits319 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits320 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits321 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits322 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder13.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits323 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits324 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits325 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits326 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits327 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits328 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits329 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits330 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits331 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits332 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    edge3 = extrude1.FindObject("EDGE * 120 * 160 {(25,25,-80)(0,25,-80)(-25,25,-80) EXTRUDE(2)}")
    point30 = NXOpen.Point3d(-19.708333049679617, 24.999999999999993, -80.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(edge3, workPart.ModelingViews.WorkView, point30)
    
    point1_20 = NXOpen.Point3d(-17.499999999996902, 6.5017774141003457, -80.0)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, line11, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    dimensionlinearunits333 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits334 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits335 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits336 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits337 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits338 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin8 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin8.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin8.View = NXOpen.View.Null
    assocOrigin8.ViewOfGeometry = workPart.ModelingViews.WorkView
    point31 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin8.PointOnGeometry = point31
    assocOrigin8.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.DimensionLine = 0
    assocOrigin8.AssociatedView = NXOpen.View.Null
    assocOrigin8.AssociatedPoint = NXOpen.Point.Null
    assocOrigin8.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.XOffsetFactor = 0.0
    assocOrigin8.YOffsetFactor = 0.0
    assocOrigin8.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder13.Origin.SetAssociativeOrigin(assocOrigin8)
    
    point32 = NXOpen.Point3d(-41.819096536999666, 18.092737821857419, -80.0)
    sketchRapidDimensionBuilder13.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point32)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.TextCentered = False
    
    markId141 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject17 = sketchRapidDimensionBuilder13.Commit()
    
    theSession.DeleteUndoMark(markId141, None)
    
    theSession.SetUndoMarkName(markId140, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId140, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder13.Destroy()
    
    markId142 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder14 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines77 = []
    sketchRapidDimensionBuilder14.AppendedText.SetBefore(lines77)
    
    lines78 = []
    sketchRapidDimensionBuilder14.AppendedText.SetAfter(lines78)
    
    lines79 = []
    sketchRapidDimensionBuilder14.AppendedText.SetAbove(lines79)
    
    lines80 = []
    sketchRapidDimensionBuilder14.AppendedText.SetBelow(lines80)
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder14.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId142, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder14.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits339 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits340 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits341 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits342 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits343 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits344 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits345 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits346 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits347 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits348 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder14.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits349 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits350 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits351 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits352 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits353 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits354 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits355 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits356 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits357 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits358 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    expression73 = workPart.Expressions.FindObject("p13")
    expression73.SetFormula("17.5")
    
    theSession.SetUndoMarkVisibility(markId142, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId143 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId143, None)
    
    markId144 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId142, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder14.Destroy()
    
    theSession.UndoToMark(markId144, None)
    
    theSession.DeleteUndoMark(markId144, None)
    
    sketchRapidDimensionBuilder14.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId145 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId125, None)
    
    section6.DistanceTolerance = 0.01
    
    section6.ChainingTolerance = 0.0094999999999999998
    
    markId146 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves3 = [NXOpen.ICurve.Null] * 4 
    curves3[0] = line11
    curves3[1] = line12
    curves3[2] = line13
    curves3[3] = line14
    seedPoint3 = NXOpen.Point3d(-14.999999999996904, -2.5000000000000093, -80.0)
    regionBoundaryRule3 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch6, curves3, seedPoint3, 0.01)
    
    section6.AllowSelfIntersection(True)
    
    rules4 = [None] * 1 
    rules4[0] = regionBoundaryRule3
    helpPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section6.AddToSection(rules4, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint4, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId146, None)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs5 = section6.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression74)
    
    expression75 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction10 = workPart.Directions.CreateDirection(sketch6, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder8.Direction = direction10
    
    targetBodies26 = [NXOpen.Body.Null] * 1 
    targetBodies26[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies26)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies27 = [NXOpen.Body.Null] * 1 
    targetBodies27[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies27)
    
    rotMatrix26 = NXOpen.Matrix3x3()
    
    rotMatrix26.Xx = 0.85966911615350838
    rotMatrix26.Xy = 0.062302798345871546
    rotMatrix26.Xz = -0.5070378408463363
    rotMatrix26.Yx = 0.10035000502941219
    rotMatrix26.Yy = -0.99379235081095096
    rotMatrix26.Yz = 0.048027491712931719
    rotMatrix26.Zx = -0.50089808067354258
    rotMatrix26.Zy = -0.092169001230958725
    rotMatrix26.Zz = -0.86058467798912219
    translation26 = NXOpen.Point3d(23.814094072935017, -8.6905775890130101, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix26, translation26, 5.3985313952536469)
    
    scaleAboutPoint164 = NXOpen.Point3d(-15.536246902334797, 0.44109218334710759, 0.0)
    viewCenter164 = NXOpen.Point3d(15.536246902334815, -0.44109218334698219, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint164, viewCenter164)
    
    scaleAboutPoint165 = NXOpen.Point3d(-12.428997521867833, 0.35287374667769617, 0.0)
    viewCenter165 = NXOpen.Point3d(12.428997521867853, -0.35287374667757576, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint165, viewCenter165)
    
    scaleAboutPoint166 = NXOpen.Point3d(-9.9745645727545007, 0.28229899734217029, 0.0)
    viewCenter166 = NXOpen.Point3d(9.9745645727545167, -0.28229899734204994, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint166, viewCenter166)
    
    scaleAboutPoint167 = NXOpen.Point3d(-7.9796516582036014, 0.2258391978737469, 0.0)
    viewCenter167 = NXOpen.Point3d(7.9796516582036139, -0.22583919787362494, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint167, viewCenter167)
    
    scaleAboutPoint168 = NXOpen.Point3d(-6.3837213265628803, 0.18067135829900952, 0.0)
    viewCenter168 = NXOpen.Point3d(6.383721326562898, -0.18067135829888969, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint168, viewCenter168)
    
    scaleAboutPoint169 = NXOpen.Point3d(-5.1390964138367865, 0.12847741034597956, 0.0)
    viewCenter169 = NXOpen.Point3d(5.1390964138367972, -0.12847741034586044, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint169, viewCenter169)
    
    scaleAboutPoint170 = NXOpen.Point3d(-6.4238705172959829, 0.16059676293245909, 0.0)
    viewCenter170 = NXOpen.Point3d(6.423870517295998, -0.16059676293234271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint170, viewCenter170)
    
    scaleAboutPoint171 = NXOpen.Point3d(-8.0549313908281679, 0.20074595366555675, 0.0)
    viewCenter171 = NXOpen.Point3d(8.0549313908281803, -0.20074595366544123, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint171, viewCenter171)
    
    scaleAboutPoint172 = NXOpen.Point3d(-10.068664238535213, 0.25093244208192989, 0.0)
    viewCenter172 = NXOpen.Point3d(10.068664238535229, -0.25093244208181753, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint172, viewCenter172)
    
    scaleAboutPoint173 = NXOpen.Point3d(-12.585830298169011, 0.31366555260239892, 0.0)
    viewCenter173 = NXOpen.Point3d(12.585830298169027, -0.31366555260228524, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint173, viewCenter173)
    
    scaleAboutPoint174 = NXOpen.Point3d(-15.73228787271127, 0.39208194075298602, 0.0)
    viewCenter174 = NXOpen.Point3d(15.732287872711279, -0.39208194075287323, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint174, viewCenter174)
    
    scaleAboutPoint175 = NXOpen.Point3d(-19.726622644131737, 0.490102425941217, 0.0)
    viewCenter175 = NXOpen.Point3d(19.726622644131748, -0.49010242594110209, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint175, viewCenter175)
    
    scaleAboutPoint176 = NXOpen.Point3d(-25.34748484164443, 0.99552055269303807, 0.0)
    viewCenter176 = NXOpen.Point3d(25.347484841644444, -0.9955205526929205, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint176, viewCenter176)
    
    scaleAboutPoint177 = NXOpen.Point3d(-31.684356052055545, 1.2444006908662897, 0.0)
    viewCenter177 = NXOpen.Point3d(31.684356052055545, -1.2444006908661591, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint177, viewCenter177)
    
    scaleAboutPoint178 = NXOpen.Point3d(-39.605445065069418, 1.5555008635828411, 0.0)
    viewCenter178 = NXOpen.Point3d(39.605445065069439, -1.5555008635827186, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint178, viewCenter178)
    
    scaleAboutPoint179 = NXOpen.Point3d(-49.506806331336747, 1.9443760794785381, 0.0)
    viewCenter179 = NXOpen.Point3d(49.506806331336776, -1.9443760794784106, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint179, viewCenter179)
    
    scaleAboutPoint180 = NXOpen.Point3d(29.352600430588641, -15.517616788145547, 0.0)
    viewCenter180 = NXOpen.Point3d(-29.352600430588609, 15.517616788145641, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint180, viewCenter180)
    
    scaleAboutPoint181 = NXOpen.Point3d(23.781215125929162, -12.414093430516438, 0.0)
    viewCenter181 = NXOpen.Point3d(-23.781215125929112, 12.414093430516527, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint181, viewCenter181)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies28 = [NXOpen.Body.Null] * 1 
    targetBodies28[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies28)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies29 = [NXOpen.Body.Null] * 1 
    targetBodies29[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies29)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies30 = [NXOpen.Body.Null] * 1 
    targetBodies30[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies30)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies31 = [NXOpen.Body.Null] * 1 
    targetBodies31[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies31)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies32 = [NXOpen.Body.Null] * 1 
    targetBodies32[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies32)
    
    direction11 = extrudeBuilder8.Direction
    
    success2 = direction11.ReverseDirection()
    
    extrudeBuilder8.Direction = direction11
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies33 = [NXOpen.Body.Null] * 1 
    targetBodies33[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies33)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies34 = [NXOpen.Body.Null] * 1 
    targetBodies34[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies34)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies35 = [NXOpen.Body.Null] * 1 
    targetBodies35[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies35)
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies36 = [NXOpen.Body.Null] * 1 
    targetBodies36[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies36)
    
    extrudeBuilder8.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies37 = [NXOpen.Body.Null] * 1 
    targetBodies37[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies37)
    
    extrudeBuilder8.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies38 = [NXOpen.Body.Null] * 1 
    targetBodies38[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies38)
    
    extrudeBuilder8.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder8.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies39 = [NXOpen.Body.Null] * 1 
    targetBodies39[0] = body1
    extrudeBuilder8.BooleanOperation.SetTargetBodies(targetBodies39)
    
    markId147 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId147, None)
    
    markId148 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder8.ParentFeatureInternal = True
    
    feature9 = extrudeBuilder8.CommitFeature()
    
    theSession.DeleteUndoMark(markId148, None)
    
    theSession.SetUndoMarkName(markId124, "Extrude")
    
    expression76 = extrudeBuilder8.Limits.StartExtend.Value
    expression77 = extrudeBuilder8.Limits.EndExtend.Value
    extrudeBuilder8.Destroy()
    
    workPart.Expressions.Delete(expression68)
    
    workPart.Expressions.Delete(expression75)
    
    rotMatrix27 = NXOpen.Matrix3x3()
    
    rotMatrix27.Xx = 0.9121637838000336
    rotMatrix27.Xy = 0.057574929588170953
    rotMatrix27.Xz = -0.40576145579209794
    rotMatrix27.Yx = -0.024723198237205937
    rotMatrix27.Yy = -0.98054882089926243
    rotMatrix27.Yz = -0.1947120265982292
    rotMatrix27.Zx = -0.40907944826467302
    rotMatrix27.Zy = 0.18764097984177883
    rotMatrix27.Zz = -0.8929976862744311
    translation27 = NXOpen.Point3d(-32.320881558427359, -1.4816904732528489, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix27, translation27, 2.2112384594958954)
    
    rotMatrix28 = NXOpen.Matrix3x3()
    
    rotMatrix28.Xx = 0.9129407518248992
    rotMatrix28.Xy = -0.011945455075774849
    rotMatrix28.Xz = -0.40791725847335669
    rotMatrix28.Yx = -0.078073238620092827
    rotMatrix28.Yy = -0.98622101069031021
    rotMatrix28.Yz = -0.14585159404117692
    rotMatrix28.Zx = -0.40055430726526575
    rotMatrix28.Zy = 0.16500128537685663
    rotMatrix28.Zz = -0.90129397132968081
    translation28 = NXOpen.Point3d(-32.320881558427359, -1.4816904732528489, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix28, translation28, 2.2112384594958954)
    
    rotMatrix29 = NXOpen.Matrix3x3()
    
    rotMatrix29.Xx = 0.91310482499177525
    rotMatrix29.Xy = -0.010141064917178217
    rotMatrix29.Xz = -0.40759874555631675
    rotMatrix29.Yx = -0.037191789093681454
    rotMatrix29.Yy = -0.99759453887176797
    rotMatrix29.Yz = -0.05849706691136404
    rotMatrix29.Zx = -0.40602506006495259
    rotMatrix29.Zy = 0.068573280624212959
    rotMatrix29.Zz = -0.91128555117684196
    translation29 = NXOpen.Point3d(-32.320881558427359, -1.4816904732528489, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix29, translation29, 2.2112384594958954)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId149 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression78 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression79 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression81 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId149, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    extrude4 = feature9
    edge4 = extrude4.FindObject("EDGE * 130 * 160 {(-9.9999999999969,-7.5,-65)(-9.9999999999969,-0,-65)(-9.9999999999969,7.5,-65) EXTRUDE(2)}")
    seedEdges1[0] = edge4
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules5 = [None] * 1 
    rules5[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules5, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    rotMatrix30 = NXOpen.Matrix3x3()
    
    rotMatrix30.Xx = 0.86351082048810845
    rotMatrix30.Xy = -0.013838303118059
    rotMatrix30.Xz = -0.50414042117922264
    rotMatrix30.Yx = 0.20096777155877965
    rotMatrix30.Yy = -0.90738813917541083
    rotMatrix30.Yz = 0.36913238773978896
    rotMatrix30.Zx = -0.46255920452915927
    rotMatrix30.Zy = -0.42006578800301342
    rotMatrix30.Zz = -0.78075842362074632
    translation30 = NXOpen.Point3d(-32.320881558427359, -1.4816904732528489, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix30, translation30, 2.2112384594958954)
    
    scaleAboutPoint182 = NXOpen.Point3d(-14.717431247744791, -0.11965391258325384, 0.0)
    viewCenter182 = NXOpen.Point3d(14.717431247744843, 0.11965391258333545, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint182, viewCenter182)
    
    scaleAboutPoint183 = NXOpen.Point3d(-11.773944998195818, -0.095723130066594914, 0.0)
    viewCenter183 = NXOpen.Point3d(11.773944998195899, 0.095723130066676529, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint183, viewCenter183)
    
    scaleAboutPoint184 = NXOpen.Point3d(-9.3425774945033453, -0.076578504053262858, 0.0)
    viewCenter184 = NXOpen.Point3d(9.3425774945034235, 0.076578504053354271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint184, viewCenter184)
    
    scaleAboutPoint185 = NXOpen.Point3d(-7.4740619956026748, -0.061262803242599834, 0.0)
    viewCenter185 = NXOpen.Point3d(7.4740619956027476, 0.061262803242693856, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint185, viewCenter185)
    
    scaleAboutPoint186 = NXOpen.Point3d(-5.9792495964821342, -0.049010242594071496, 0.0)
    viewCenter186 = NXOpen.Point3d(5.9792495964821928, 0.049010242594163429, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint186, viewCenter186)
    
    scaleAboutPoint187 = NXOpen.Point3d(-7.4740619956026721, -0.061262803242599813, 0.0)
    viewCenter187 = NXOpen.Point3d(7.4740619956027352, 0.061262803242693835, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint187, viewCenter187)
    
    scaleAboutPoint188 = NXOpen.Point3d(-9.3425774945033577, -0.076578504053262816, 0.0)
    viewCenter188 = NXOpen.Point3d(9.3425774945034235, 0.076578504053360752, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint188, viewCenter188)
    
    scaleAboutPoint189 = NXOpen.Point3d(-11.678221868129192, -0.095723130066586698, 0.0)
    viewCenter189 = NXOpen.Point3d(11.678221868129258, 0.095723130066684634, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint189, viewCenter189)
    
    scaleAboutPoint190 = NXOpen.Point3d(-14.597777335161501, -0.11965391258324358, 0.0)
    viewCenter190 = NXOpen.Point3d(14.597777335161553, 0.1196539125833456, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint190, viewCenter190)
    
    scaleAboutPoint191 = NXOpen.Point3d(-18.247221668951887, -0.14956739072906719, 0.0)
    viewCenter191 = NXOpen.Point3d(18.247221668951937, 0.14956739072916922, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint191, viewCenter191)
    
    scaleAboutPoint192 = NXOpen.Point3d(-22.809027086189861, -0.18695923841133402, 0.0)
    viewCenter192 = NXOpen.Point3d(22.809027086189925, 0.1869592384114456, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint192, viewCenter192)
    
    rotMatrix31 = NXOpen.Matrix3x3()
    
    rotMatrix31.Xx = 0.83856973590576955
    rotMatrix31.Xy = -0.035431330667953675
    rotMatrix31.Xz = -0.54364089142560224
    rotMatrix31.Yx = 0.33808606943931141
    rotMatrix31.Yy = -0.74864189739801812
    rotMatrix31.Yz = 0.57029213488471509
    rotMatrix31.Zx = -0.42719855766844694
    rotMatrix31.Zy = -0.66202713710797934
    rotMatrix31.Zz = -0.61580959886851794
    translation31 = NXOpen.Point3d(-46.191312672473202, -1.5957356086838017, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix31, translation31, 1.1321540912618986)
    
    rules6 = []
    scCollector1.ReplaceRules(rules6, False)
    
    rotMatrix32 = NXOpen.Matrix3x3()
    
    rotMatrix32.Xx = 0.87662387198754799
    rotMatrix32.Xy = 0.027590899321650798
    rotMatrix32.Xz = -0.48038456400698276
    rotMatrix32.Yx = 0.072493214078815441
    rotMatrix32.Yy = -0.99453235328903467
    rotMatrix32.Yz = 0.075167361094363172
    rotMatrix32.Zx = -0.4756840558333631
    rotMatrix32.Zy = -0.10071812416834355
    rotMatrix32.Zz = -0.87383095532827382
    translation32 = NXOpen.Point3d(-46.191312672473202, -1.5957356086838017, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix32, translation32, 1.1321540912618986)
    
    seedEdges2 = [NXOpen.Edge.Null] * 1 
    seedEdges2[0] = edge4
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules7 = [None] * 1 
    rules7[0] = edgeMultipleSeedTangentRule2
    scCollector1.ReplaceRules(rules7, False)
    
    rotMatrix33 = NXOpen.Matrix3x3()
    
    rotMatrix33.Xx = 0.83725065557002798
    rotMatrix33.Xy = -0.016779142266099899
    rotMatrix33.Xz = -0.54656179900572299
    rotMatrix33.Yx = 0.54312238816916836
    rotMatrix33.Yy = -0.090513231968137875
    rotMatrix33.Yz = 0.83476070002612046
    rotMatrix33.Zx = -0.063477643442215084
    rotMatrix33.Zy = -0.99575389289899041
    rotMatrix33.Zz = -0.066669134984090911
    translation33 = NXOpen.Point3d(-46.191312672473202, -1.5957356086838017, -66.686065019846609)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix33, translation33, 1.1321540912618986)
    
    scaleAboutPoint193 = NXOpen.Point3d(-20.565516225253159, -46.272411506819573, 0.0)
    viewCenter193 = NXOpen.Point3d(20.565516225253198, 46.272411506819694, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint193, viewCenter193)
    
    scaleAboutPoint194 = NXOpen.Point3d(-14.956739072911375, -44.683257980322729, 0.0)
    viewCenter194 = NXOpen.Point3d(14.956739072911439, 44.683257980322857, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint194, viewCenter194)
    
    scaleAboutPoint195 = NXOpen.Point3d(-11.965391258329113, -35.746606384258179, 0.0)
    viewCenter195 = NXOpen.Point3d(11.965391258329138, 35.746606384258307, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint195, viewCenter195)
    
    scaleAboutPoint196 = NXOpen.Point3d(-9.6919669192465765, -30.631401621322485, 0.0)
    viewCenter196 = NXOpen.Point3d(9.691966919246596, 30.63140162132261, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint196, viewCenter196)
    
    scaleAboutPoint197 = NXOpen.Point3d(-5.8391109340646121, -28.525492759856565, 0.0)
    viewCenter197 = NXOpen.Point3d(5.8391109340646121, 28.525492759856686, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint197, viewCenter197)
    
    scaleAboutPoint198 = NXOpen.Point3d(-3.8289252026653213, -24.275385784898056, 0.0)
    viewCenter198 = NXOpen.Point3d(3.8289252026653346, 24.275385784898173, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint198, viewCenter198)
    
    scaleAboutPoint199 = NXOpen.Point3d(-3.0631401621322576, -19.420308627918438, 0.0)
    viewCenter199 = NXOpen.Point3d(3.0631401621322576, 19.420308627918551, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint199, viewCenter199)
    
    scaleAboutPoint200 = NXOpen.Point3d(-2.4505121297058063, -15.536246902334739, 0.0)
    viewCenter200 = NXOpen.Point3d(2.4505121297058063, 15.536246902334856, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint200, viewCenter200)
    
    scaleAboutPoint201 = NXOpen.Point3d(-3.0631401621322576, -19.420308627918438, 0.0)
    viewCenter201 = NXOpen.Point3d(3.0631401621322474, 19.420308627918551, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint201, viewCenter201)
    
    scaleAboutPoint202 = NXOpen.Point3d(-3.8289252026653213, -24.275385784898056, 0.0)
    viewCenter202 = NXOpen.Point3d(3.8289252026653213, 24.275385784898173, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint202, viewCenter202)
    
    scaleAboutPoint203 = NXOpen.Point3d(-4.7861565033316529, -30.344232231122593, 0.0)
    viewCenter203 = NXOpen.Point3d(4.7861565033316529, 30.344232231122707, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint203, viewCenter203)
    
    scaleAboutPoint204 = NXOpen.Point3d(-5.9826956291645663, -37.930290288903258, 0.0)
    viewCenter204 = NXOpen.Point3d(5.9826956291645663, 37.930290288903372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint204, viewCenter204)
    
    scaleAboutPoint205 = NXOpen.Point3d(-7.4783695364557063, -47.412862861129085, 0.0)
    viewCenter205 = NXOpen.Point3d(7.4783695364556939, 47.412862861129199, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint205, viewCenter205)
    
    scaleAboutPoint206 = NXOpen.Point3d(-9.3479619205696345, -59.266078576411374, 0.0)
    viewCenter206 = NXOpen.Point3d(9.3479619205696345, 59.266078576411473, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint206, viewCenter206)
    
    scaleAboutPoint207 = NXOpen.Point3d(-11.684952400712042, -74.082598220514214, 0.0)
    viewCenter207 = NXOpen.Point3d(11.684952400712042, 74.082598220514342, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint207, viewCenter207)
    
    scaleAboutPoint208 = NXOpen.Point3d(-14.606190500890053, -92.603247775642771, 0.0)
    viewCenter208 = NXOpen.Point3d(14.606190500890053, 92.603247775642885, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint208, viewCenter208)
    
    scaleAboutPoint209 = NXOpen.Point3d(-17.527428601068042, -138.39365499593302, 0.0)
    viewCenter209 = NXOpen.Point3d(17.527428601068042, 138.39365499593316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint209, viewCenter209)
    
    scaleAboutPoint210 = NXOpen.Point3d(-14.021942880854434, -110.71492399674641, 0.0)
    viewCenter210 = NXOpen.Point3d(14.021942880854434, 110.71492399674652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint210, viewCenter210)
    
    scaleAboutPoint211 = NXOpen.Point3d(-11.217554304683587, -88.805638245411416, 0.0)
    viewCenter211 = NXOpen.Point3d(11.217554304683508, 88.805638245411487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint211, viewCenter211)
    
    scaleAboutPoint212 = NXOpen.Point3d(-7.4783695364557357, -67.86620354333543, 0.0)
    viewCenter212 = NXOpen.Point3d(7.4783695364556717, 67.86620354333553, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint212, viewCenter212)
    
    scaleAboutPoint213 = NXOpen.Point3d(-5.3844260662481531, -52.797288927377195, 0.0)
    viewCenter213 = NXOpen.Point3d(5.3844260662480767, 52.797288927377274, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint213, viewCenter213)
    
    scaleAboutPoint214 = NXOpen.Point3d(-4.3075408529985237, -42.237831141901765, 0.0)
    viewCenter214 = NXOpen.Point3d(4.307540852998442, 42.237831141901815, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint214, viewCenter214)
    
    scaleAboutPoint215 = NXOpen.Point3d(-3.446032682398835, -33.790264913521405, 0.0)
    viewCenter215 = NXOpen.Point3d(3.4460326823987373, 33.790264913521462, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint215, viewCenter215)
    
    scaleAboutPoint216 = NXOpen.Point3d(-2.7568261459190806, -27.032211930817116, 0.0)
    viewCenter216 = NXOpen.Point3d(2.7568261459189891, 27.032211930817169, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint216, viewCenter216)
    
    scaleAboutPoint217 = NXOpen.Point3d(-3.446032682398835, -33.790264913521405, 0.0)
    viewCenter217 = NXOpen.Point3d(3.4460326823987373, 33.790264913521462, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint217, viewCenter217)
    
    scaleAboutPoint218 = NXOpen.Point3d(-4.3075408529985237, -42.237831141901765, 0.0)
    viewCenter218 = NXOpen.Point3d(4.307540852998442, 42.237831141901829, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint218, viewCenter218)
    
    scaleAboutPoint219 = NXOpen.Point3d(-5.3844260662481283, -52.797288927377217, 0.0)
    viewCenter219 = NXOpen.Point3d(5.3844260662480519, 52.797288927377281, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint219, viewCenter219)
    
    scaleAboutPoint220 = NXOpen.Point3d(-6.7305325828101914, -65.996611159221501, 0.0)
    viewCenter220 = NXOpen.Point3d(6.7305325828100955, 65.996611159221573, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint220, viewCenter220)
    
    scaleAboutPoint221 = NXOpen.Point3d(-8.4131657285127392, -82.495763949026909, 0.0)
    viewCenter221 = NXOpen.Point3d(8.4131657285126202, 82.495763949026937, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint221, viewCenter221)
    
    scaleAboutPoint222 = NXOpen.Point3d(-7.0109714404272658, -104.58032398637262, 0.0)
    viewCenter222 = NXOpen.Point3d(7.0109714404271664, 104.58032398637265, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint222, viewCenter222)
    
    scaleAboutPoint223 = NXOpen.Point3d(-5.6087771523418128, -83.664259189098118, 0.0)
    viewCenter223 = NXOpen.Point3d(5.6087771523417329, 83.664259189098118, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint223, viewCenter223)
    
    scaleAboutPoint224 = NXOpen.Point3d(-4.4870217218734512, -66.931407351278523, 0.0)
    viewCenter224 = NXOpen.Point3d(4.4870217218733872, 66.931407351278509, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint224, viewCenter224)
    
    scaleAboutPoint225 = NXOpen.Point3d(-3.5896173774987354, -53.54512588102282, 0.0)
    viewCenter225 = NXOpen.Point3d(3.5896173774987226, 53.545125881022784, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint225, viewCenter225)
    
    scaleAboutPoint226 = NXOpen.Point3d(-2.8716939019989889, -42.836100704818271, 0.0)
    viewCenter226 = NXOpen.Point3d(2.8716939019989889, 42.836100704818236, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint226, viewCenter226)
    
    scaleAboutPoint227 = NXOpen.Point3d(-2.2973551215991908, -34.26888056385463, 0.0)
    viewCenter227 = NXOpen.Point3d(2.2973551215991908, 34.268880563854573, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint227, viewCenter227)
    
    rotMatrix34 = NXOpen.Matrix3x3()
    
    rotMatrix34.Xx = 0.72798492297978235
    rotMatrix34.Xy = -0.21269107545126975
    rotMatrix34.Xz = -0.65176718108347653
    rotMatrix34.Yx = 0.092225966015025043
    rotMatrix34.Yy = -0.91164079425115307
    rotMatrix34.Yz = 0.40050647117084398
    rotMatrix34.Zx = -0.6793617027082951
    rotMatrix34.Zy = -0.35167253046052455
    rotMatrix34.Zz = -0.64404511349188531
    translation34 = NXOpen.Point3d(-44.82705395048491, 23.61321207285949, -104.71703417875014)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix34, translation34, 3.4550600929623365)
    
    scCollector1.Destroy()
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression81)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression80)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression78)
    
    workPart.Expressions.Delete(expression79)
    
    theSession.UndoToMark(markId149, None)
    
    theSession.DeleteUndoMark(markId149, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId150 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete5 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId151 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects9 = [NXOpen.TaggedObject.Null] * 1 
    objects9[0] = extrude4
    nErrs8 = theSession.UpdateManager.AddObjectsToDeleteList(objects9)
    
    notifyOnDelete6 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id3 = theSession.NewestVisibleUndoMark
    
    nErrs9 = theSession.UpdateManager.DoUpdate(id3)
    
    theSession.DeleteUndoMark(markId150, None)
    
    rotMatrix35 = NXOpen.Matrix3x3()
    
    rotMatrix35.Xx = 0.94794205198605763
    rotMatrix35.Xy = -0.066720344165089138
    rotMatrix35.Xz = -0.3113747930564561
    rotMatrix35.Yx = 0.027607581091262531
    rotMatrix35.Yy = -0.95690375717830523
    rotMatrix35.Yz = 0.28908998765839555
    rotMatrix35.Zx = -0.31724389283758947
    rotMatrix35.Zy = -0.28263686095860446
    rotMatrix35.Zz = -0.90524732382079609
    translation35 = NXOpen.Point3d(-44.82705395048491, 23.61321207285949, -104.71703417875014)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix35, translation35, 3.4550600929623401)
    
    scaleAboutPoint228 = NXOpen.Point3d(-21.748295151138986, 7.2749578850640715, 0.0)
    viewCenter228 = NXOpen.Point3d(21.748295151138986, -7.2749578850641301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint228, viewCenter228)
    
    scaleAboutPoint229 = NXOpen.Point3d(-17.398636120911199, 5.819966308051252, 0.0)
    viewCenter229 = NXOpen.Point3d(17.398636120911178, -5.8199663080512982, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint229, viewCenter229)
    
    scaleAboutPoint230 = NXOpen.Point3d(-13.918908896728963, 4.6559730464409981, 0.0)
    viewCenter230 = NXOpen.Point3d(13.918908896728945, -4.6559730464410523, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint230, viewCenter230)
    
    scaleAboutPoint231 = NXOpen.Point3d(-11.135127117383171, 3.7247784371527985, 0.0)
    viewCenter231 = NXOpen.Point3d(11.135127117383156, -3.7247784371528421, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint231, viewCenter231)
    
    scaleAboutPoint232 = NXOpen.Point3d(-8.9081016939065361, 2.9798227497222309, 0.0)
    viewCenter232 = NXOpen.Point3d(8.9081016939065236, -2.9798227497222793, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint232, viewCenter232)
    
    scaleAboutPoint233 = NXOpen.Point3d(-7.1264813551252297, 2.3838581997777806, 0.0)
    viewCenter233 = NXOpen.Point3d(7.1264813551252191, -2.3838581997778321, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint233, viewCenter233)
    
    scaleAboutPoint234 = NXOpen.Point3d(-5.6811104887336352, 1.9070865598222189, 0.0)
    viewCenter234 = NXOpen.Point3d(5.681110488733621, -1.9070865598222684, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint234, viewCenter234)
    
    scaleAboutPoint235 = NXOpen.Point3d(-4.5448883909869107, 1.5256692478577696, 0.0)
    viewCenter235 = NXOpen.Point3d(4.5448883909868947, -1.5256692478578189, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint235, viewCenter235)
    
    scaleAboutPoint236 = NXOpen.Point3d(-5.6811104887336352, 1.9070865598222189, 0.0)
    viewCenter236 = NXOpen.Point3d(5.681110488733621, -1.9070865598222666, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint236, viewCenter236)
    
    scaleAboutPoint237 = NXOpen.Point3d(-7.10138811091704, 2.3838581997777801, 0.0)
    viewCenter237 = NXOpen.Point3d(7.1013881109170276, -2.3838581997778294, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint237, viewCenter237)
    
    scaleAboutPoint238 = NXOpen.Point3d(-8.8767351386462998, 2.9798227497222305, 0.0)
    viewCenter238 = NXOpen.Point3d(8.8767351386462892, -2.9798227497222816, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint238, viewCenter238)
    
    scaleAboutPoint239 = NXOpen.Point3d(-11.095918923307876, 3.724778437152795, 0.0)
    viewCenter239 = NXOpen.Point3d(11.095918923307863, -3.7247784371528452, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint239, viewCenter239)
    
    scaleAboutPoint240 = NXOpen.Point3d(-13.869898654134845, 4.6559730464409981, 0.0)
    viewCenter240 = NXOpen.Point3d(13.869898654134827, -4.6559730464410478, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint240, viewCenter240)
    
    scaleAboutPoint241 = NXOpen.Point3d(-17.337373317668558, 5.8199663080512538, 0.0)
    viewCenter241 = NXOpen.Point3d(17.337373317668536, -5.8199663080513053, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint241, viewCenter241)
    
    scaleAboutPoint242 = NXOpen.Point3d(-21.671716647085685, 7.2749578850640795, 0.0)
    viewCenter242 = NXOpen.Point3d(21.671716647085677, -7.2749578850641257, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint242, viewCenter242)
    
    scaleAboutPoint243 = NXOpen.Point3d(-27.089645808857121, 9.0936973563301002, 0.0)
    viewCenter243 = NXOpen.Point3d(27.089645808857089, -9.0936973563301411, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint243, viewCenter243)
    
    scaleAboutPoint244 = NXOpen.Point3d(-33.862057261071399, 11.367121695412633, 0.0)
    viewCenter244 = NXOpen.Point3d(33.862057261071357, -11.367121695412674, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint244, viewCenter244)
    
    scaleAboutPoint245 = NXOpen.Point3d(-42.925841139255674, 14.20890211926579, 0.0)
    viewCenter245 = NXOpen.Point3d(42.925841139255674, -14.208902119265829, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint245, viewCenter245)
    
    scaleAboutPoint246 = NXOpen.Point3d(-53.844260662480977, 17.761127649082237, 0.0)
    viewCenter246 = NXOpen.Point3d(53.844260662480977, -17.761127649082301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint246, viewCenter246)
    
    scaleAboutPoint247 = NXOpen.Point3d(-67.305325828101203, 22.201409561352797, 0.0)
    viewCenter247 = NXOpen.Point3d(67.305325828101246, -22.201409561352857, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint247, viewCenter247)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId152 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder9 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section7 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder9.Section = section7
    
    extrudeBuilder9.AllowSelfIntersectingSection(True)
    
    expression82 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder9.DistanceTolerance = 0.01
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies40 = [NXOpen.Body.Null] * 1 
    targetBodies40[0] = NXOpen.Body.Null
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies40)
    
    extrudeBuilder9.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder9.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies41 = [NXOpen.Body.Null] * 1 
    targetBodies41[0] = NXOpen.Body.Null
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies41)
    
    extrudeBuilder9.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder9.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder9.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder9.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder7 = extrudeBuilder9.SmartVolumeProfile
    
    smartVolumeProfileBuilder7.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder7.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId152, "Extrude Dialog")
    
    section7.DistanceTolerance = 0.01
    
    section7.ChainingTolerance = 0.0094999999999999998
    
    section7.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar5 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point33 = workPart.Points.CreatePoint(edge2, scalar5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction12 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction12, point33, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem6 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder5 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder5.Csys = cartesianCoordinateSystem6
    
    datumCsysBuilder5.DisplayScaleFactor = 1.25
    
    feature10 = datumCsysBuilder5.CommitFeature()
    
    datumCsysBuilder5.Destroy()
    
    markId153 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder9 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder9.Csystem = cartesianCoordinateSystem6
    
    sketchInPlaceBuilder9.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject18 = sketchInPlaceBuilder9.Commit()
    
    sketchInPlaceBuilder9.Destroy()
    
    sketch7 = nXObject18
    sketch7.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId154 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId154, None, True)
    
    markId155 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId156 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint248 = NXOpen.Point3d(51.267728658124007, -35.931228632189494, 0.0)
    viewCenter248 = NXOpen.Point3d(-51.267728658123957, 35.931228632189466, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint248, viewCenter248)
    
    scaleAboutPoint249 = NXOpen.Point3d(47.287541746631476, -40.532178639969828, 0.0)
    viewCenter249 = NXOpen.Point3d(-47.287541746631348, 40.532178639969764, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint249, viewCenter249)
    
    scaleAboutPoint250 = NXOpen.Point3d(57.740096823830847, -49.752336393656684, 0.0)
    viewCenter250 = NXOpen.Point3d(-57.740096823830768, 49.752336393656606, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint250, viewCenter250)
    
    scaleAboutPoint251 = NXOpen.Point3d(46.192077459064699, -39.801869114925346, 0.0)
    viewCenter251 = NXOpen.Point3d(-46.192077459064578, 39.801869114925282, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint251, viewCenter251)
    
    scaleAboutPoint252 = NXOpen.Point3d(36.95366196725179, -31.549371481922446, 0.0)
    viewCenter252 = NXOpen.Point3d(-36.953661967251662, 31.549371481922421, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint252, viewCenter252)
    
    scaleAboutPoint253 = NXOpen.Point3d(30.497725765858387, -25.005798137523726, 0.0)
    viewCenter253 = NXOpen.Point3d(-30.497725765858267, 25.005798137523687, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint253, viewCenter253)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId156, "Curve")
    
    markId157 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId158 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId158, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix5 = theSession.ActiveSketch.Orientation
    
    center6 = NXOpen.Point3d(-16.577340247661763, 0.0, -80.0)
    arc5 = workPart.Curves.CreateArc(center6, nXMatrix5, 8.4226597523382445, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_20 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_20.Geometry = arc5
    geom1_20.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_20.SplineDefiningPointIndex = 0
    geom1Help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help1.Point.X = -25.000000000000007
    geom1Help1.Point.Y = 0.0
    geom1Help1.Point.Z = -80.0
    geom1Help1.Parameter = 0.0
    geom2_20 = NXOpen.Sketch.ConstraintGeometry()
    
    edge5 = extrude1.FindObject("EDGE * 130 * 170 {(-25,25,80)(-25,0,80)(-25,-25,80) EXTRUDE(2)}")
    geom2_20.Geometry = edge5
    geom2_20.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_20.SplineDefiningPointIndex = 0
    geom2Help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help1.Point.X = -25.000000000000007
    geom2Help1.Point.Y = 0.0
    geom2Help1.Point.Z = -80.0
    geom2Help1.Parameter = 0.0
    sketchTangentConstraint1 = theSession.ActiveSketch.CreateTangentConstraint(geom1_20, geom1Help1, geom2_20, geom2Help1)
    
    geom1_21 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_21.Geometry = arc5
    geom1_21.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_21.SplineDefiningPointIndex = 0
    geom1Help2 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help2.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help2.Point.X = -25.000000000000007
    geom1Help2.Point.Y = 0.0
    geom1Help2.Point.Z = -80.0
    geom1Help2.Parameter = 0.0
    geom2_21 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_21.Geometry = edge1
    geom2_21.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_21.SplineDefiningPointIndex = 0
    geom2Help2 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help2.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help2.Point.X = -25.000000000000007
    geom2Help2.Point.Y = 0.0
    geom2Help2.Point.Z = -80.0
    geom2Help2.Parameter = 0.0
    sketchTangentConstraint2 = theSession.ActiveSketch.CreateTangentConstraint(geom1_21, geom1Help2, geom2_21, geom2Help2)
    
    geom1_22 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_22.Geometry = arc5
    geom1_22.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_22.SplineDefiningPointIndex = 0
    geom1Help3 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help3.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help3.Point.X = -25.000000000000007
    geom1Help3.Point.Y = 0.0
    geom1Help3.Point.Z = -80.0
    geom1Help3.Parameter = 0.0
    geom2_22 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_22.Geometry = line4
    geom2_22.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_22.SplineDefiningPointIndex = 0
    geom2Help3 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help3.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help3.Point.X = -25.000000000000007
    geom2Help3.Point.Y = 0.0
    geom2Help3.Point.Z = -80.0
    geom2Help3.Parameter = 0.0
    sketchTangentConstraint3 = theSession.ActiveSketch.CreateTangentConstraint(geom1_22, geom1Help3, geom2_22, geom2Help3)
    
    conGeom1_21 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_21.Geometry = arc5
    conGeom1_21.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_21.SplineDefiningPointIndex = 0
    conGeom2_21 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_21.Geometry = edge1
    conGeom2_21.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    conGeom2_21.SplineDefiningPointIndex = 0
    help5 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help5.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help5.Point.X = -25.000000000000007
    help5.Point.Y = 0.0
    help5.Point.Z = -80.0
    help5.Parameter = 0.0
    sketchHelpedGeometricConstraint5 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_21, conGeom2_21, help5)
    
    dimObject1_13 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_13.Geometry = arc5
    dimObject1_13.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_13.AssocValue = 0
    dimObject1_13.HelpPoint.X = 0.0
    dimObject1_13.HelpPoint.Y = 0.0
    dimObject1_13.HelpPoint.Z = 0.0
    dimObject1_13.View = NXOpen.NXObject.Null
    dimOrigin13 = NXOpen.Point3d(-16.577340247661763, -2.11985278198744, -80.0)
    sketchDimensionalConstraint13 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_13, dimOrigin13, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension13 = sketchDimensionalConstraint13.AssociatedDimension
    
    expression83 = sketchDimensionalConstraint13.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId159 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder15 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines81 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBefore(lines81)
    
    lines82 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAfter(lines82)
    
    lines83 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAbove(lines83)
    
    lines84 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBelow(lines84)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder15.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines85 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBefore(lines85)
    
    lines86 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAfter(lines86)
    
    lines87 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAbove(lines87)
    
    lines88 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBelow(lines88)
    
    theSession.SetUndoMarkName(markId159, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder15.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits359 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits360 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits361 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits362 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits363 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits364 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits365 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits366 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits367 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits368 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder15.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder15.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits369 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits370 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits371 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits372 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits373 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits374 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits375 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits376 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits377 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits378 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    point1_21 = NXOpen.Point3d(-12.651287329997647, -7.4516646322388675, -80.0)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc5, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    point1_22 = NXOpen.Point3d(-12.651287329997647, -7.4516646322388675, -80.0)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc5, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    dimensionlinearunits379 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits380 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits381 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits382 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits383 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits384 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin9 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin9.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin9.View = NXOpen.View.Null
    assocOrigin9.ViewOfGeometry = workPart.ModelingViews.WorkView
    point34 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin9.PointOnGeometry = point34
    assocOrigin9.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.DimensionLine = 0
    assocOrigin9.AssociatedView = NXOpen.View.Null
    assocOrigin9.AssociatedPoint = NXOpen.Point.Null
    assocOrigin9.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.XOffsetFactor = 0.0
    assocOrigin9.YOffsetFactor = 0.0
    assocOrigin9.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder15.Origin.SetAssociativeOrigin(assocOrigin9)
    
    point35 = NXOpen.Point3d(-5.9206636582123924, -13.585262123554429, -80.0)
    sketchRapidDimensionBuilder15.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point35)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder15.Style.DimensionStyle.TextCentered = False
    
    markId160 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject19 = sketchRapidDimensionBuilder15.Commit()
    
    theSession.DeleteUndoMark(markId160, None)
    
    theSession.SetUndoMarkName(markId159, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId159, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder15.Destroy()
    
    markId161 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder16 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines89 = []
    sketchRapidDimensionBuilder16.AppendedText.SetBefore(lines89)
    
    lines90 = []
    sketchRapidDimensionBuilder16.AppendedText.SetAfter(lines90)
    
    lines91 = []
    sketchRapidDimensionBuilder16.AppendedText.SetAbove(lines91)
    
    lines92 = []
    sketchRapidDimensionBuilder16.AppendedText.SetBelow(lines92)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder16.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId161, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder16.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits385 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits386 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits387 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits388 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits389 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits390 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits391 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits392 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits393 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits394 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder16.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits395 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits396 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits397 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits398 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits399 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits400 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits401 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits402 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits403 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits404 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    expression84 = workPart.Expressions.FindObject("p11")
    expression84.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId161, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId162 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId162, None)
    
    markId163 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId161, "Edit Driving Value")
    
    sketchRapidDimensionBuilder16.Destroy()
    
    theSession.UndoToMark(markId163, None)
    
    theSession.DeleteUndoMark(markId163, None)
    
    sketchRapidDimensionBuilder16.Destroy()
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId164 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId153, None)
    
    section7.DistanceTolerance = 0.01
    
    section7.ChainingTolerance = 0.0094999999999999998
    
    markId165 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves4 = [NXOpen.ICurve.Null] * 1 
    curves4[0] = arc5
    seedPoint4 = NXOpen.Point3d(-15.000000000000009, 2.8912057932946783e-16, -80.0)
    regionBoundaryRule4 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch7, curves4, seedPoint4, 0.01)
    
    section7.AllowSelfIntersection(True)
    
    rules8 = [None] * 1 
    rules8[0] = regionBoundaryRule4
    helpPoint5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section7.AddToSection(rules8, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint5, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId165, None)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs6 = section7.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression85)
    
    expression86 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction13 = workPart.Directions.CreateDirection(sketch7, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder9.Direction = direction13
    
    targetBodies42 = [NXOpen.Body.Null] * 1 
    targetBodies42[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies42)
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies43 = [NXOpen.Body.Null] * 1 
    targetBodies43[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies43)
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies44 = [NXOpen.Body.Null] * 1 
    targetBodies44[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies44)
    
    direction14 = extrudeBuilder9.Direction
    
    success3 = direction14.ReverseDirection()
    
    extrudeBuilder9.Direction = direction14
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies45 = [NXOpen.Body.Null] * 1 
    targetBodies45[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies45)
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies46 = [NXOpen.Body.Null] * 1 
    targetBodies46[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies46)
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies47 = [NXOpen.Body.Null] * 1 
    targetBodies47[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies47)
    
    extrudeBuilder9.Limits.EndExtend.Value.SetFormula("20")
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies48 = [NXOpen.Body.Null] * 1 
    targetBodies48[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies48)
    
    extrudeBuilder9.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies49 = [NXOpen.Body.Null] * 1 
    targetBodies49[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies49)
    
    markId166 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId166, None)
    
    markId167 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder9.ParentFeatureInternal = True
    
    try:
        # The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
        feature11 = extrudeBuilder9.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670028)
        
    theSession.UndoToMarkWithStatus(markId167, None)
    
    theSession.DeleteUndoMark(markId167, None)
    
    markId168 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId168, None)
    
    markId169 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder9.ParentFeatureInternal = True
    
    try:
        # The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
        feature12 = extrudeBuilder9.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670028)
        
    theSession.UndoToMarkWithStatus(markId169, None)
    
    theSession.DeleteUndoMark(markId169, None)
    
    markId170 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId170, None)
    
    markId171 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder9.ParentFeatureInternal = True
    
    try:
        # The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
        feature13 = extrudeBuilder9.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670028)
        
    theSession.UndoToMarkWithStatus(markId171, None)
    
    theSession.DeleteUndoMark(markId171, None)
    
    success4 = direction14.ReverseDirection()
    
    extrudeBuilder9.Direction = direction14
    
    extrudeBuilder9.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies50 = [NXOpen.Body.Null] * 1 
    targetBodies50[0] = body1
    extrudeBuilder9.BooleanOperation.SetTargetBodies(targetBodies50)
    
    extrudeBuilder9.Destroy()
    
    section7.Destroy()
    
    workPart.Expressions.Delete(expression82)
    
    workPart.Expressions.Delete(expression86)
    
    theSession.UndoToMark(markId152, None)
    
    theSession.DeleteUndoMark(markId152, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId172 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder10 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section8 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder10.Section = section8
    
    extrudeBuilder10.AllowSelfIntersectingSection(True)
    
    expression87 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder10.DistanceTolerance = 0.01
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies51 = [NXOpen.Body.Null] * 1 
    targetBodies51[0] = NXOpen.Body.Null
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies51)
    
    extrudeBuilder10.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder10.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies52 = [NXOpen.Body.Null] * 1 
    targetBodies52[0] = NXOpen.Body.Null
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies52)
    
    extrudeBuilder10.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder10.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder10.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder10.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder8 = extrudeBuilder10.SmartVolumeProfile
    
    smartVolumeProfileBuilder8.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder8.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId172, "Extrude Dialog")
    
    section8.DistanceTolerance = 0.01
    
    section8.ChainingTolerance = 0.0094999999999999998
    
    section8.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar6 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point36 = workPart.Points.CreatePoint(edge2, scalar6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction15 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform6 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction15, point36, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem7 = workPart.CoordinateSystems.CreateCoordinateSystem(xform6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder6 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder6.Csys = cartesianCoordinateSystem7
    
    datumCsysBuilder6.DisplayScaleFactor = 1.25
    
    feature14 = datumCsysBuilder6.CommitFeature()
    
    datumCsysBuilder6.Destroy()
    
    markId173 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder10 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder10.Csystem = cartesianCoordinateSystem7
    
    sketchInPlaceBuilder10.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject20 = sketchInPlaceBuilder10.Commit()
    
    sketchInPlaceBuilder10.Destroy()
    
    sketch8 = nXObject20
    sketch8.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId174 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId174, None, True)
    
    markId175 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId176 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId176, "Curve")
    
    markId177 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId178 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId178, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix6 = theSession.ActiveSketch.Orientation
    
    center7 = NXOpen.Point3d(-14.337480934350282, 0.0, -80.0)
    arc6 = workPart.Curves.CreateArc(center7, nXMatrix6, 10.662519065649725, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_23 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_23.Geometry = arc6
    geom1_23.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_23.SplineDefiningPointIndex = 0
    geom1Help4 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help4.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help4.Point.X = -25.000000000000007
    geom1Help4.Point.Y = 0.0
    geom1Help4.Point.Z = -80.0
    geom1Help4.Parameter = 0.0
    geom2_23 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_23.Geometry = edge5
    geom2_23.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_23.SplineDefiningPointIndex = 0
    geom2Help4 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help4.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help4.Point.X = -25.000000000000007
    geom2Help4.Point.Y = 0.0
    geom2Help4.Point.Z = -80.0
    geom2Help4.Parameter = 0.0
    sketchTangentConstraint4 = theSession.ActiveSketch.CreateTangentConstraint(geom1_23, geom1Help4, geom2_23, geom2Help4)
    
    geom1_24 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_24.Geometry = arc6
    geom1_24.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_24.SplineDefiningPointIndex = 0
    geom1Help5 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help5.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help5.Point.X = -25.000000000000007
    geom1Help5.Point.Y = 0.0
    geom1Help5.Point.Z = -80.0
    geom1Help5.Parameter = 0.0
    geom2_24 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_24.Geometry = edge1
    geom2_24.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_24.SplineDefiningPointIndex = 0
    geom2Help5 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help5.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help5.Point.X = -25.000000000000007
    geom2Help5.Point.Y = 0.0
    geom2Help5.Point.Z = -80.0
    geom2Help5.Parameter = 0.0
    sketchTangentConstraint5 = theSession.ActiveSketch.CreateTangentConstraint(geom1_24, geom1Help5, geom2_24, geom2Help5)
    
    geom1_25 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_25.Geometry = arc6
    geom1_25.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_25.SplineDefiningPointIndex = 0
    geom1Help6 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help6.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help6.Point.X = -25.000000000000007
    geom1Help6.Point.Y = 0.0
    geom1Help6.Point.Z = -80.0
    geom1Help6.Parameter = 0.0
    geom2_25 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_25.Geometry = line4
    geom2_25.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_25.SplineDefiningPointIndex = 0
    geom2Help6 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help6.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help6.Point.X = -25.000000000000007
    geom2Help6.Point.Y = 0.0
    geom2Help6.Point.Z = -80.0
    geom2Help6.Parameter = 0.0
    sketchTangentConstraint6 = theSession.ActiveSketch.CreateTangentConstraint(geom1_25, geom1Help6, geom2_25, geom2Help6)
    
    conGeom1_22 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_22.Geometry = arc6
    conGeom1_22.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_22.SplineDefiningPointIndex = 0
    conGeom2_22 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_22.Geometry = edge1
    conGeom2_22.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    conGeom2_22.SplineDefiningPointIndex = 0
    help6 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help6.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help6.Point.X = -25.000000000000007
    help6.Point.Y = 0.0
    help6.Point.Z = -80.0
    help6.Parameter = 0.0
    sketchHelpedGeometricConstraint6 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_22, conGeom2_22, help6)
    
    dimObject1_14 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_14.Geometry = arc6
    dimObject1_14.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_14.AssocValue = 0
    dimObject1_14.HelpPoint.X = 0.0
    dimObject1_14.HelpPoint.Y = 0.0
    dimObject1_14.HelpPoint.Z = 0.0
    dimObject1_14.View = NXOpen.NXObject.Null
    dimOrigin14 = NXOpen.Point3d(-14.337480934350282, -3.3122699718553732, -80.0)
    sketchDimensionalConstraint14 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_14, dimOrigin14, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension14 = sketchDimensionalConstraint14.AssociatedDimension
    
    expression88 = sketchDimensionalConstraint14.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId179 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder17 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines93 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBefore(lines93)
    
    lines94 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAfter(lines94)
    
    lines95 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAbove(lines95)
    
    lines96 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBelow(lines96)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder17.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines97 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBefore(lines97)
    
    lines98 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAfter(lines98)
    
    lines99 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAbove(lines99)
    
    lines100 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBelow(lines100)
    
    theSession.SetUndoMarkName(markId179, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder17.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits405 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits406 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits407 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits408 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits409 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits410 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits411 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits412 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits413 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits414 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder17.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits415 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits416 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits417 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits418 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits419 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits420 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits421 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits422 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits423 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits424 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    point1_24 = NXOpen.Point3d(-14.337480934350282, 0.0, -80.0)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc6, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    point1_25 = NXOpen.Point3d(-14.337480934350282, 0.0, -80.0)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc6, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    dimensionlinearunits425 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits426 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits427 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits428 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits429 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits430 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin10 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin10.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin10.View = NXOpen.View.Null
    assocOrigin10.ViewOfGeometry = workPart.ModelingViews.WorkView
    point37 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin10.PointOnGeometry = point37
    assocOrigin10.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.DimensionLine = 0
    assocOrigin10.AssociatedView = NXOpen.View.Null
    assocOrigin10.AssociatedPoint = NXOpen.Point.Null
    assocOrigin10.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.XOffsetFactor = 0.0
    assocOrigin10.YOffsetFactor = 0.0
    assocOrigin10.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder17.Origin.SetAssociativeOrigin(assocOrigin10)
    
    point38 = NXOpen.Point3d(14.874900067429742, -39.31406669087221, -80.0)
    sketchRapidDimensionBuilder17.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point38)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.TextCentered = False
    
    markId180 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject21 = sketchRapidDimensionBuilder17.Commit()
    
    theSession.DeleteUndoMark(markId180, None)
    
    theSession.SetUndoMarkName(markId179, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId179, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder17.Destroy()
    
    markId181 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder18 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines101 = []
    sketchRapidDimensionBuilder18.AppendedText.SetBefore(lines101)
    
    lines102 = []
    sketchRapidDimensionBuilder18.AppendedText.SetAfter(lines102)
    
    lines103 = []
    sketchRapidDimensionBuilder18.AppendedText.SetAbove(lines103)
    
    lines104 = []
    sketchRapidDimensionBuilder18.AppendedText.SetBelow(lines104)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder18.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId181, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder18.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits431 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits432 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits433 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits434 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits435 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits436 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits437 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits438 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits439 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits440 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder18.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits441 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits442 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits443 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits444 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits445 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits446 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits447 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits448 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits449 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits450 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    expression89 = workPart.Expressions.FindObject("p11")
    expression89.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId181, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId182 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId182, None)
    
    markId183 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId181, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder18.Destroy()
    
    theSession.UndoToMark(markId183, None)
    
    theSession.DeleteUndoMark(markId183, None)
    
    sketchRapidDimensionBuilder18.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId184 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId173, None)
    
    section8.DistanceTolerance = 0.01
    
    section8.ChainingTolerance = 0.0094999999999999998
    
    markId185 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves5 = [NXOpen.ICurve.Null] * 1 
    curves5[0] = arc6
    seedPoint5 = NXOpen.Point3d(-15.000000000000009, 2.8912057932946783e-16, -80.0)
    regionBoundaryRule5 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch8, curves5, seedPoint5, 0.01)
    
    section8.AllowSelfIntersection(True)
    
    rules9 = [None] * 1 
    rules9[0] = regionBoundaryRule5
    helpPoint6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section8.AddToSection(rules9, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint6, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId185, None)
    
    expression90 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs7 = section8.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression90)
    
    expression91 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction16 = workPart.Directions.CreateDirection(sketch8, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder10.Direction = direction16
    
    targetBodies53 = [NXOpen.Body.Null] * 1 
    targetBodies53[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies53)
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies54 = [NXOpen.Body.Null] * 1 
    targetBodies54[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies54)
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies55 = [NXOpen.Body.Null] * 1 
    targetBodies55[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies55)
    
    targetBodies56 = []
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies56)
    
    direction17 = extrudeBuilder10.Direction
    
    success5 = direction17.ReverseDirection()
    
    extrudeBuilder10.Direction = direction17
    
    targetBodies57 = [NXOpen.Body.Null] * 1 
    targetBodies57[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies57)
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies58 = [NXOpen.Body.Null] * 1 
    targetBodies58[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies58)
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies59 = [NXOpen.Body.Null] * 1 
    targetBodies59[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies59)
    
    extrudeBuilder10.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies60 = [NXOpen.Body.Null] * 1 
    targetBodies60[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies60)
    
    extrudeBuilder10.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies61 = [NXOpen.Body.Null] * 1 
    targetBodies61[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies61)
    
    extrudeBuilder10.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder10.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies62 = [NXOpen.Body.Null] * 1 
    targetBodies62[0] = body1
    extrudeBuilder10.BooleanOperation.SetTargetBodies(targetBodies62)
    
    markId186 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId186, None)
    
    markId187 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder10.ParentFeatureInternal = True
    
    try:
        # The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
        feature15 = extrudeBuilder10.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(670028)
        
    theSession.UndoToMarkWithStatus(markId187, None)
    
    theSession.DeleteUndoMark(markId187, None)
    
    extrudeBuilder10.Destroy()
    
    section8.Destroy()
    
    workPart.Expressions.Delete(expression87)
    
    workPart.Expressions.Delete(expression91)
    
    theSession.UndoToMark(markId172, None)
    
    theSession.DeleteUndoMark(markId172, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId188 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder11 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section9 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder11.Section = section9
    
    extrudeBuilder11.AllowSelfIntersectingSection(True)
    
    expression92 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder11.DistanceTolerance = 0.01
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies63 = [NXOpen.Body.Null] * 1 
    targetBodies63[0] = NXOpen.Body.Null
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies63)
    
    extrudeBuilder11.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder11.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies64 = [NXOpen.Body.Null] * 1 
    targetBodies64[0] = NXOpen.Body.Null
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies64)
    
    extrudeBuilder11.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder11.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder11.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder11.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder9 = extrudeBuilder11.SmartVolumeProfile
    
    smartVolumeProfileBuilder9.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder9.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId188, "Extrude Dialog")
    
    section9.DistanceTolerance = 0.01
    
    section9.ChainingTolerance = 0.0094999999999999998
    
    section9.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar7 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point39 = workPart.Points.CreatePoint(edge2, scalar7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction18 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform7 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction18, point39, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem8 = workPart.CoordinateSystems.CreateCoordinateSystem(xform7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder7 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder7.Csys = cartesianCoordinateSystem8
    
    datumCsysBuilder7.DisplayScaleFactor = 1.25
    
    feature16 = datumCsysBuilder7.CommitFeature()
    
    datumCsysBuilder7.Destroy()
    
    markId189 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder11 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder11.Csystem = cartesianCoordinateSystem8
    
    sketchInPlaceBuilder11.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject22 = sketchInPlaceBuilder11.Commit()
    
    sketchInPlaceBuilder11.Destroy()
    
    sketch9 = nXObject22
    sketch9.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId190 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId190, None, True)
    
    markId191 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId192 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint254 = NXOpen.Point3d(24.100214326468542, -23.369904801424028, 0.0)
    viewCenter254 = NXOpen.Point3d(-24.100214326468492, 23.369904801424003, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint254, viewCenter254)
    
    scaleAboutPoint255 = NXOpen.Point3d(30.125267908085707, -29.212381001780063, 0.0)
    viewCenter255 = NXOpen.Point3d(-30.125267908085579, 29.212381001779999, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint255, viewCenter255)
    
    scaleAboutPoint256 = NXOpen.Point3d(37.656584885107094, -36.515476252225078, 0.0)
    viewCenter256 = NXOpen.Point3d(-37.656584885107016, 36.515476252225, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint256, viewCenter256)
    
    scaleAboutPoint257 = NXOpen.Point3d(30.1252679080857, -29.212381001780056, 0.0)
    viewCenter257 = NXOpen.Point3d(-30.125267908085572, 29.212381001779992, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint257, viewCenter257)
    
    scaleAboutPoint258 = NXOpen.Point3d(24.10021432646856, -23.369904801424045, 0.0)
    viewCenter258 = NXOpen.Point3d(-24.100214326468457, 23.369904801424017, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint258, viewCenter258)
    
    scaleAboutPoint259 = NXOpen.Point3d(19.280171461174845, -18.695923841139233, 0.0)
    viewCenter259 = NXOpen.Point3d(-19.280171461174721, 18.695923841139191, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint259, viewCenter259)
    
    scaleAboutPoint260 = NXOpen.Point3d(15.42413716893989, -14.956739072911384, 0.0)
    viewCenter260 = NXOpen.Point3d(-15.424137168939792, 14.956739072911352, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint260, viewCenter260)
    
    scaleAboutPoint261 = NXOpen.Point3d(12.339309735151941, -11.96539125832911, 0.0)
    viewCenter261 = NXOpen.Point3d(-12.339309735151824, 11.965391258329083, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint261, viewCenter261)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId192, "Curve")
    
    markId193 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId194 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId194, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix7 = theSession.ActiveSketch.Orientation
    
    center8 = NXOpen.Point3d(-25.000000000000007, 0.0, -80.0)
    arc7 = workPart.Curves.CreateArc(center8, nXMatrix7, 8.8619259751572557, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_26 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_26.Geometry = arc7
    geom1_26.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_26.SplineDefiningPointIndex = 0
    geom2_26 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_26.Geometry = edge1
    geom2_26.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom2_26.SplineDefiningPointIndex = 0
    sketchGeometricConstraint41 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_26, geom2_26)
    
    dimObject1_15 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_15.Geometry = arc7
    dimObject1_15.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_15.AssocValue = 0
    dimObject1_15.HelpPoint.X = 0.0
    dimObject1_15.HelpPoint.Y = 0.0
    dimObject1_15.HelpPoint.Z = 0.0
    dimObject1_15.View = NXOpen.NXObject.Null
    dimOrigin15 = NXOpen.Point3d(-25.000000000000007, -1.3567057804719604, -80.0)
    sketchDimensionalConstraint15 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_15, dimOrigin15, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension15 = sketchDimensionalConstraint15.AssociatedDimension
    
    expression93 = sketchDimensionalConstraint15.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId195 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder19 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines105 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBefore(lines105)
    
    lines106 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAfter(lines106)
    
    lines107 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAbove(lines107)
    
    lines108 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBelow(lines108)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder19.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines109 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBefore(lines109)
    
    lines110 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAfter(lines110)
    
    lines111 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAbove(lines111)
    
    lines112 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBelow(lines112)
    
    theSession.SetUndoMarkName(markId195, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder19.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits451 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits452 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits453 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits454 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits455 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits456 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits457 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits458 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits459 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits460 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder19.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits461 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits462 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits463 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits464 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits465 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits466 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits467 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits468 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits469 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits470 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    point1_27 = NXOpen.Point3d(-18.914290311901716, -6.4418840086851521, -80.0)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc7, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    point1_28 = NXOpen.Point3d(-18.914290311901716, -6.4418840086851521, -80.0)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc7, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    point1_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    dimensionlinearunits471 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits472 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits473 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits474 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits475 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits476 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin11 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin11.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin11.View = NXOpen.View.Null
    assocOrigin11.ViewOfGeometry = workPart.ModelingViews.WorkView
    point40 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin11.PointOnGeometry = point40
    assocOrigin11.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.DimensionLine = 0
    assocOrigin11.AssociatedView = NXOpen.View.Null
    assocOrigin11.AssociatedPoint = NXOpen.Point.Null
    assocOrigin11.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.XOffsetFactor = 0.0
    assocOrigin11.YOffsetFactor = 0.0
    assocOrigin11.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder19.Origin.SetAssociativeOrigin(assocOrigin11)
    
    point41 = NXOpen.Point3d(-8.0790204285288993, -10.604138642322715, -80.0)
    sketchRapidDimensionBuilder19.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point41)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.TextCentered = False
    
    markId196 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject23 = sketchRapidDimensionBuilder19.Commit()
    
    theSession.DeleteUndoMark(markId196, None)
    
    theSession.SetUndoMarkName(markId195, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId195, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder19.Destroy()
    
    markId197 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder20 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines113 = []
    sketchRapidDimensionBuilder20.AppendedText.SetBefore(lines113)
    
    lines114 = []
    sketchRapidDimensionBuilder20.AppendedText.SetAfter(lines114)
    
    lines115 = []
    sketchRapidDimensionBuilder20.AppendedText.SetAbove(lines115)
    
    lines116 = []
    sketchRapidDimensionBuilder20.AppendedText.SetBelow(lines116)
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder20.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId197, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder20.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits477 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits478 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits479 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits480 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits481 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits482 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits483 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits484 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits485 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits486 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder20.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder20.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder20.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits487 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits488 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits489 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits490 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits491 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits492 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits493 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits494 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits495 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits496 = sketchRapidDimensionBuilder20.Style.UnitsStyle.DimensionLinearUnits
    
    expression94 = workPart.Expressions.FindObject("p11")
    expression94.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId197, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId198 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId198, None)
    
    markId199 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId197, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder20.Destroy()
    
    theSession.UndoToMark(markId199, None)
    
    theSession.DeleteUndoMark(markId199, None)
    
    sketchRapidDimensionBuilder20.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId200 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId189, None)
    
    section9.DistanceTolerance = 0.01
    
    section9.ChainingTolerance = 0.0094999999999999998
    
    markId201 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves6 = [NXOpen.ICurve.Null] * 1 
    curves6[0] = arc7
    seedPoint6 = NXOpen.Point3d(-22.500000000000011, 2.8912057932946783e-16, -80.0)
    regionBoundaryRule6 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch9, curves6, seedPoint6, 0.01)
    
    section9.AllowSelfIntersection(True)
    
    rules10 = [None] * 1 
    rules10[0] = regionBoundaryRule6
    helpPoint7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section9.AddToSection(rules10, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint7, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId201, None)
    
    expression95 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs8 = section9.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression95)
    
    expression96 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction19 = workPart.Directions.CreateDirection(sketch9, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder11.Direction = direction19
    
    targetBodies65 = [NXOpen.Body.Null] * 1 
    targetBodies65[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies65)
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies66 = [NXOpen.Body.Null] * 1 
    targetBodies66[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies66)
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies67 = [NXOpen.Body.Null] * 1 
    targetBodies67[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies67)
    
    direction20 = extrudeBuilder11.Direction
    
    success6 = direction20.ReverseDirection()
    
    extrudeBuilder11.Direction = direction20
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies68 = [NXOpen.Body.Null] * 1 
    targetBodies68[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies68)
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies69 = [NXOpen.Body.Null] * 1 
    targetBodies69[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies69)
    
    extrudeBuilder11.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies70 = [NXOpen.Body.Null] * 1 
    targetBodies70[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies70)
    
    extrudeBuilder11.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies71 = [NXOpen.Body.Null] * 1 
    targetBodies71[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies71)
    
    extrudeBuilder11.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder11.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies72 = [NXOpen.Body.Null] * 1 
    targetBodies72[0] = body1
    extrudeBuilder11.BooleanOperation.SetTargetBodies(targetBodies72)
    
    markId202 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId202, None)
    
    markId203 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder11.ParentFeatureInternal = True
    
    feature17 = extrudeBuilder11.CommitFeature()
    
    theSession.DeleteUndoMark(markId203, None)
    
    theSession.SetUndoMarkName(markId188, "Extrude")
    
    expression97 = extrudeBuilder11.Limits.StartExtend.Value
    expression98 = extrudeBuilder11.Limits.EndExtend.Value
    extrudeBuilder11.Destroy()
    
    workPart.Expressions.Delete(expression92)
    
    workPart.Expressions.Delete(expression96)
    
    scaleAboutPoint262 = NXOpen.Point3d(-110.71492399674628, 24.830523851512993, 0.0)
    viewCenter262 = NXOpen.Point3d(110.71492399674634, -24.830523851513018, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint262, viewCenter262)
    
    scaleAboutPoint263 = NXOpen.Point3d(-116.11921448207562, 27.021452426646484, 0.0)
    viewCenter263 = NXOpen.Point3d(116.11921448207562, -27.021452426646547, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint263, viewCenter263)
    
    scaleAboutPoint264 = NXOpen.Point3d(-137.84592285214953, 34.689702439613733, 0.0)
    viewCenter264 = NXOpen.Point3d(137.84592285214953, -34.689702439613811, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint264, viewCenter264)
    
    scaleAboutPoint265 = NXOpen.Point3d(-167.17241471721772, 42.79157373307617, 0.0)
    viewCenter265 = NXOpen.Point3d(167.17241471721772, -42.791573733076262, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint265, viewCenter265)
    
    scaleAboutPoint266 = NXOpen.Point3d(-138.30236630530231, 33.776815533308103, 0.0)
    viewCenter266 = NXOpen.Point3d(138.30236630530231, -33.776815533308181, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint266, viewCenter266)
    
    scaleAboutPoint267 = NXOpen.Point3d(-113.19797638189753, 27.386607189168739, 0.0)
    viewCenter267 = NXOpen.Point3d(113.19797638189766, -27.386607189168803, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint267, viewCenter267)
    
    scaleAboutPoint268 = NXOpen.Point3d(-90.850504915535822, 21.909285751334988, 0.0)
    viewCenter268 = NXOpen.Point3d(90.850504915535879, -21.909285751335037, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint268, viewCenter268)
    
    scaleAboutPoint269 = NXOpen.Point3d(-72.914102980442905, 17.527428601067971, 0.0)
    viewCenter269 = NXOpen.Point3d(72.914102980442934, -17.527428601068049, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint269, viewCenter269)
    
    scaleAboutPoint270 = NXOpen.Point3d(-83.383820331480848, 19.630720033196123, 0.0)
    viewCenter270 = NXOpen.Point3d(83.383820331480919, -19.630720033196219, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint270, viewCenter270)
    
    scaleAboutPoint271 = NXOpen.Point3d(-66.70705626518469, 15.704576026556886, 0.0)
    viewCenter271 = NXOpen.Point3d(66.707056265184733, -15.704576026556975, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint271, viewCenter271)
    
    rotMatrix36 = NXOpen.Matrix3x3()
    
    rotMatrix36.Xx = 0.87955542971987233
    rotMatrix36.Xy = -0.010885294649397996
    rotMatrix36.Xz = -0.47567189995907966
    rotMatrix36.Yx = -0.042419139772016334
    rotMatrix36.Yy = -0.9975511636238249
    rotMatrix36.Yz = -0.055608385462549037
    rotMatrix36.Zx = -0.47390174364659898
    rotMatrix36.Zy = 0.069088250181527089
    rotMatrix36.Zz = -0.87786328722390405
    translation36 = NXOpen.Point3d(-51.109628831841626, 29.980034445387972, -104.71703417875014)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix36, translation36, 2.2112384594958998)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId204 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder2 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression99 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression100 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData2 = edgeBlendBuilder2.LimitsListData
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder2 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression101 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression102 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId204, "Edge Blend Dialog")
    
    scCollector2 = workPart.ScCollectors.CreateCollector()
    
    seedEdges3 = [NXOpen.Edge.Null] * 1 
    extrude5 = feature17
    edge6 = extrude5.FindObject("EDGE * 130 * 140 {(-25,-7.5,-65)(-17.5,-0,-65)(-25,7.5,-65) EXTRUDE(2)}")
    seedEdges3[0] = edge6
    edgeMultipleSeedTangentRule3 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges3, 0.5, True)
    
    rules11 = [None] * 1 
    rules11[0] = edgeMultipleSeedTangentRule3
    scCollector2.ReplaceRules(rules11, False)
    
    scCollector2.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    rotMatrix37 = NXOpen.Matrix3x3()
    
    rotMatrix37.Xx = 0.87955542971987466
    rotMatrix37.Xy = -0.010885294649398124
    rotMatrix37.Xz = -0.47567189995908182
    rotMatrix37.Yx = 0.44302572496772535
    rotMatrix37.Yy = -0.34586940604577693
    rotMatrix37.Yz = 0.82710492742962294
    rotMatrix37.Zx = -0.17352363835255441
    rotMatrix37.Zy = -0.93821951819493521
    rotMatrix37.Zz = -0.29938884850801445
    translation37 = NXOpen.Point3d(-51.109628831841626, 29.980034445387972, -104.71703417875014)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix37, translation37, 2.2112384594958998)
    
    scaleAboutPoint272 = NXOpen.Point3d(-35.896173774987261, 23.571820778908275, 0.0)
    viewCenter272 = NXOpen.Point3d(35.896173774987325, -23.571820778908357, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint272, viewCenter272)
    
    scaleAboutPoint273 = NXOpen.Point3d(-48.914519464049313, 13.688407599528446, 0.0)
    viewCenter273 = NXOpen.Point3d(48.914519464049377, -13.688407599528528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint273, viewCenter273)
    
    scaleAboutPoint274 = NXOpen.Point3d(-61.023495417478358, 17.110509499410565, 0.0)
    viewCenter274 = NXOpen.Point3d(61.023495417478422, -17.110509499410647, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint274, viewCenter274)
    
    scaleAboutPoint275 = NXOpen.Point3d(-75.830667099660602, 21.986406437179657, 0.0)
    viewCenter275 = NXOpen.Point3d(75.830667099660658, -21.98640643717976, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint275, viewCenter275)
    
    scaleAboutPoint276 = NXOpen.Point3d(-97.592722450746621, 30.100437384234077, 0.0)
    viewCenter276 = NXOpen.Point3d(97.592722450746692, -30.100437384234187, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint276, viewCenter276)
    
    rotMatrix38 = NXOpen.Matrix3x3()
    
    rotMatrix38.Xx = 0.77864238290662202
    rotMatrix38.Xy = -0.18769378693283012
    rotMatrix38.Xz = -0.59873790750904443
    rotMatrix38.Yx = 0.29922023757440352
    rotMatrix38.Yy = -0.72765860096858692
    rotMatrix38.Yz = 0.61723594343034882
    rotMatrix38.Zx = -0.55152813977839177
    rotMatrix38.Zy = -0.65976056473788169
    rotMatrix38.Zz = -0.51042404748339887
    translation38 = NXOpen.Point3d(-76.518321672431426, 20.757366629686089, -99.756873374829965)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix38, translation38, 1.76899076759672)
    
    markId205 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    csIndex1 = edgeBlendBuilder2.AddChainset(scCollector2, "7.5")
    
    feature18 = edgeBlendBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId205, None)
    
    theSession.SetUndoMarkName(markId204, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder2)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression102)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression101)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression99)
    
    workPart.Expressions.Delete(expression100)
    
    markId206 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder3 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression103 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression104 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData3 = edgeBlendBuilder3.LimitsListData
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder3 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression105 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression106 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId206, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    rotMatrix39 = NXOpen.Matrix3x3()
    
    rotMatrix39.Xx = 0.8292588929773812
    rotMatrix39.Xy = -0.30265855921570495
    rotMatrix39.Xz = -0.46981643750660751
    rotMatrix39.Yx = 0.068070807595846675
    rotMatrix39.Yy = -0.77970265862443833
    rotMatrix39.Yz = 0.62243885586234382
    rotMatrix39.Zx = -0.55470357270453374
    rotMatrix39.Zy = -0.5481437408813935
    rotMatrix39.Zz = -0.62597315099081396
    translation39 = NXOpen.Point3d(-76.518321672431426, 20.757366629686089, -99.756873374829965)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix39, translation39, 1.76899076759672)
    
    scaleAboutPoint277 = NXOpen.Point3d(-71.493212768516315, -10.469717351038012, 0.0)
    viewCenter277 = NXOpen.Point3d(71.493212768516358, 10.469717351037922, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint277, viewCenter277)
    
    scaleAboutPoint278 = NXOpen.Point3d(-55.160453700897115, -9.093697356330166, 0.0)
    viewCenter278 = NXOpen.Point3d(55.160453700897172, 9.0936973563300736, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint278, viewCenter278)
    
    scaleAboutPoint279 = NXOpen.Point3d(-44.128362960717674, -7.3706810151307769, 0.0)
    viewCenter279 = NXOpen.Point3d(44.128362960717745, 7.3706810151306872, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint279, viewCenter279)
    
    scaleAboutPoint280 = NXOpen.Point3d(-35.302690368574133, -5.8965448121046276, 0.0)
    viewCenter280 = NXOpen.Point3d(35.302690368574197, 5.8965448121045299, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint280, viewCenter280)
    
    scaleAboutPoint281 = NXOpen.Point3d(-44.128362960717659, -7.3706810151307769, 0.0)
    viewCenter281 = NXOpen.Point3d(44.128362960717745, 7.3706810151306792, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint281, viewCenter281)
    
    scaleAboutPoint282 = NXOpen.Point3d(-55.160453700897094, -9.2133512689134509, 0.0)
    viewCenter282 = NXOpen.Point3d(55.160453700897172, 9.2133512689133781, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint282, viewCenter282)
    
    scaleAboutPoint283 = NXOpen.Point3d(-68.950567126121371, -11.516689086141799, 0.0)
    viewCenter283 = NXOpen.Point3d(68.950567126121442, 11.516689086141723, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint283, viewCenter283)
    
    scaleAboutPoint284 = NXOpen.Point3d(-86.188208907651699, -14.395861357677248, 0.0)
    viewCenter284 = NXOpen.Point3d(86.188208907651799, 14.395861357677152, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint284, viewCenter284)
    
    scaleAboutPoint285 = NXOpen.Point3d(-107.73526113456464, -17.99482669709656, 0.0)
    viewCenter285 = NXOpen.Point3d(107.73526113456475, 17.99482669709646, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint285, viewCenter285)
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder3)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression106)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression105)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression103)
    
    workPart.Expressions.Delete(expression104)
    
    theSession.UndoToMark(markId206, None)
    
    theSession.DeleteUndoMark(markId206, None)
    
    markId207 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects10 = [NXOpen.DisplayableObject.Null] * 5 
    objects10[0] = sketch2
    objects10[1] = line1
    objects10[2] = line2
    objects10[3] = line3
    objects10[4] = line4
    theSession.DisplayManager.BlankObjects(objects10)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    rotMatrix40 = NXOpen.Matrix3x3()
    
    rotMatrix40.Xx = 0.96553617531888514
    rotMatrix40.Xy = -0.18817616364935089
    rotMatrix40.Xz = -0.1798044092473538
    rotMatrix40.Yx = -0.16824210121329103
    rotMatrix40.Yy = -0.97835746989054329
    rotMatrix40.Yz = 0.12046267674557949
    rotMatrix40.Zx = -0.19858119127931972
    rotMatrix40.Zy = -0.086060400554412442
    rotMatrix40.Zz = -0.97629868274339915
    translation40 = NXOpen.Point3d(-141.72830183603685, 9.5471972149198301, -99.756873374829965)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix40, translation40, 0.90572327300952049)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId208 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder12 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder12.PlaneReference = plane8
    
    expression107 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression108 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    sketchAlongPathBuilder4 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder4.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId208, "Create Sketch Dialog")
    
    scalar8 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge7 = extrude1.FindObject("EDGE * 120 * 150 {(25,-25,-80)(25,0,-80)(25,25,-80) EXTRUDE(2)}")
    point42 = workPart.Points.CreatePoint(edge7, scalar8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction21 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform8 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction21, point42, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem9 = workPart.CoordinateSystems.CreateCoordinateSystem(xform8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder12.Csystem = cartesianCoordinateSystem9
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane9.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom6 = [NXOpen.NXObject.Null] * 1 
    geom6[0] = face1
    plane9.SetGeometry(geom6)
    
    plane9.SetFlip(False)
    
    plane9.SetExpression(None)
    
    plane9.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane9.Evaluate()
    
    origin10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal10 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane10 = workPart.Planes.CreatePlane(origin10, normal10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression109 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression110 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    plane10.SynchronizeToPlane(plane9)
    
    scalar9 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point43 = workPart.Points.CreatePoint(edge7, scalar9, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane10.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom7 = [NXOpen.NXObject.Null] * 1 
    geom7[0] = face1
    plane10.SetGeometry(geom7)
    
    plane10.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane10.Evaluate()
    
    markId209 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId209, None)
    
    markId210 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
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
    
    nXObject24 = sketchInPlaceBuilder12.Commit()
    
    sketch10 = nXObject24
    feature19 = sketch10.Feature
    
    markId211 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs10 = theSession.UpdateManager.DoUpdate(markId211)
    
    sketch10.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId210, None)
    
    theSession.SetUndoMarkName(markId208, "Create Sketch")
    
    sketchInPlaceBuilder12.Destroy()
    
    sketchAlongPathBuilder4.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression108)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point43)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression107)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane8.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression110)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression109)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane10.DestroyPlane()
    
    scaleAboutPoint286 = NXOpen.Point3d(20.156542891228259, -26.291142901602065, 0.0)
    viewCenter286 = NXOpen.Point3d(-20.15654289122816, 26.29114290160199, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint286, viewCenter286)
    
    scaleAboutPoint287 = NXOpen.Point3d(25.195678614035327, -32.863928627002551, 0.0)
    viewCenter287 = NXOpen.Point3d(-25.195678614035202, 32.863928627002487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint287, viewCenter287)
    
    scaleAboutPoint288 = NXOpen.Point3d(31.49459826754412, -41.079910783753185, 0.0)
    viewCenter288 = NXOpen.Point3d(-31.494598267544042, 41.079910783753107, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint288, viewCenter288)
    
    scaleAboutPoint289 = NXOpen.Point3d(25.195678614035327, -32.863928627002551, 0.0)
    viewCenter289 = NXOpen.Point3d(-25.195678614035202, 32.863928627002487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint289, viewCenter289)
    
    scaleAboutPoint290 = NXOpen.Point3d(20.156542891228259, -26.29114290160204, 0.0)
    viewCenter290 = NXOpen.Point3d(-20.15654289122816, 26.291142901602015, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint290, viewCenter290)
    
    scaleAboutPoint291 = NXOpen.Point3d(16.592632409011081, -20.565516225253138, 0.0)
    viewCenter291 = NXOpen.Point3d(-16.592632409010982, 20.56551622525312, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint291, viewCenter291)
    
    scaleAboutPoint292 = NXOpen.Point3d(12.526268973563324, -15.51761678814557, 0.0)
    viewCenter292 = NXOpen.Point3d(-12.526268973563196, 15.517616788145538, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint292, viewCenter292)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId212 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId213 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId213, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix8 = theSession.ActiveSketch.Orientation
    
    center9 = NXOpen.Point3d(25.000000000000007, 0.0, -80.0)
    arc8 = workPart.Curves.CreateArc(center9, nXMatrix8, 8.6148611630111471, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_27 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_27.Geometry = arc8
    geom1_27.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_27.SplineDefiningPointIndex = 0
    geom2_27 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_27.Geometry = edge7
    geom2_27.PointType = NXOpen.Sketch.ConstraintPointType.MidVertex
    geom2_27.SplineDefiningPointIndex = 0
    sketchGeometricConstraint42 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_27, geom2_27)
    
    dimObject1_16 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_16.Geometry = arc8
    dimObject1_16.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_16.AssocValue = 0
    dimObject1_16.HelpPoint.X = 0.0
    dimObject1_16.HelpPoint.Y = 0.0
    dimObject1_16.HelpPoint.Z = 0.0
    dimObject1_16.View = NXOpen.NXObject.Null
    dimOrigin16 = NXOpen.Point3d(25.000000000000007, -1.6958822255899504, -80.0)
    sketchDimensionalConstraint16 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_16, dimOrigin16, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension16 = sketchDimensionalConstraint16.AssociatedDimension
    
    expression111 = sketchDimensionalConstraint16.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId214 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder21 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines117 = []
    sketchRapidDimensionBuilder21.AppendedText.SetBefore(lines117)
    
    lines118 = []
    sketchRapidDimensionBuilder21.AppendedText.SetAfter(lines118)
    
    lines119 = []
    sketchRapidDimensionBuilder21.AppendedText.SetAbove(lines119)
    
    lines120 = []
    sketchRapidDimensionBuilder21.AppendedText.SetBelow(lines120)
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder21.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines121 = []
    sketchRapidDimensionBuilder21.AppendedText.SetBefore(lines121)
    
    lines122 = []
    sketchRapidDimensionBuilder21.AppendedText.SetAfter(lines122)
    
    lines123 = []
    sketchRapidDimensionBuilder21.AppendedText.SetAbove(lines123)
    
    lines124 = []
    sketchRapidDimensionBuilder21.AppendedText.SetBelow(lines124)
    
    theSession.SetUndoMarkName(markId214, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder21.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits497 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits498 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits499 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits500 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits501 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits502 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits503 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits504 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits505 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits506 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder21.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder21.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits507 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits508 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits509 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits510 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits511 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits512 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits513 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits514 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits515 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits516 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    point1_30 = NXOpen.Point3d(33.578125243155959, -0.79473276683953531, -80.0)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc8, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(33.578125243155959, -0.79473276683953531, -80.0)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc8, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    point1_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder21.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    dimensionlinearunits517 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits518 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits519 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits520 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits521 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits522 = sketchRapidDimensionBuilder21.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin12 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin12.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin12.View = NXOpen.View.Null
    assocOrigin12.ViewOfGeometry = workPart.ModelingViews.WorkView
    point44 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin12.PointOnGeometry = point44
    assocOrigin12.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.DimensionLine = 0
    assocOrigin12.AssociatedView = NXOpen.View.Null
    assocOrigin12.AssociatedPoint = NXOpen.Point.Null
    assocOrigin12.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.XOffsetFactor = 0.0
    assocOrigin12.YOffsetFactor = 0.0
    assocOrigin12.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder21.Origin.SetAssociativeOrigin(assocOrigin12)
    
    point45 = NXOpen.Point3d(43.230862735590868, -3.9998035454403489, -80.0)
    sketchRapidDimensionBuilder21.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point45)
    
    sketchRapidDimensionBuilder21.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder21.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder21.Style.DimensionStyle.TextCentered = False
    
    markId215 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject25 = sketchRapidDimensionBuilder21.Commit()
    
    theSession.DeleteUndoMark(markId215, None)
    
    theSession.SetUndoMarkName(markId214, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId214, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder21.Destroy()
    
    markId216 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder22 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines125 = []
    sketchRapidDimensionBuilder22.AppendedText.SetBefore(lines125)
    
    lines126 = []
    sketchRapidDimensionBuilder22.AppendedText.SetAfter(lines126)
    
    lines127 = []
    sketchRapidDimensionBuilder22.AppendedText.SetAbove(lines127)
    
    lines128 = []
    sketchRapidDimensionBuilder22.AppendedText.SetBelow(lines128)
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder22.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId216, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder22.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits523 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits524 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits525 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits526 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits527 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits528 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits529 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits530 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits531 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits532 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder22.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder22.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder22.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits533 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits534 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits535 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits536 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits537 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits538 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits539 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits540 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits541 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits542 = sketchRapidDimensionBuilder22.Style.UnitsStyle.DimensionLinearUnits
    
    expression112 = workPart.Expressions.FindObject("p20")
    expression112.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId216, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId217 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId217, None)
    
    markId218 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId216, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder22.Destroy()
    
    theSession.UndoToMark(markId218, None)
    
    theSession.DeleteUndoMark(markId218, None)
    
    sketchRapidDimensionBuilder22.Destroy()
    
    sketch11 = theSession.ActiveSketch
    
    markId219 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId220 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder12 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section10 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder12.Section = section10
    
    extrudeBuilder12.AllowSelfIntersectingSection(True)
    
    expression113 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder12.DistanceTolerance = 0.01
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies73 = [NXOpen.Body.Null] * 1 
    targetBodies73[0] = NXOpen.Body.Null
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies73)
    
    extrudeBuilder12.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder12.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies74 = [NXOpen.Body.Null] * 1 
    targetBodies74[0] = NXOpen.Body.Null
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies74)
    
    extrudeBuilder12.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder12.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder12.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder12.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder10 = extrudeBuilder12.SmartVolumeProfile
    
    smartVolumeProfileBuilder10.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder10.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId220, "Extrude Dialog")
    
    section10.DistanceTolerance = 0.01
    
    section10.ChainingTolerance = 0.0094999999999999998
    
    section10.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId221 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId222 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature4 = feature19
    features2[0] = sketchFeature4
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section10.AllowSelfIntersection(True)
    
    rules12 = [None] * 1 
    rules12[0] = curveFeatureRule2
    helpPoint8 = NXOpen.Point3d(30.083062902486152, -5.4969550068044057, -80.0)
    section10.AddToSection(rules12, arc8, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint8, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId222, None)
    
    direction22 = workPart.Directions.CreateDirection(sketch11, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder12.Direction = direction22
    
    targetBodies75 = [NXOpen.Body.Null] * 1 
    targetBodies75[0] = body1
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies75)
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies76 = [NXOpen.Body.Null] * 1 
    targetBodies76[0] = body1
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies76)
    
    expression114 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.DeleteUndoMark(markId221, None)
    
    rotMatrix41 = NXOpen.Matrix3x3()
    
    rotMatrix41.Xx = 0.92600497527535641
    rotMatrix41.Xy = 0.034900601555360657
    rotMatrix41.Xz = 0.37589457800872406
    rotMatrix41.Yx = -0.21226465981437181
    rotMatrix41.Yy = -0.77527440174683382
    rotMatrix41.Yz = 0.59488933104399777
    rotMatrix41.Zx = 0.31218343959789474
    rotMatrix41.Zy = -0.63065961501206047
    rotMatrix41.Zz = -0.71049978890472831
    translation41 = NXOpen.Point3d(-133.9013118995932, 16.351316459041524, -102.29550501524936)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix41, translation41, 0.90572327300952049)
    
    direction23 = extrudeBuilder12.Direction
    
    success7 = direction23.ReverseDirection()
    
    extrudeBuilder12.Direction = direction23
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies77 = [NXOpen.Body.Null] * 1 
    targetBodies77[0] = body1
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies77)
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies78 = [NXOpen.Body.Null] * 1 
    targetBodies78[0] = body1
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies78)
    
    extrudeBuilder12.Limits.EndExtend.Value.SetFormula("18")
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies79 = [NXOpen.Body.Null] * 1 
    targetBodies79[0] = body1
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies79)
    
    extrudeBuilder12.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder12.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies80 = [NXOpen.Body.Null] * 1 
    targetBodies80[0] = body1
    extrudeBuilder12.BooleanOperation.SetTargetBodies(targetBodies80)
    
    markId223 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder12.ParentFeatureInternal = False
    
    feature20 = extrudeBuilder12.CommitFeature()
    
    theSession.DeleteUndoMark(markId223, None)
    
    theSession.SetUndoMarkName(markId220, "Extrude")
    
    expression115 = extrudeBuilder12.Limits.StartExtend.Value
    expression116 = extrudeBuilder12.Limits.EndExtend.Value
    extrudeBuilder12.Destroy()
    
    workPart.Expressions.Delete(expression113)
    
    workPart.Expressions.Delete(expression114)
    
    markId224 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder13 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section11 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder13.Section = section11
    
    extrudeBuilder13.AllowSelfIntersectingSection(True)
    
    expression117 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder13.DistanceTolerance = 0.01
    
    extrudeBuilder13.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies81 = [NXOpen.Body.Null] * 1 
    targetBodies81[0] = NXOpen.Body.Null
    extrudeBuilder13.BooleanOperation.SetTargetBodies(targetBodies81)
    
    extrudeBuilder13.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder13.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder13.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies82 = [NXOpen.Body.Null] * 1 
    targetBodies82[0] = NXOpen.Body.Null
    extrudeBuilder13.BooleanOperation.SetTargetBodies(targetBodies82)
    
    extrudeBuilder13.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder13.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder13.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder13.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder11 = extrudeBuilder13.SmartVolumeProfile
    
    smartVolumeProfileBuilder11.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder11.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId224, "Extrude Dialog")
    
    section11.DistanceTolerance = 0.01
    
    section11.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section11.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    extrudeBuilder13.Destroy()
    
    section11.Destroy()
    
    workPart.Expressions.Delete(expression117)
    
    theSession.UndoToMark(markId224, None)
    
    theSession.DeleteUndoMark(markId224, None)
    
    markId225 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder4 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression118 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression119 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData4 = edgeBlendBuilder4.LimitsListData
    
    origin11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane11 = workPart.Planes.CreatePlane(origin11, normal11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder4 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression120 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression121 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId225, "Edge Blend Dialog")
    
    rotMatrix42 = NXOpen.Matrix3x3()
    
    rotMatrix42.Xx = 0.81842810250630393
    rotMatrix42.Xy = 0.18736611041931145
    rotMatrix42.Xz = 0.54320289183164794
    rotMatrix42.Yx = -0.079552853282554278
    rotMatrix42.Yy = -0.89929251632695228
    rotMatrix42.Yz = 0.43005152436997535
    rotMatrix42.Zx = 0.56907537687245946
    rotMatrix42.Zy = -0.39517959302660544
    rotMatrix42.Zz = -0.72110075904327697
    translation42 = NXOpen.Point3d(-133.49789862670926, 15.853647184547208, -103.25884978002895)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix42, translation42, 0.90572327300952049)
    
    scCollector3 = workPart.ScCollectors.CreateCollector()
    
    seedEdges4 = [NXOpen.Edge.Null] * 1 
    extrude6 = feature20
    edge8 = extrude6.FindObject("EDGE * 130 * 140 {(25,7.5,-65)(17.5,0,-65)(25,-7.5,-65) EXTRUDE(2)}")
    seedEdges4[0] = edge8
    edgeMultipleSeedTangentRule4 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges4, 0.5, True)
    
    rules13 = [None] * 1 
    rules13[0] = edgeMultipleSeedTangentRule4
    scCollector3.ReplaceRules(rules13, False)
    
    scCollector3.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId226 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder4.Tolerance = 0.01
    
    edgeBlendBuilder4.AllInstancesOption = False
    
    edgeBlendBuilder4.RemoveSelfIntersection = True
    
    edgeBlendBuilder4.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder4.LimitFailingAreas = True
    
    edgeBlendBuilder4.ConvexConcaveY = False
    
    edgeBlendBuilder4.RollOverSmoothEdge = True
    
    edgeBlendBuilder4.RollOntoEdge = True
    
    edgeBlendBuilder4.MoveSharpEdge = True
    
    edgeBlendBuilder4.TrimmingOption = False
    
    edgeBlendBuilder4.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder4.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder4.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder4.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex2 = edgeBlendBuilder4.AddChainset(scCollector3, "7.5")
    
    feature21 = edgeBlendBuilder4.CommitFeature()
    
    theSession.DeleteUndoMark(markId226, None)
    
    theSession.SetUndoMarkName(markId225, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder4)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression121)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression120)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression118)
    
    workPart.Expressions.Delete(expression119)
    
    markId227 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder5 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression122 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression123 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData5 = edgeBlendBuilder5.LimitsListData
    
    origin12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal12 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane12 = workPart.Planes.CreatePlane(origin12, normal12, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder5 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression124 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression125 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId227, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    rotMatrix43 = NXOpen.Matrix3x3()
    
    rotMatrix43.Xx = 0.99214050911497009
    rotMatrix43.Xy = -0.093034223536625327
    rotMatrix43.Xz = 0.08367701849385463
    rotMatrix43.Yx = -0.11835534966713349
    rotMatrix43.Yy = -0.48069750996643751
    rotMatrix43.Yz = 0.86886242588641849
    rotMatrix43.Zx = -0.040610606721080293
    rotMatrix43.Zy = -0.87193723235276477
    rotMatrix43.Zz = -0.48793057032608683
    translation43 = NXOpen.Point3d(-134.14932015149176, 15.999156545989379, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix43, translation43, 0.90572327300952049)
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder5)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression125)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression124)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression122)
    
    workPart.Expressions.Delete(expression123)
    
    theSession.UndoToMark(markId227, None)
    
    theSession.DeleteUndoMark(markId227, None)
    
    markId228 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects11 = [NXOpen.DisplayableObject.Null] * 2 
    objects11[0] = sketch11
    objects11[1] = arc8
    theSession.DisplayManager.BlankObjects(objects11)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    scaleAboutPoint293 = NXOpen.Point3d(-86.468647765268813, 9.3479619205695474, 0.0)
    viewCenter293 = NXOpen.Point3d(86.468647765268912, -9.3479619205696221, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint293, viewCenter293)
    
    scaleAboutPoint294 = NXOpen.Point3d(-69.174918212215019, 7.4783695364556575, 0.0)
    viewCenter294 = NXOpen.Point3d(69.174918212215175, -7.478369536455717, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint294, viewCenter294)
    
    scaleAboutPoint295 = NXOpen.Point3d(-56.461690000240331, 5.9826956291645095, 0.0)
    viewCenter295 = NXOpen.Point3d(56.461690000240516, -5.9826956291645734, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint295, viewCenter295)
    
    scaleAboutPoint296 = NXOpen.Point3d(-70.577112500300444, 7.4783695364556566, 0.0)
    viewCenter296 = NXOpen.Point3d(70.577112500300601, -7.4783695364557161, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint296, viewCenter296)
    
    scaleAboutPoint297 = NXOpen.Point3d(-88.221390625375534, 9.3479619205695688, 0.0)
    viewCenter297 = NXOpen.Point3d(88.221390625375733, -9.3479619205696185, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint297, viewCenter297)
    
    scaleAboutPoint298 = NXOpen.Point3d(-110.27673828171947, 11.684952400711962, 0.0)
    viewCenter298 = NXOpen.Point3d(110.27673828171966, -11.684952400712024, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint298, viewCenter298)
    
    rotMatrix44 = NXOpen.Matrix3x3()
    
    rotMatrix44.Xx = 0.95252289447868377
    rotMatrix44.Xy = -0.30444612410280386
    rotMatrix44.Xz = 0.0035627254631580662
    rotMatrix44.Yx = 0.094861080682276847
    rotMatrix44.Yy = 0.30787101760632074
    rotMatrix44.Yz = 0.94668728305065453
    rotMatrix44.Zx = -0.28931213397598138
    rotMatrix44.Zy = -0.90140334702996383
    rotMatrix44.Zz = 0.32213428115839438
    translation44 = NXOpen.Point3d(-184.40483980790393, 21.257385126309799, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix44, translation44, 0.57966289472609334)
    
    scaleAboutPoint299 = NXOpen.Point3d(-198.55290212147341, 57.511875097254361, 0.0)
    viewCenter299 = NXOpen.Point3d(198.55290212147364, -57.511875097254439, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint299, viewCenter299)
    
    rotMatrix45 = NXOpen.Matrix3x3()
    
    rotMatrix45.Xx = 0.82726400653237286
    rotMatrix45.Xy = -0.55095317087288398
    rotMatrix45.Xz = 0.10993119212085882
    rotMatrix45.Yx = 0.14935831457489979
    rotMatrix45.Yy = 0.40430780574986463
    rotMatrix45.Yz = 0.90234543943938972
    rotMatrix45.Zx = -0.5415961201516718
    rotMatrix45.Zy = -0.73005876593246555
    rotMatrix45.Zz = 0.41675873226821747
    translation45 = NXOpen.Point3d(-234.04306533827233, 35.6353539006234, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix45, translation45, 0.4637303157808747)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId229 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder14 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section12 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder14.Section = section12
    
    extrudeBuilder14.AllowSelfIntersectingSection(True)
    
    expression126 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder14.DistanceTolerance = 0.01
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies83 = [NXOpen.Body.Null] * 1 
    targetBodies83[0] = NXOpen.Body.Null
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies83)
    
    extrudeBuilder14.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder14.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies84 = [NXOpen.Body.Null] * 1 
    targetBodies84[0] = NXOpen.Body.Null
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies84)
    
    extrudeBuilder14.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder14.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder14.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder14.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder12 = extrudeBuilder14.SmartVolumeProfile
    
    smartVolumeProfileBuilder12.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder12.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId229, "Extrude Dialog")
    
    section12.DistanceTolerance = 0.01
    
    section12.ChainingTolerance = 0.0094999999999999998
    
    section12.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar10 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point46 = workPart.Points.CreatePoint(edge5, scalar10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction24 = workPart.Directions.CreateDirection(edge1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face2 = extrude1.FindObject("FACE 170 {(-25,0,0) EXTRUDE(2)}")
    xform9 = workPart.Xforms.CreateXformByPlaneXDirPoint(face2, direction24, point46, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem10 = workPart.CoordinateSystems.CreateCoordinateSystem(xform9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder8 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder8.Csys = cartesianCoordinateSystem10
    
    datumCsysBuilder8.DisplayScaleFactor = 1.25
    
    feature22 = datumCsysBuilder8.CommitFeature()
    
    datumCsysBuilder8.Destroy()
    
    markId230 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder13 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder13.Csystem = cartesianCoordinateSystem10
    
    sketchInPlaceBuilder13.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject26 = sketchInPlaceBuilder13.Commit()
    
    sketchInPlaceBuilder13.Destroy()
    
    sketch12 = nXObject26
    sketch12.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId231 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId231, None, True)
    
    markId232 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_003")
    
    markId233 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint300 = NXOpen.Point3d(77.310109877757668, -58.19654027698364, 0.0)
    viewCenter300 = NXOpen.Point3d(-77.310109877757469, 58.19654027698364, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint300, viewCenter300)
    
    scaleAboutPoint301 = NXOpen.Point3d(90.932094182786926, -63.474167704063028, 0.0)
    viewCenter301 = NXOpen.Point3d(-90.93209418278667, 63.474167704063028, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint301, viewCenter301)
    
    scaleAboutPoint302 = NXOpen.Point3d(112.77362660904454, -79.342709630078772, 0.0)
    viewCenter302 = NXOpen.Point3d(-112.77362660904423, 79.342709630078772, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint302, viewCenter302)
    
    scaleAboutPoint303 = NXOpen.Point3d(140.96703326130566, -99.178387037598469, 0.0)
    viewCenter303 = NXOpen.Point3d(-140.96703326130546, 99.178387037598469, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint303, viewCenter303)
    
    scaleAboutPoint304 = NXOpen.Point3d(112.77362660904454, -79.342709630078772, 0.0)
    viewCenter304 = NXOpen.Point3d(-112.77362660904423, 79.342709630078772, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint304, viewCenter304)
    
    scaleAboutPoint305 = NXOpen.Point3d(90.218901287235624, -63.474167704063014, 0.0)
    viewCenter305 = NXOpen.Point3d(-90.218901287235369, 63.474167704063014, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint305, viewCenter305)
    
    scaleAboutPoint306 = NXOpen.Point3d(72.1751210297885, -50.779334163250461, 0.0)
    viewCenter306 = NXOpen.Point3d(-72.175121029788301, 50.779334163250361, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint306, viewCenter306)
    
    scaleAboutPoint307 = NXOpen.Point3d(57.740096823830797, -40.623467330600363, 0.0)
    viewCenter307 = NXOpen.Point3d(-57.740096823830555, 40.623467330600285, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint307, viewCenter307)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId233, "Curve")
    
    markId234 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId235 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId235, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix9 = theSession.ActiveSketch.Orientation
    
    center10 = NXOpen.Point3d(-25.000000000000007, -7.1054273576010019e-15, 28.0)
    arc9 = workPart.Curves.CreateArc(center10, nXMatrix9, 15.899175564315801, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc9, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_17 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_17.Geometry = arc9
    dimObject1_17.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_17.AssocValue = 0
    dimObject1_17.HelpPoint.X = 0.0
    dimObject1_17.HelpPoint.Y = 0.0
    dimObject1_17.HelpPoint.Z = 0.0
    dimObject1_17.View = NXOpen.NXObject.Null
    dimOrigin17 = NXOpen.Point3d(-25.000000000000007, -7.1054273576010019e-15, 32.140337464819211)
    sketchDimensionalConstraint17 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_17, dimOrigin17, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension17 = sketchDimensionalConstraint17.AssociatedDimension
    
    expression127 = sketchDimensionalConstraint17.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId236 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder23 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines129 = []
    sketchRapidDimensionBuilder23.AppendedText.SetBefore(lines129)
    
    lines130 = []
    sketchRapidDimensionBuilder23.AppendedText.SetAfter(lines130)
    
    lines131 = []
    sketchRapidDimensionBuilder23.AppendedText.SetAbove(lines131)
    
    lines132 = []
    sketchRapidDimensionBuilder23.AppendedText.SetBelow(lines132)
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder23.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines133 = []
    sketchRapidDimensionBuilder23.AppendedText.SetBefore(lines133)
    
    lines134 = []
    sketchRapidDimensionBuilder23.AppendedText.SetAfter(lines134)
    
    lines135 = []
    sketchRapidDimensionBuilder23.AppendedText.SetAbove(lines135)
    
    lines136 = []
    sketchRapidDimensionBuilder23.AppendedText.SetBelow(lines136)
    
    theSession.SetUndoMarkName(markId236, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder23.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits543 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits544 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits545 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits546 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits547 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits548 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits549 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits550 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits551 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits552 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder23.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder23.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits553 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits554 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits555 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits556 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits557 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits558 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits559 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits560 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits561 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits562 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    point1_33 = NXOpen.Point3d(-25.000000000000007, -6.5500190394110875, 42.487271454911344)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder23.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    point1_34 = NXOpen.Point3d(-25.000000000000007, -6.5500190394110875, 42.487271454911344)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder23.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc9, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    point1_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder23.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    dimensionlinearunits563 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits564 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits565 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits566 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits567 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits568 = sketchRapidDimensionBuilder23.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin13 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin13.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin13.View = NXOpen.View.Null
    assocOrigin13.ViewOfGeometry = workPart.ModelingViews.WorkView
    point47 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin13.PointOnGeometry = point47
    assocOrigin13.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.DimensionLine = 0
    assocOrigin13.AssociatedView = NXOpen.View.Null
    assocOrigin13.AssociatedPoint = NXOpen.Point.Null
    assocOrigin13.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.XOffsetFactor = 0.0
    assocOrigin13.YOffsetFactor = 0.0
    assocOrigin13.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder23.Origin.SetAssociativeOrigin(assocOrigin13)
    
    point48 = NXOpen.Point3d(-25.000000000000007, -56.302563707053899, 65.03436027975205)
    sketchRapidDimensionBuilder23.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point48)
    
    sketchRapidDimensionBuilder23.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder23.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder23.Style.DimensionStyle.TextCentered = False
    
    markId237 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject27 = sketchRapidDimensionBuilder23.Commit()
    
    theSession.DeleteUndoMark(markId237, None)
    
    theSession.SetUndoMarkName(markId236, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId236, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder23.Destroy()
    
    markId238 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder24 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines137 = []
    sketchRapidDimensionBuilder24.AppendedText.SetBefore(lines137)
    
    lines138 = []
    sketchRapidDimensionBuilder24.AppendedText.SetAfter(lines138)
    
    lines139 = []
    sketchRapidDimensionBuilder24.AppendedText.SetAbove(lines139)
    
    lines140 = []
    sketchRapidDimensionBuilder24.AppendedText.SetBelow(lines140)
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder24.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId238, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder24.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits569 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits570 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits571 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits572 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits573 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits574 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits575 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits576 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits577 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits578 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder24.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits579 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits580 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits581 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits582 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits583 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits584 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits585 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits586 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits587 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits588 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    expression128 = workPart.Expressions.FindObject("p38")
    expression128.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId238, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId239 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.47172257263662276)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId239, None)
    
    markId240 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId238, "Edit Driving Value")
    
    point1_36 = NXOpen.Point3d(-25.000000000000007, 6.2515808411932525, 52.66453260241105)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    point1_37 = NXOpen.Point3d(-25.000000000000007, 6.2515808411932525, 52.66453260241105)
    point2_37 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc9, workPart.ModelingViews.WorkView, point1_37, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_37)
    
    point1_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_38, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_38)
    
    dimensionlinearunits589 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits590 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits591 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits592 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits593 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits594 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    edge9 = extrude1.FindObject("EDGE * 160 * 170 {(-25,25,80)(-25,25,0)(-25,25,-80) EXTRUDE(2)}")
    point49 = NXOpen.Point3d(-25.000000000000007, 24.999999999999993, 29.614348315093796)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(edge9, workPart.ModelingViews.WorkView, point49)
    
    point1_39 = NXOpen.Point3d(-25.000000000000007, 24.999999999999993, 29.614348315093796)
    point2_39 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge9, workPart.ModelingViews.WorkView, point1_39, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_39)
    
    point1_40 = NXOpen.Point3d(-25.000000000000007, 6.2515808411932525, 52.66453260241105)
    point2_40 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_40, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_40)
    
    point1_41 = NXOpen.Point3d(-25.000000000000007, 24.999999999999993, 29.614348315093796)
    point2_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge9, workPart.ModelingViews.WorkView, point1_41, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_41)
    
    point1_42 = NXOpen.Point3d(-25.000000000000007, 6.2515808411932525, 52.66453260241105)
    point2_42 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder24.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_42, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_42)
    
    dimensionlinearunits595 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits596 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits597 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits598 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits599 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits600 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits601 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits602 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits603 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits604 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits605 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits606 = sketchRapidDimensionBuilder24.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin14 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin14.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin14.View = NXOpen.View.Null
    assocOrigin14.ViewOfGeometry = workPart.ModelingViews.WorkView
    point50 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin14.PointOnGeometry = point50
    assocOrigin14.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.DimensionLine = 0
    assocOrigin14.AssociatedView = NXOpen.View.Null
    assocOrigin14.AssociatedPoint = NXOpen.Point.Null
    assocOrigin14.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.XOffsetFactor = 0.0
    assocOrigin14.YOffsetFactor = 0.0
    assocOrigin14.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder24.Origin.SetAssociativeOrigin(assocOrigin14)
    
    point51 = NXOpen.Point3d(-25.000000000000007, 3.2176625840728552, 113.96509845773357)
    sketchRapidDimensionBuilder24.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point51)
    
    sketchRapidDimensionBuilder24.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder24.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder24.Style.DimensionStyle.TextCentered = False
    
    markId241 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject28 = sketchRapidDimensionBuilder24.Commit()
    
    theSession.DeleteUndoMark(markId241, None)
    
    theSession.SetUndoMarkName(markId240, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId240, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder24.Destroy()
    
    markId242 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder25 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines141 = []
    sketchRapidDimensionBuilder25.AppendedText.SetBefore(lines141)
    
    lines142 = []
    sketchRapidDimensionBuilder25.AppendedText.SetAfter(lines142)
    
    lines143 = []
    sketchRapidDimensionBuilder25.AppendedText.SetAbove(lines143)
    
    lines144 = []
    sketchRapidDimensionBuilder25.AppendedText.SetBelow(lines144)
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder25.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId242, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder25.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits607 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits608 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits609 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits610 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits611 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits612 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits613 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits614 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits615 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits616 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder25.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits617 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits618 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits619 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits620 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits621 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits622 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits623 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits624 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits625 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits626 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    expression129 = workPart.Expressions.FindObject("p39")
    expression129.SetFormula("25")
    
    theSession.SetUndoMarkVisibility(markId242, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId243 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId243, None)
    
    markId244 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId242, "Edit Driving Value")
    
    expression129.SetFormula("25+15")
    
    theSession.SetUndoMarkVisibility(markId244, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId245 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId245, None)
    
    markId246 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId244, "Edit Driving Value")
    
    expression129.SetFormula("25+7.5")
    
    theSession.SetUndoMarkVisibility(markId246, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId247 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId247, None)
    
    markId248 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId246, "Edit Driving Value")
    
    point1_43 = NXOpen.Point3d(-25.000000000000007, -5.9069440814072118, 50.848953338724556)
    point2_43 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_43, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_43)
    
    point1_44 = NXOpen.Point3d(-25.000000000000007, -5.9069440814072118, 50.848953338724556)
    point2_44 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc9, workPart.ModelingViews.WorkView, point1_44, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_44)
    
    point1_45 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_45 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_45, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_45)
    
    dimensionlinearunits627 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits628 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits629 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits630 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits631 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits632 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    edge10 = extrude1.FindObject("EDGE * 130 * 140 {(-25,-25,80)(0,-25,80)(25,-25,80) EXTRUDE(2)}")
    point1_46 = NXOpen.Point3d(-25.000000000000007, -24.999999999999993, 80.0)
    point2_46 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, edge10, workPart.ModelingViews.WorkView, point1_46, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_46)
    
    point1_47 = NXOpen.Point3d(-25.000000000000007, -5.9069440814072118, 50.848953338724556)
    point2_47 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_47, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_47)
    
    point1_48 = NXOpen.Point3d(-25.000000000000007, -24.999999999999993, 80.0)
    point2_48 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, edge10, workPart.ModelingViews.WorkView, point1_48, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_48)
    
    point1_49 = NXOpen.Point3d(-25.000000000000007, -5.9069440814072118, 50.848953338724556)
    point2_49 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_49, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_49)
    
    point1_50 = NXOpen.Point3d(-25.000000000000007, -24.999999999999993, 80.0)
    point2_50 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, edge10, workPart.ModelingViews.WorkView, point1_50, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_50)
    
    dimensionlinearunits633 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits634 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits635 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits636 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits637 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits638 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits639 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits640 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits641 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits642 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits643 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits644 = sketchRapidDimensionBuilder25.Style.UnitsStyle.DimensionLinearUnits
    
    point1_51 = NXOpen.Point3d(-25.000000000000007, -5.9069440814072118, 50.848953338724556)
    point2_51 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc9, workPart.ModelingViews.WorkView, point1_51, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_51)
    
    point1_52 = NXOpen.Point3d(-25.000000000000007, -24.999999999999993, 80.0)
    point2_52 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder25.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, edge10, workPart.ModelingViews.WorkView, point1_52, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_52)
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin15 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin15.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin15.View = NXOpen.View.Null
    assocOrigin15.ViewOfGeometry = workPart.ModelingViews.WorkView
    point52 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin15.PointOnGeometry = point52
    assocOrigin15.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin15.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin15.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.DimensionLine = 0
    assocOrigin15.AssociatedView = NXOpen.View.Null
    assocOrigin15.AssociatedPoint = NXOpen.Point.Null
    assocOrigin15.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin15.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin15.XOffsetFactor = 0.0
    assocOrigin15.YOffsetFactor = 0.0
    assocOrigin15.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder25.Origin.SetAssociativeOrigin(assocOrigin15)
    
    point53 = NXOpen.Point3d(-25.000000000000007, -89.531647096578638, 58.461574554351571)
    sketchRapidDimensionBuilder25.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point53)
    
    sketchRapidDimensionBuilder25.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder25.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder25.Style.DimensionStyle.TextCentered = False
    
    markId249 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject29 = sketchRapidDimensionBuilder25.Commit()
    
    theSession.DeleteUndoMark(markId249, None)
    
    theSession.SetUndoMarkName(markId248, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId248, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder25.Destroy()
    
    markId250 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder26 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines145 = []
    sketchRapidDimensionBuilder26.AppendedText.SetBefore(lines145)
    
    lines146 = []
    sketchRapidDimensionBuilder26.AppendedText.SetAfter(lines146)
    
    lines147 = []
    sketchRapidDimensionBuilder26.AppendedText.SetAbove(lines147)
    
    lines148 = []
    sketchRapidDimensionBuilder26.AppendedText.SetBelow(lines148)
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder26.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder26.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder26.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId250, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder26.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits645 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits646 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits647 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits648 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits649 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits650 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits651 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits652 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits653 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits654 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder26.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder26.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder26.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits655 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits656 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits657 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits658 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits659 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits660 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits661 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits662 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits663 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits664 = sketchRapidDimensionBuilder26.Style.UnitsStyle.DimensionLinearUnits
    
    expression130 = workPart.Expressions.FindObject("p40")
    expression130.SetFormula("50")
    
    theSession.SetUndoMarkVisibility(markId250, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId251 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId251, None)
    
    markId252 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId250, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder26.Destroy()
    
    theSession.UndoToMark(markId252, None)
    
    theSession.DeleteUndoMark(markId252, None)
    
    sketchRapidDimensionBuilder26.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId253 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId230, None)
    
    section12.DistanceTolerance = 0.01
    
    section12.ChainingTolerance = 0.0094999999999999998
    
    markId254 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves7 = [NXOpen.ICurve.Null] * 1 
    curves7[0] = arc9
    seedPoint7 = NXOpen.Point3d(-25.000000000000007, -7.5171350625661635e-15, 40.0)
    regionBoundaryRule7 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch12, curves7, seedPoint7, 0.01)
    
    section12.AllowSelfIntersection(True)
    
    rules14 = [None] * 1 
    rules14[0] = regionBoundaryRule7
    helpPoint9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section12.AddToSection(rules14, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint9, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId254, None)
    
    expression131 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs9 = section12.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression131)
    
    expression132 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction25 = workPart.Directions.CreateDirection(sketch12, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder14.Direction = direction25
    
    targetBodies85 = [NXOpen.Body.Null] * 1 
    targetBodies85[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies85)
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies86 = [NXOpen.Body.Null] * 1 
    targetBodies86[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies86)
    
    scaleAboutPoint308 = NXOpen.Point3d(-221.16743163921137, 74.11151403213681, 0.0)
    viewCenter308 = NXOpen.Point3d(221.16743163921157, -74.11151403213681, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint308, viewCenter308)
    
    scaleAboutPoint309 = NXOpen.Point3d(-276.45928954901422, 92.639392540170945, 0.0)
    viewCenter309 = NXOpen.Point3d(276.45928954901444, -92.639392540171073, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint309, viewCenter309)
    
    scaleAboutPoint310 = NXOpen.Point3d(-345.57411193626785, 115.79924067521368, 0.0)
    viewCenter310 = NXOpen.Point3d(345.57411193626797, -115.79924067521384, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint310, viewCenter310)
    
    scaleAboutPoint311 = NXOpen.Point3d(-276.45928954901422, 92.639392540170945, 0.0)
    viewCenter311 = NXOpen.Point3d(276.45928954901444, -92.639392540171073, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint311, viewCenter311)
    
    scaleAboutPoint312 = NXOpen.Point3d(-221.16743163921137, 74.11151403213681, 0.0)
    viewCenter312 = NXOpen.Point3d(221.16743163921157, -74.111514032136853, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint312, viewCenter312)
    
    scaleAboutPoint313 = NXOpen.Point3d(-176.93394531136909, 59.289211225709451, 0.0)
    viewCenter313 = NXOpen.Point3d(176.93394531136934, -59.289211225709487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint313, viewCenter313)
    
    scaleAboutPoint314 = NXOpen.Point3d(-141.5471562490952, 47.431368980567527, 0.0)
    viewCenter314 = NXOpen.Point3d(141.54715624909545, -47.431368980567591, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint314, viewCenter314)
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies87 = [NXOpen.Body.Null] * 1 
    targetBodies87[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies87)
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies88 = [NXOpen.Body.Null] * 1 
    targetBodies88[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies88)
    
    direction26 = extrudeBuilder14.Direction
    
    success8 = direction26.ReverseDirection()
    
    extrudeBuilder14.Direction = direction26
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies89 = [NXOpen.Body.Null] * 1 
    targetBodies89[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies89)
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies90 = [NXOpen.Body.Null] * 1 
    targetBodies90[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies90)
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies91 = [NXOpen.Body.Null] * 1 
    targetBodies91[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies91)
    
    extrudeBuilder14.Limits.EndExtend.Value.SetFormula("6")
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies92 = [NXOpen.Body.Null] * 1 
    targetBodies92[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies92)
    
    extrudeBuilder14.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies93 = [NXOpen.Body.Null] * 1 
    targetBodies93[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies93)
    
    extrudeBuilder14.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder14.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies94 = [NXOpen.Body.Null] * 1 
    targetBodies94[0] = body1
    extrudeBuilder14.BooleanOperation.SetTargetBodies(targetBodies94)
    
    markId255 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder14.ParentFeatureInternal = True
    
    feature23 = extrudeBuilder14.CommitFeature()
    
    theSession.DeleteUndoMark(markId255, None)
    
    theSession.SetUndoMarkName(markId229, "Extrude")
    
    expression133 = extrudeBuilder14.Limits.StartExtend.Value
    expression134 = extrudeBuilder14.Limits.EndExtend.Value
    extrudeBuilder14.Destroy()
    
    workPart.Expressions.Delete(expression126)
    
    workPart.Expressions.Delete(expression132)
    
    markId256 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder15 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section13 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder15.Section = section13
    
    extrudeBuilder15.AllowSelfIntersectingSection(True)
    
    expression135 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder15.DistanceTolerance = 0.01
    
    extrudeBuilder15.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies95 = [NXOpen.Body.Null] * 1 
    targetBodies95[0] = NXOpen.Body.Null
    extrudeBuilder15.BooleanOperation.SetTargetBodies(targetBodies95)
    
    extrudeBuilder15.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder15.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder15.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies96 = [NXOpen.Body.Null] * 1 
    targetBodies96[0] = NXOpen.Body.Null
    extrudeBuilder15.BooleanOperation.SetTargetBodies(targetBodies96)
    
    extrudeBuilder15.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder15.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder15.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder15.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder13 = extrudeBuilder15.SmartVolumeProfile
    
    smartVolumeProfileBuilder13.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder13.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId256, "Extrude Dialog")
    
    section13.DistanceTolerance = 0.01
    
    section13.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section13.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    extrudeBuilder15.Destroy()
    
    section13.Destroy()
    
    workPart.Expressions.Delete(expression135)
    
    theSession.UndoToMark(markId256, None)
    
    theSession.DeleteUndoMark(markId256, None)
    
    markId257 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder6 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression136 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression137 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData6 = edgeBlendBuilder6.LimitsListData
    
    origin13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal13 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane13 = workPart.Planes.CreatePlane(origin13, normal13, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder6 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression138 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression139 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId257, "Edge Blend Dialog")
    
    scaleAboutPoint315 = NXOpen.Point3d(-163.73159181953395, 30.47558825838037, 0.0)
    viewCenter315 = NXOpen.Point3d(163.73159181953415, -30.475588258380444, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint315, viewCenter315)
    
    rotMatrix46 = NXOpen.Matrix3x3()
    
    rotMatrix46.Xx = 0.42778901584097062
    rotMatrix46.Xy = -0.85009433791243927
    rotMatrix46.Xz = 0.30714194532011607
    rotMatrix46.Yx = 0.16131382127853966
    rotMatrix46.Yy = 0.40615298227811397
    rotMatrix46.Yz = 0.899454060000348
    rotMatrix46.Zx = -0.88936742069311781
    rotMatrix46.Zy = -0.33523032624720195
    rotMatrix46.Zz = 0.31087975066553519
    translation46 = NXOpen.Point3d(-93.367040334430314, -6.6261825987354399, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix46, translation46, 1.1069310529460723)
    
    scCollector4 = workPart.ScCollectors.CreateCollector()
    
    seedEdges5 = [NXOpen.Edge.Null] * 1 
    extrude7 = feature23
    edge11 = extrude7.FindObject("EDGE * 130 * 140 {(-10,3.75,31.0048094716167)(-10,-7.5,37.5)(-10,3.75,43.9951905283833) EXTRUDE(2)}")
    seedEdges5[0] = edge11
    edgeMultipleSeedTangentRule5 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges5, 0.5, True)
    
    rules15 = [None] * 1 
    rules15[0] = edgeMultipleSeedTangentRule5
    scCollector4.ReplaceRules(rules15, False)
    
    scCollector4.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId258 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder6.Tolerance = 0.01
    
    edgeBlendBuilder6.AllInstancesOption = False
    
    edgeBlendBuilder6.RemoveSelfIntersection = True
    
    edgeBlendBuilder6.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder6.LimitFailingAreas = True
    
    edgeBlendBuilder6.ConvexConcaveY = False
    
    edgeBlendBuilder6.RollOverSmoothEdge = True
    
    edgeBlendBuilder6.RollOntoEdge = True
    
    edgeBlendBuilder6.MoveSharpEdge = True
    
    edgeBlendBuilder6.TrimmingOption = False
    
    edgeBlendBuilder6.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder6.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder6.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder6.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex3 = edgeBlendBuilder6.AddChainset(scCollector4, "7.5")
    
    feature24 = edgeBlendBuilder6.CommitFeature()
    
    theSession.DeleteUndoMark(markId258, None)
    
    theSession.SetUndoMarkName(markId257, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder6)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression139)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression138)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder6.Destroy()
    
    workPart.Expressions.Delete(expression136)
    
    workPart.Expressions.Delete(expression137)
    
    markId259 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder7 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression140 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression141 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData7 = edgeBlendBuilder7.LimitsListData
    
    origin14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal14 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane14 = workPart.Planes.CreatePlane(origin14, normal14, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder7 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression142 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression143 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId259, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    rotMatrix47 = NXOpen.Matrix3x3()
    
    rotMatrix47.Xx = 0.84998672198322134
    rotMatrix47.Xy = 0.52671556253816976
    rotMatrix47.Xz = -0.0096586040560902049
    rotMatrix47.Yx = -0.1307798241410825
    rotMatrix47.Yy = 0.22873526270695149
    rotMatrix47.Yz = 0.9646640955234137
    rotMatrix47.Zx = 0.51031285507014301
    rotMatrix47.Zy = -0.81868852182895069
    rotMatrix47.Zz = 0.26330570479136628
    translation47 = NXOpen.Point3d(-93.367040334430314, -6.6261825987354399, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix47, translation47, 1.1069310529460723)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder7)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression143)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression142)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder7.Destroy()
    
    workPart.Expressions.Delete(expression140)
    
    workPart.Expressions.Delete(expression141)
    
    theSession.UndoToMark(markId259, None)
    
    theSession.DeleteUndoMark(markId259, None)
    
    markId260 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder16 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section14 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder16.Section = section14
    
    extrudeBuilder16.AllowSelfIntersectingSection(True)
    
    expression144 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder16.DistanceTolerance = 0.01
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies97 = [NXOpen.Body.Null] * 1 
    targetBodies97[0] = NXOpen.Body.Null
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies97)
    
    extrudeBuilder16.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder16.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies98 = [NXOpen.Body.Null] * 1 
    targetBodies98[0] = NXOpen.Body.Null
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies98)
    
    extrudeBuilder16.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder16.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder16.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder16.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder14 = extrudeBuilder16.SmartVolumeProfile
    
    smartVolumeProfileBuilder14.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder14.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId260, "Extrude Dialog")
    
    section14.DistanceTolerance = 0.01
    
    section14.ChainingTolerance = 0.0094999999999999998
    
    section14.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar11 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge12 = extrude1.FindObject("EDGE * 150 * 160 {(25,25,80)(25,25,0)(25,25,-80) EXTRUDE(2)}")
    point54 = workPart.Points.CreatePoint(edge12, scalar11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge13 = extrude1.FindObject("EDGE * 120 * 150 1 {(25,7.5,-80)(25,16.25,-80)(25,25,-80) EXTRUDE(2)}")
    direction27 = workPart.Directions.CreateDirection(edge13, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face3 = extrude1.FindObject("FACE 150 {(25,0,0) EXTRUDE(2)}")
    xform10 = workPart.Xforms.CreateXformByPlaneXDirPoint(face3, direction27, point54, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem11 = workPart.CoordinateSystems.CreateCoordinateSystem(xform10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder9 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder9.Csys = cartesianCoordinateSystem11
    
    datumCsysBuilder9.DisplayScaleFactor = 1.25
    
    feature25 = datumCsysBuilder9.CommitFeature()
    
    datumCsysBuilder9.Destroy()
    
    markId261 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder14 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder14.Csystem = cartesianCoordinateSystem11
    
    sketchInPlaceBuilder14.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject30 = sketchInPlaceBuilder14.Commit()
    
    sketchInPlaceBuilder14.Destroy()
    
    sketch13 = nXObject30
    sketch13.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId262 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId262, None, True)
    
    markId263 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_004")
    
    markId264 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint316 = NXOpen.Point3d(-7.1278209644342274, -36.457051490221502, 0.0)
    viewCenter316 = NXOpen.Point3d(7.1278209644344308, 36.457051490221424, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint316, viewCenter316)
    
    scaleAboutPoint317 = NXOpen.Point3d(-5.7022567715473489, -29.165641192177215, 0.0)
    viewCenter317 = NXOpen.Point3d(5.7022567715475772, 29.165641192177137, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint317, viewCenter317)
    
    scaleAboutPoint318 = NXOpen.Point3d(-4.5618054172378404, -23.332512953741791, 0.0)
    viewCenter318 = NXOpen.Point3d(4.5618054172380758, 23.332512953741698, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint318, viewCenter318)
    
    scaleAboutPoint319 = NXOpen.Point3d(-3.6494443337902829, -18.666010362993433, 0.0)
    viewCenter319 = NXOpen.Point3d(3.6494443337904707, 18.666010362993347, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint319, viewCenter319)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId264, "Curve")
    
    markId265 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId266 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId266, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix10 = theSession.ActiveSketch.Orientation
    
    center11 = NXOpen.Point3d(25.000000000000007, -1.0000000000000071, 39.5)
    arc10 = workPart.Curves.CreateArc(center11, nXMatrix10, 16.145303931631933, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc10, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_18 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_18.Geometry = arc10
    dimObject1_18.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_18.AssocValue = 0
    dimObject1_18.HelpPoint.X = 0.0
    dimObject1_18.HelpPoint.Y = 0.0
    dimObject1_18.HelpPoint.Z = 0.0
    dimObject1_18.View = NXOpen.NXObject.Null
    dimOrigin18 = NXOpen.Point3d(25.000000000000007, -1.0000000000000071, 40.585364624377569)
    sketchDimensionalConstraint18 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_18, dimOrigin18, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension18 = sketchDimensionalConstraint18.AssociatedDimension
    
    expression145 = sketchDimensionalConstraint18.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId267 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder27 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines149 = []
    sketchRapidDimensionBuilder27.AppendedText.SetBefore(lines149)
    
    lines150 = []
    sketchRapidDimensionBuilder27.AppendedText.SetAfter(lines150)
    
    lines151 = []
    sketchRapidDimensionBuilder27.AppendedText.SetAbove(lines151)
    
    lines152 = []
    sketchRapidDimensionBuilder27.AppendedText.SetBelow(lines152)
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder27.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines153 = []
    sketchRapidDimensionBuilder27.AppendedText.SetBefore(lines153)
    
    lines154 = []
    sketchRapidDimensionBuilder27.AppendedText.SetAfter(lines154)
    
    lines155 = []
    sketchRapidDimensionBuilder27.AppendedText.SetAbove(lines155)
    
    lines156 = []
    sketchRapidDimensionBuilder27.AppendedText.SetBelow(lines156)
    
    theSession.SetUndoMarkName(markId267, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder27.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits665 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits666 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits667 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits668 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits669 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits670 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits671 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits672 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits673 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits674 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder27.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder27.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits675 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits676 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits677 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits678 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits679 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits680 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits681 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits682 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits683 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits684 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    point1_53 = NXOpen.Point3d(25.000000000000007, 5.6054292523492348, 54.23224841756948)
    point2_53 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder27.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc10, workPart.ModelingViews.WorkView, point1_53, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_53)
    
    point1_54 = NXOpen.Point3d(25.000000000000007, 5.6054292523492348, 54.23224841756948)
    point2_54 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder27.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc10, workPart.ModelingViews.WorkView, point1_54, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_54)
    
    point1_55 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_55 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder27.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_55, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_55)
    
    dimensionlinearunits685 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits686 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits687 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits688 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits689 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits690 = sketchRapidDimensionBuilder27.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin16 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin16.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin16.View = NXOpen.View.Null
    assocOrigin16.ViewOfGeometry = workPart.ModelingViews.WorkView
    point55 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin16.PointOnGeometry = point55
    assocOrigin16.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin16.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin16.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.DimensionLine = 0
    assocOrigin16.AssociatedView = NXOpen.View.Null
    assocOrigin16.AssociatedPoint = NXOpen.Point.Null
    assocOrigin16.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin16.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin16.XOffsetFactor = 0.0
    assocOrigin16.YOffsetFactor = 0.0
    assocOrigin16.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder27.Origin.SetAssociativeOrigin(assocOrigin16)
    
    point56 = NXOpen.Point3d(25.000000000000007, 17.10639399503269, 54.934000987707819)
    sketchRapidDimensionBuilder27.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point56)
    
    sketchRapidDimensionBuilder27.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder27.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder27.Style.DimensionStyle.TextCentered = False
    
    markId268 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject31 = sketchRapidDimensionBuilder27.Commit()
    
    theSession.DeleteUndoMark(markId268, None)
    
    theSession.SetUndoMarkName(markId267, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId267, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder27.Destroy()
    
    markId269 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder28 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines157 = []
    sketchRapidDimensionBuilder28.AppendedText.SetBefore(lines157)
    
    lines158 = []
    sketchRapidDimensionBuilder28.AppendedText.SetAfter(lines158)
    
    lines159 = []
    sketchRapidDimensionBuilder28.AppendedText.SetAbove(lines159)
    
    lines160 = []
    sketchRapidDimensionBuilder28.AppendedText.SetBelow(lines160)
    
    sketchRapidDimensionBuilder28.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder28.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder28.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder28.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder28.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId269, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder28.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder28.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits691 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits692 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits693 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits694 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits695 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits696 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits697 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits698 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits699 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits700 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder28.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder28.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder28.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder28.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder28.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits701 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits702 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits703 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits704 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits705 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits706 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits707 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits708 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits709 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits710 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    expression146 = workPart.Expressions.FindObject("p56")
    expression146.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId269, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId270 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.46453136043520821)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId270, None)
    
    markId271 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId269, "Edit Driving Value")
    
    point57 = NXOpen.Point3d(25.000000000000007, 24.999999999999993, 60.007326881239351)
    sketchRapidDimensionBuilder28.FirstAssociativity.SetValue(edge12, workPart.ModelingViews.WorkView, point57)
    
    point1_56 = NXOpen.Point3d(25.000000000000007, 9.9567817969243606, 68.075339462954602)
    point2_56 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder28.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc10, workPart.ModelingViews.WorkView, point1_56, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_56)
    
    dimensionlinearunits711 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits712 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits713 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits714 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits715 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits716 = sketchRapidDimensionBuilder28.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder28.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin17 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin17.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin17.View = NXOpen.View.Null
    assocOrigin17.ViewOfGeometry = workPart.ModelingViews.WorkView
    point58 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin17.PointOnGeometry = point58
    assocOrigin17.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin17.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin17.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.DimensionLine = 0
    assocOrigin17.AssociatedView = NXOpen.View.Null
    assocOrigin17.AssociatedPoint = NXOpen.Point.Null
    assocOrigin17.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin17.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin17.XOffsetFactor = 0.0
    assocOrigin17.YOffsetFactor = 0.0
    assocOrigin17.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder28.Origin.SetAssociativeOrigin(assocOrigin17)
    
    point59 = NXOpen.Point3d(25.000000000000007, 13.564638182567268, 91.787406063361431)
    sketchRapidDimensionBuilder28.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point59)
    
    sketchRapidDimensionBuilder28.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder28.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder28.Style.DimensionStyle.TextCentered = True
    
    markId272 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject32 = sketchRapidDimensionBuilder28.Commit()
    
    theSession.DeleteUndoMark(markId272, None)
    
    theSession.SetUndoMarkName(markId271, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId271, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder28.Destroy()
    
    markId273 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder29 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines161 = []
    sketchRapidDimensionBuilder29.AppendedText.SetBefore(lines161)
    
    lines162 = []
    sketchRapidDimensionBuilder29.AppendedText.SetAfter(lines162)
    
    lines163 = []
    sketchRapidDimensionBuilder29.AppendedText.SetAbove(lines163)
    
    lines164 = []
    sketchRapidDimensionBuilder29.AppendedText.SetBelow(lines164)
    
    sketchRapidDimensionBuilder29.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder29.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder29.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder29.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder29.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId273, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder29.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder29.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits717 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits718 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits719 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits720 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits721 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits722 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits723 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits724 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits725 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits726 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder29.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder29.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder29.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder29.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder29.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits727 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits728 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits729 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits730 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits731 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits732 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits733 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits734 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits735 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits736 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    expression147 = workPart.Expressions.FindObject("p57")
    expression147.SetFormula("25+7.5")
    
    theSession.SetUndoMarkVisibility(markId273, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId274 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId274, None)
    
    markId275 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId273, "Edit Driving Value")
    
    point1_57 = NXOpen.Point3d(25.000000000000007, -7.1054273576010019e-15, 61.186479902374067)
    point2_57 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc10, workPart.ModelingViews.WorkView, point1_57, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_57)
    
    point1_58 = NXOpen.Point3d(25.000000000000007, -7.1054273576010019e-15, 61.186479902374067)
    point2_58 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc10, workPart.ModelingViews.WorkView, point1_58, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_58)
    
    point1_59 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_59 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_59, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_59)
    
    dimensionlinearunits737 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits738 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits739 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits740 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits741 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits742 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    edge14 = extrude1.FindObject("EDGE * 130 * 150 {(25,-25,80)(25,0,80)(25,25,80) EXTRUDE(2)}")
    point60 = NXOpen.Point3d(25.000000000000007, -15.822362747888986, 80.0)
    sketchRapidDimensionBuilder29.SecondAssociativity.SetValue(edge14, workPart.ModelingViews.WorkView, point60)
    
    point1_60 = NXOpen.Point3d(25.000000000000007, -15.822362747888986, 80.0)
    point2_60 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge14, workPart.ModelingViews.WorkView, point1_60, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_60)
    
    point1_61 = NXOpen.Point3d(25.000000000000007, -7.1054273576010019e-15, 61.186479902374067)
    point2_61 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc10, workPart.ModelingViews.WorkView, point1_61, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_61)
    
    point1_62 = NXOpen.Point3d(25.000000000000007, -15.822362747888986, 80.0)
    point2_62 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge14, workPart.ModelingViews.WorkView, point1_62, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_62)
    
    point1_63 = NXOpen.Point3d(25.000000000000007, -7.1054273576010019e-15, 61.186479902374067)
    point2_63 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder29.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc10, workPart.ModelingViews.WorkView, point1_63, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_63)
    
    dimensionlinearunits743 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits744 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits745 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits746 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits747 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits748 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits749 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits750 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits751 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits752 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits753 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits754 = sketchRapidDimensionBuilder29.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder29.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin18 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin18.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin18.View = NXOpen.View.Null
    assocOrigin18.ViewOfGeometry = workPart.ModelingViews.WorkView
    point61 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin18.PointOnGeometry = point61
    assocOrigin18.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin18.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin18.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.DimensionLine = 0
    assocOrigin18.AssociatedView = NXOpen.View.Null
    assocOrigin18.AssociatedPoint = NXOpen.Point.Null
    assocOrigin18.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin18.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin18.XOffsetFactor = 0.0
    assocOrigin18.YOffsetFactor = 0.0
    assocOrigin18.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder29.Origin.SetAssociativeOrigin(assocOrigin18)
    
    point62 = NXOpen.Point3d(25.000000000000007, -34.584096240948995, 70.058255538235798)
    sketchRapidDimensionBuilder29.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point62)
    
    sketchRapidDimensionBuilder29.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder29.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder29.Style.DimensionStyle.TextCentered = True
    
    markId276 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject33 = sketchRapidDimensionBuilder29.Commit()
    
    theSession.DeleteUndoMark(markId276, None)
    
    theSession.SetUndoMarkName(markId275, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId275, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder29.Destroy()
    
    markId277 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder30 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines165 = []
    sketchRapidDimensionBuilder30.AppendedText.SetBefore(lines165)
    
    lines166 = []
    sketchRapidDimensionBuilder30.AppendedText.SetAfter(lines166)
    
    lines167 = []
    sketchRapidDimensionBuilder30.AppendedText.SetAbove(lines167)
    
    lines168 = []
    sketchRapidDimensionBuilder30.AppendedText.SetBelow(lines168)
    
    sketchRapidDimensionBuilder30.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder30.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder30.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder30.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder30.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId277, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder30.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder30.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits755 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits756 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits757 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits758 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits759 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits760 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits761 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits762 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits763 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits764 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder30.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder30.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder30.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder30.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder30.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits765 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits766 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits767 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits768 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits769 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits770 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits771 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits772 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits773 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits774 = sketchRapidDimensionBuilder30.Style.UnitsStyle.DimensionLinearUnits
    
    expression148 = workPart.Expressions.FindObject("p58")
    expression148.SetFormula("50")
    
    theSession.SetUndoMarkVisibility(markId277, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId278 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId278, None)
    
    markId279 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId277, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder30.Destroy()
    
    theSession.UndoToMark(markId279, None)
    
    theSession.DeleteUndoMark(markId279, None)
    
    sketchRapidDimensionBuilder30.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId280 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId261, None)
    
    section14.DistanceTolerance = 0.01
    
    section14.ChainingTolerance = 0.0094999999999999998
    
    markId281 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves8 = [NXOpen.ICurve.Null] * 1 
    curves8[0] = arc10
    seedPoint8 = NXOpen.Point3d(25.000000000000007, 2.4999999999999925, 29.999999999999996)
    regionBoundaryRule8 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch13, curves8, seedPoint8, 0.01)
    
    section14.AllowSelfIntersection(True)
    
    rules16 = [None] * 1 
    rules16[0] = regionBoundaryRule8
    helpPoint10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section14.AddToSection(rules16, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint10, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId281, None)
    
    expression149 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs10 = section14.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression149)
    
    expression150 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction28 = workPart.Directions.CreateDirection(sketch13, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder16.Direction = direction28
    
    targetBodies99 = [NXOpen.Body.Null] * 1 
    targetBodies99[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies99)
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies100 = [NXOpen.Body.Null] * 1 
    targetBodies100[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies100)
    
    rotMatrix48 = NXOpen.Matrix3x3()
    
    rotMatrix48.Xx = 0.99237245481415759
    rotMatrix48.Xy = 0.072979741607261603
    rotMatrix48.Xz = 0.099352243261336376
    rotMatrix48.Yx = -0.11749588458334448
    rotMatrix48.Yy = 0.31605934003440944
    rotMatrix48.Yz = 0.9414357177646232
    rotMatrix48.Zx = 0.037304530986193005
    rotMatrix48.Zy = -0.94592835399513753
    rotMatrix48.Zz = 0.32222340243369829
    translation48 = NXOpen.Point3d(-93.367040334430314, -6.6261825987354399, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix48, translation48, 1.1069310529460723)
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies101 = [NXOpen.Body.Null] * 1 
    targetBodies101[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies101)
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies102 = [NXOpen.Body.Null] * 1 
    targetBodies102[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies102)
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies103 = [NXOpen.Body.Null] * 1 
    targetBodies103[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies103)
    
    direction29 = extrudeBuilder16.Direction
    
    success9 = direction29.ReverseDirection()
    
    extrudeBuilder16.Direction = direction29
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies104 = [NXOpen.Body.Null] * 1 
    targetBodies104[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies104)
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies105 = [NXOpen.Body.Null] * 1 
    targetBodies105[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies105)
    
    extrudeBuilder16.Limits.EndExtend.Value.SetFormula("11")
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies106 = [NXOpen.Body.Null] * 1 
    targetBodies106[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies106)
    
    rotMatrix49 = NXOpen.Matrix3x3()
    
    rotMatrix49.Xx = 0.90231884012341435
    rotMatrix49.Xy = 0.42663737205393626
    rotMatrix49.Xz = 0.061654387720930327
    rotMatrix49.Yx = -0.13293914858194145
    rotMatrix49.Yy = 0.13935338778983666
    rotMatrix49.Yz = 0.98127866382888385
    rotMatrix49.Zx = 0.41005840258753418
    rotMatrix49.Zy = -0.89362250759389372
    rotMatrix49.Zz = 0.18245799623188133
    translation49 = NXOpen.Point3d(-93.367040334430314, -6.6261825987354399, -100.97252734155317)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix49, translation49, 1.1069310529460723)
    
    extrudeBuilder16.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder16.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies107 = [NXOpen.Body.Null] * 1 
    targetBodies107[0] = body1
    extrudeBuilder16.BooleanOperation.SetTargetBodies(targetBodies107)
    
    markId282 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder16.ParentFeatureInternal = True
    
    feature26 = extrudeBuilder16.CommitFeature()
    
    theSession.DeleteUndoMark(markId282, None)
    
    theSession.SetUndoMarkName(markId260, "Extrude")
    
    expression151 = extrudeBuilder16.Limits.StartExtend.Value
    expression152 = extrudeBuilder16.Limits.EndExtend.Value
    extrudeBuilder16.Destroy()
    
    workPart.Expressions.Delete(expression144)
    
    workPart.Expressions.Delete(expression150)
    
    markId283 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder17 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section15 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder17.Section = section15
    
    extrudeBuilder17.AllowSelfIntersectingSection(True)
    
    expression153 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder17.DistanceTolerance = 0.01
    
    extrudeBuilder17.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies108 = [NXOpen.Body.Null] * 1 
    targetBodies108[0] = NXOpen.Body.Null
    extrudeBuilder17.BooleanOperation.SetTargetBodies(targetBodies108)
    
    extrudeBuilder17.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder17.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder17.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies109 = [NXOpen.Body.Null] * 1 
    targetBodies109[0] = NXOpen.Body.Null
    extrudeBuilder17.BooleanOperation.SetTargetBodies(targetBodies109)
    
    extrudeBuilder17.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder17.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder17.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder17.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder15 = extrudeBuilder17.SmartVolumeProfile
    
    smartVolumeProfileBuilder15.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder15.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId283, "Extrude Dialog")
    
    section15.DistanceTolerance = 0.01
    
    section15.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section15.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    extrudeBuilder17.Destroy()
    
    section15.Destroy()
    
    workPart.Expressions.Delete(expression153)
    
    theSession.UndoToMark(markId283, None)
    
    theSession.DeleteUndoMark(markId283, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit with Rollback...
    # ----------------------------------------------
    markId284 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Redefine Feature")
    
    extrude8 = feature26
    editWithRollbackManager3 = workPart.Features.StartEditWithRollbackManager(extrude8, markId284)
    
    markId285 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder18 = workPart.Features.CreateExtrudeBuilder(extrude8)
    
    section14.PrepareMappingData()
    
    extrudeBuilder18.AllowSelfIntersectingSection(True)
    
    targetBodies110 = [NXOpen.Body.Null] * 1 
    targetBodies110[0] = body1
    extrudeBuilder18.BooleanOperation.SetTargetBodies(targetBodies110)
    
    targetBodies111 = [NXOpen.Body.Null] * 1 
    targetBodies111[0] = body1
    extrudeBuilder18.BooleanOperation.SetTargetBodies(targetBodies111)
    
    expression154 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    expression155 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId285, "Extrude Dialog")
    
    sketchFeature5 = workPart.Features.FindObject("EXTRUDE(10:1B)")
    extrudeBuilder18.ShowInternalParentFeatureForEdit(sketchFeature5)
    
    refs11 = section14.EvaluateAndAskOutputEntities()
    
    section14.DistanceTolerance = 0.01
    
    section14.ChainingTolerance = 0.0094999999999999998
    
    rotMatrix50 = NXOpen.Matrix3x3()
    
    rotMatrix50.Xx = 0.44462579780549316
    rotMatrix50.Xy = 0.89520106970032254
    rotMatrix50.Xz = -0.030380005484184763
    rotMatrix50.Yx = -0.053061817298909103
    rotMatrix50.Yy = 0.0601816935518125
    rotMatrix50.Yz = 0.99677610690975516
    rotMatrix50.Zx = 0.89414335733749084
    rotMatrix50.Zy = -0.44158035346766145
    rotMatrix50.Zz = 0.074259329114986769
    translation50 = NXOpen.Point3d(-77.101057403767783, -9.4075862967426005, -97.292172167083692)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix50, translation50, 1.1069310529460723)
    
    markId286 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId287 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    face4 = extrude1.FindObject("FACE 140 {(0,-25,0) EXTRUDE(2)}")
    curves9 = [NXOpen.ICurve.Null] * 5 
    curves9[0] = arc10
    curves9[1] = edge2
    edge15 = extrude1.FindObject("EDGE * 140 * 150 {(25,-25,80)(25,-25,0)(25,-25,-80) EXTRUDE(2)}")
    curves9[2] = edge15
    curves9[3] = edge10
    edge16 = extrude1.FindObject("EDGE * 140 * 170 {(-25,-25,80)(-25,-25,0)(-25,-25,-80) EXTRUDE(2)}")
    curves9[4] = edge16
    seedPoint9 = NXOpen.Point3d(11.811400411488648, -24.999999999977263, 53.300914018990397)
    regionBoundaryRule9 = workPart.ScRuleFactory.CreateRuleRegionBoundary(face4, curves9, seedPoint9, 0.01)
    
    section14.AllowSelfIntersection(True)
    
    rules17 = [None] * 1 
    rules17[0] = regionBoundaryRule9
    helpPoint11 = NXOpen.Point3d(11.811400411488648, -24.999999999977263, 53.300914018990397)
    section14.AddToSection(rules17, face4, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint11, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId287, None)
    
    extrudeBuilder18.Draft.DraftOption = NXOpen.GeometricUtilities.SimpleDraft.SimpleDraftType.NoDraft
    
    workPart.Expressions.Delete(expression155)
    
    expression156 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression157 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.DeleteUndoMark(markId286, None)
    
    expression158 = extrudeBuilder18.Limits.StartExtend.Value
    expression159 = extrudeBuilder18.Limits.EndExtend.Value
    extrudeBuilder18.Destroy()
    
    workPart.Expressions.Delete(expression154)
    
    workPart.Expressions.Delete(expression156)
    
    workPart.Expressions.Delete(expression157)
    
    theSession.UndoToMark(markId285, None)
    
    theSession.DeleteUndoMark(markId285, None)
    
    theSession.DeleteUndoMark(markId285, None)
    
    editWithRollbackManager3.UpdateFeature(True)
    
    editWithRollbackManager3.Stop()
    
    theSession.UndoToMarkWithStatus(markId284, None)
    
    theSession.DeleteUndoMarksUpToMark(markId284, None, False)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit with Rollback...
    # ----------------------------------------------
    markId288 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Redefine Feature")
    
    editWithRollbackManager4 = workPart.Features.StartEditWithRollbackManager(extrude8, markId288)
    
    markId289 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrudeBuilder19 = workPart.Features.CreateExtrudeBuilder(extrude8)
    
    section14.PrepareMappingData()
    
    extrudeBuilder19.AllowSelfIntersectingSection(True)
    
    targetBodies112 = [NXOpen.Body.Null] * 1 
    targetBodies112[0] = body1
    extrudeBuilder19.BooleanOperation.SetTargetBodies(targetBodies112)
    
    targetBodies113 = [NXOpen.Body.Null] * 1 
    targetBodies113[0] = body1
    extrudeBuilder19.BooleanOperation.SetTargetBodies(targetBodies113)
    
    expression160 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    expression161 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId289, "Extrude Dialog")
    
    extrudeBuilder19.ShowInternalParentFeatureForEdit(sketchFeature5)
    
    refs12 = section14.EvaluateAndAskOutputEntities()
    
    section14.DistanceTolerance = 0.01
    
    section14.ChainingTolerance = 0.0094999999999999998
    
    scaleAboutPoint320 = NXOpen.Point3d(-66.20970939271659, 19.360961952382816, 0.0)
    viewCenter320 = NXOpen.Point3d(66.209709392716789, -19.360961952382898, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint320, viewCenter320)
    
    rotMatrix51 = NXOpen.Matrix3x3()
    
    rotMatrix51.Xx = 0.015983014696511467
    rotMatrix51.Xy = 0.99759201854879076
    rotMatrix51.Xz = -0.06748857509942327
    rotMatrix51.Yx = -0.1997278578903445
    rotMatrix51.Yy = 0.069322252561449041
    rotMatrix51.Yz = 0.97739613672365988
    rotMatrix51.Zx = 0.97972104500400392
    rotMatrix51.Zy = -0.0021423882808872564
    rotMatrix51.Zz = 0.20035489549474067
    translation51 = NXOpen.Point3d(-79.558558141700615, 0.19603651777003117, -99.051398773422676)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix51, translation51, 0.88554484235685793)
    
    markId290 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId291 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId291, None)
    
    workPart.Expressions.Delete(expression161)
    
    expression162 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.DeleteUndoMark(markId290, None)
    
    expression148.SetFormula("50-7.5")
    
    sketch13.LocalUpdate()
    
    scaleAboutPoint321 = NXOpen.Point3d(-97.999930870085961, 7.4695069260735645, 0.0)
    viewCenter321 = NXOpen.Point3d(97.999930870086175, -7.4695069260736409, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint321, viewCenter321)
    
    rotMatrix52 = NXOpen.Matrix3x3()
    
    rotMatrix52.Xx = 0.98142042817991948
    rotMatrix52.Xy = -0.038136534436464475
    rotMatrix52.Xz = -0.18804134623086716
    rotMatrix52.Yx = 0.18131305193681121
    rotMatrix52.Yy = -0.13626216085404808
    rotMatrix52.Yz = 0.9739395262113264
    rotMatrix52.Zx = -0.062765598447713955
    rotMatrix52.Zy = -0.98993849721109328
    rotMatrix52.Zz = -0.1268158168011326
    translation52 = NXOpen.Point3d(-141.48691240850195, -11.036803006351713, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix52, translation52, 0.70843587388548634)
    
    markId292 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId292, None)
    
    markId293 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature27 = extrudeBuilder19.CommitFeature()
    
    theSession.DeleteUndoMark(markId293, None)
    
    theSession.SetUndoMarkName(markId289, "Extrude")
    
    section14.CleanMappingData()
    
    expression163 = extrudeBuilder19.Limits.StartExtend.Value
    expression164 = extrudeBuilder19.Limits.EndExtend.Value
    extrudeBuilder19.Destroy()
    
    workPart.Expressions.Delete(expression160)
    
    workPart.Expressions.Delete(expression162)
    
    theSession.DeleteUndoMark(markId289, None)
    
    editWithRollbackManager4.UpdateFeature(False)
    
    editWithRollbackManager4.Stop()
    
    editWithRollbackManager4.Destroy()
    
    rotMatrix53 = NXOpen.Matrix3x3()
    
    rotMatrix53.Xx = 0.39576186507955868
    rotMatrix53.Xy = 0.91124647673088188
    rotMatrix53.Xz = -0.1140280877428676
    rotMatrix53.Yx = -0.20881431014878624
    rotMatrix53.Yy = 0.21020507413362843
    rotMatrix53.Yz = 0.95509706872419942
    rotMatrix53.Zx = 0.89429812144822696
    rotMatrix53.Zy = -0.35418030077069601
    rotMatrix53.Zz = 0.27347245660238506
    translation53 = NXOpen.Point3d(-141.48691240850195, -11.036803006351713, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix53, translation53, 0.70843587388548634)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId294 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder8 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression165 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression166 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData8 = edgeBlendBuilder8.LimitsListData
    
    origin15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal15 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane15 = workPart.Planes.CreatePlane(origin15, normal15, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder8 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression167 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression168 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId294, "Edge Blend Dialog")
    
    scCollector5 = workPart.ScCollectors.CreateCollector()
    
    seedEdges6 = [NXOpen.Edge.Null] * 1 
    extrude9 = feature27
    edge17 = extrude9.FindObject("EDGE * 130 * 140 {(10,-3.75,31.0048094716167)(10,7.5,37.5)(10,-3.75,43.9951905283833) EXTRUDE(2)}")
    seedEdges6[0] = edge17
    edgeMultipleSeedTangentRule6 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges6, 0.5, True)
    
    rules18 = [None] * 1 
    rules18[0] = edgeMultipleSeedTangentRule6
    scCollector5.ReplaceRules(rules18, False)
    
    scCollector5.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId295 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder8.Tolerance = 0.01
    
    edgeBlendBuilder8.AllInstancesOption = False
    
    edgeBlendBuilder8.RemoveSelfIntersection = True
    
    edgeBlendBuilder8.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder8.LimitFailingAreas = True
    
    edgeBlendBuilder8.ConvexConcaveY = False
    
    edgeBlendBuilder8.RollOverSmoothEdge = True
    
    edgeBlendBuilder8.RollOntoEdge = True
    
    edgeBlendBuilder8.MoveSharpEdge = True
    
    edgeBlendBuilder8.TrimmingOption = False
    
    edgeBlendBuilder8.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder8.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder8.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder8.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex4 = edgeBlendBuilder8.AddChainset(scCollector5, "7.5")
    
    feature28 = edgeBlendBuilder8.CommitFeature()
    
    theSession.DeleteUndoMark(markId295, None)
    
    theSession.SetUndoMarkName(markId294, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder8)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression168)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression167)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder8.Destroy()
    
    workPart.Expressions.Delete(expression165)
    
    workPart.Expressions.Delete(expression166)
    
    markId296 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder9 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression169 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression170 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData9 = edgeBlendBuilder9.LimitsListData
    
    origin16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal16 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane16 = workPart.Planes.CreatePlane(origin16, normal16, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder9 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression171 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression172 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId296, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    rotMatrix54 = NXOpen.Matrix3x3()
    
    rotMatrix54.Xx = 0.88754745417251857
    rotMatrix54.Xy = -0.45235820204507682
    rotMatrix54.Xz = 0.087358878394948963
    rotMatrix54.Yx = 0.020212751674697878
    rotMatrix54.Yy = 0.22766523181874659
    rotMatrix54.Yz = 0.97352965383220458
    rotMatrix54.Zx = -0.46027270314631408
    rotMatrix54.Zy = -0.86228800250464921
    rotMatrix54.Zz = 0.21120710091027517
    translation54 = NXOpen.Point3d(-141.48691240850195, -11.036803006351713, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix54, translation54, 0.70843587388548634)
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder9)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression172)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression171)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder9.Destroy()
    
    workPart.Expressions.Delete(expression169)
    
    workPart.Expressions.Delete(expression170)
    
    theSession.UndoToMark(markId296, None)
    
    theSession.DeleteUndoMark(markId296, None)
    
    rotMatrix55 = NXOpen.Matrix3x3()
    
    rotMatrix55.Xx = 0.99891115420881693
    rotMatrix55.Xy = -0.046335290562099986
    rotMatrix55.Xz = 0.0054357010343733282
    rotMatrix55.Yx = 0.04257581515587424
    rotMatrix55.Yy = 0.95303833535956073
    rotMatrix55.Yz = 0.29984201056371401
    rotMatrix55.Zx = -0.019073698147505338
    rotMatrix55.Zy = -0.29928409945000972
    rotMatrix55.Zz = 0.95397338634543394
    translation55 = NXOpen.Point3d(-141.48691240850195, -11.036803006351713, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix55, translation55, 0.70843587388548634)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId297 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder20 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section16 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder20.Section = section16
    
    extrudeBuilder20.AllowSelfIntersectingSection(True)
    
    expression173 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder20.DistanceTolerance = 0.01
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies114 = [NXOpen.Body.Null] * 1 
    targetBodies114[0] = NXOpen.Body.Null
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies114)
    
    extrudeBuilder20.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder20.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies115 = [NXOpen.Body.Null] * 1 
    targetBodies115[0] = NXOpen.Body.Null
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies115)
    
    extrudeBuilder20.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder20.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder20.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder20.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder16 = extrudeBuilder20.SmartVolumeProfile
    
    smartVolumeProfileBuilder16.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder16.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId297, "Extrude Dialog")
    
    section16.DistanceTolerance = 0.01
    
    section16.ChainingTolerance = 0.0094999999999999998
    
    section16.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar12 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge18 = extrude1.FindObject("EDGE * 130 * 160 {(25,25,80)(0,25,80)(-25,25,80) EXTRUDE(2)}")
    point63 = workPart.Points.CreatePoint(edge18, scalar12, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction30 = workPart.Directions.CreateDirection(edge10, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face5 = extrude1.FindObject("FACE 130 {(0,0,80) EXTRUDE(2)}")
    xform11 = workPart.Xforms.CreateXformByPlaneXDirPoint(face5, direction30, point63, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem12 = workPart.CoordinateSystems.CreateCoordinateSystem(xform11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder10 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder10.Csys = cartesianCoordinateSystem12
    
    datumCsysBuilder10.DisplayScaleFactor = 1.25
    
    feature29 = datumCsysBuilder10.CommitFeature()
    
    datumCsysBuilder10.Destroy()
    
    markId298 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder15 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder15.Csystem = cartesianCoordinateSystem12
    
    sketchInPlaceBuilder15.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
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
    
    nXObject34 = sketchInPlaceBuilder15.Commit()
    
    sketchInPlaceBuilder15.Destroy()
    
    sketch14 = nXObject34
    sketch14.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId299 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId299, None, True)
    
    markId300 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_005")
    
    markId301 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId301, "Curve")
    
    markId302 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    scaleAboutPoint322 = NXOpen.Point3d(31.932142108964833, -23.528946817131981, 0.0)
    viewCenter322 = NXOpen.Point3d(-31.932142108964637, 23.528946817131885, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint322, viewCenter322)
    
    scaleAboutPoint323 = NXOpen.Point3d(39.915177636206039, -29.411183521414976, 0.0)
    viewCenter323 = NXOpen.Point3d(-39.915177636205833, 29.411183521414852, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint323, viewCenter323)
    
    scaleAboutPoint324 = NXOpen.Point3d(49.893972045257492, -36.763979401768715, 0.0)
    viewCenter324 = NXOpen.Point3d(-49.893972045257293, 36.763979401768616, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint324, viewCenter324)
    
    scaleAboutPoint325 = NXOpen.Point3d(74.038569628561916, -43.037198109213449, 0.0)
    viewCenter325 = NXOpen.Point3d(-74.03856962856166, 43.037198109213257, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint325, viewCenter325)
    
    scaleAboutPoint326 = NXOpen.Point3d(59.230855702849517, -34.429758487370755, 0.0)
    viewCenter326 = NXOpen.Point3d(-59.230855702849318, 34.429758487370499, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint326, viewCenter326)
    
    scaleAboutPoint327 = NXOpen.Point3d(47.384684562279659, -27.543806789896646, 0.0)
    viewCenter327 = NXOpen.Point3d(-47.384684562279453, 27.543806789896401, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint327, viewCenter327)
    
    scaleAboutPoint328 = NXOpen.Point3d(37.907747649823762, -22.03504543191735, 0.0)
    viewCenter328 = NXOpen.Point3d(-37.907747649823499, 22.035045431917123, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint328, viewCenter328)
    
    scaleAboutPoint329 = NXOpen.Point3d(30.326198119859008, -17.628036345533907, 0.0)
    viewCenter329 = NXOpen.Point3d(-30.326198119858802, 17.628036345533648, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint329, viewCenter329)
    
    scaleAboutPoint330 = NXOpen.Point3d(5.617069208407468, -14.819501741330209, 0.0)
    viewCenter330 = NXOpen.Point3d(-5.6170692084072593, 14.819501741329958, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint330, viewCenter330)
    
    markId303 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId303, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix11 = theSession.ActiveSketch.Orientation
    
    center12 = NXOpen.Point3d(-0.040642606524940561, 0.0, 80.0)
    arc11 = workPart.Curves.CreateArc(center12, nXMatrix11, 10.832249715870246, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc11, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_19 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_19.Geometry = arc11
    dimObject1_19.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_19.AssocValue = 0
    dimObject1_19.HelpPoint.X = 0.0
    dimObject1_19.HelpPoint.Y = 0.0
    dimObject1_19.HelpPoint.Z = 0.0
    dimObject1_19.View = NXOpen.NXObject.Null
    dimOrigin19 = NXOpen.Point3d(-0.040642606524940561, 2.1681567190769955, 80.0)
    sketchDimensionalConstraint19 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_19, dimOrigin19, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension19 = sketchDimensionalConstraint19.AssociatedDimension
    
    expression174 = sketchDimensionalConstraint19.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId304 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder31 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines169 = []
    sketchRapidDimensionBuilder31.AppendedText.SetBefore(lines169)
    
    lines170 = []
    sketchRapidDimensionBuilder31.AppendedText.SetAfter(lines170)
    
    lines171 = []
    sketchRapidDimensionBuilder31.AppendedText.SetAbove(lines171)
    
    lines172 = []
    sketchRapidDimensionBuilder31.AppendedText.SetBelow(lines172)
    
    sketchRapidDimensionBuilder31.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder31.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder31.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines173 = []
    sketchRapidDimensionBuilder31.AppendedText.SetBefore(lines173)
    
    lines174 = []
    sketchRapidDimensionBuilder31.AppendedText.SetAfter(lines174)
    
    lines175 = []
    sketchRapidDimensionBuilder31.AppendedText.SetAbove(lines175)
    
    lines176 = []
    sketchRapidDimensionBuilder31.AppendedText.SetBelow(lines176)
    
    theSession.SetUndoMarkName(markId304, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder31.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder31.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits775 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits776 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits777 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits778 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits779 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits780 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits781 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits782 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits783 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits784 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder31.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder31.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder31.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder31.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder31.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits785 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits786 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits787 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits788 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits789 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits790 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits791 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits792 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits793 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits794 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    point1_64 = NXOpen.Point3d(-0.040642606524940561, 0.0, 80.0)
    point2_64 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder31.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_64, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_64)
    
    point1_65 = NXOpen.Point3d(-0.040642606524940561, 0.0, 80.0)
    point2_65 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder31.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc11, workPart.ModelingViews.WorkView, point1_65, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_65)
    
    point1_66 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_66 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder31.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_66, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_66)
    
    dimensionlinearunits795 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits796 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits797 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits798 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits799 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits800 = sketchRapidDimensionBuilder31.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder31.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin19 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin19.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin19.View = NXOpen.View.Null
    assocOrigin19.ViewOfGeometry = workPart.ModelingViews.WorkView
    point64 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin19.PointOnGeometry = point64
    assocOrigin19.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin19.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin19.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.DimensionLine = 0
    assocOrigin19.AssociatedView = NXOpen.View.Null
    assocOrigin19.AssociatedPoint = NXOpen.Point.Null
    assocOrigin19.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin19.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin19.XOffsetFactor = 0.0
    assocOrigin19.YOffsetFactor = 0.0
    assocOrigin19.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder31.Origin.SetAssociativeOrigin(assocOrigin19)
    
    point65 = NXOpen.Point3d(18.125198237686114, 13.615164280951554, 80.0)
    sketchRapidDimensionBuilder31.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point65)
    
    sketchRapidDimensionBuilder31.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder31.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder31.Style.DimensionStyle.TextCentered = False
    
    markId305 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject35 = sketchRapidDimensionBuilder31.Commit()
    
    theSession.DeleteUndoMark(markId305, None)
    
    theSession.SetUndoMarkName(markId304, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId304, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder31.Destroy()
    
    markId306 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder32 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines177 = []
    sketchRapidDimensionBuilder32.AppendedText.SetBefore(lines177)
    
    lines178 = []
    sketchRapidDimensionBuilder32.AppendedText.SetAfter(lines178)
    
    lines179 = []
    sketchRapidDimensionBuilder32.AppendedText.SetAbove(lines179)
    
    lines180 = []
    sketchRapidDimensionBuilder32.AppendedText.SetBelow(lines180)
    
    sketchRapidDimensionBuilder32.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder32.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder32.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder32.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder32.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId306, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder32.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder32.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits801 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits802 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits803 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits804 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits805 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits806 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits807 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits808 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits809 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits810 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder32.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder32.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder32.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder32.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder32.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits811 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits812 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits813 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits814 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits815 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits816 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits817 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits818 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits819 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits820 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    expression175 = workPart.Expressions.FindObject("p74")
    expression175.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId306, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId307 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.692376948161745)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId307, None)
    
    markId308 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId306, "Edit Driving Value")
    
    point1_67 = NXOpen.Point3d(-7.7187162998274559, 7.6905762959563724, 80.0)
    point2_67 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_67, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_67)
    
    point1_68 = NXOpen.Point3d(-7.7187162998274559, 7.6905762959563724, 80.0)
    point2_68 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc11, workPart.ModelingViews.WorkView, point1_68, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_68)
    
    point1_69 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_69 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_69, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_69)
    
    dimensionlinearunits821 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits822 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits823 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits824 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits825 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits826 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    perpendicularDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    point66 = NXOpen.Point3d(-25.000000000000007, 10.938092998646759, 80.0)
    sketchRapidDimensionBuilder32.SecondAssociativity.SetValue(perpendicularDimension2, workPart.ModelingViews.WorkView, point66)
    
    line15 = theSession.ActiveSketch.FindObject("Curve DATUM12")
    point1_70 = NXOpen.Point3d(-25.000000000000007, 39.287499999999994, 80.0)
    point2_70 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line15, NXOpen.View.Null, point1_70, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_70)
    
    point1_71 = NXOpen.Point3d(-7.7187162998274559, 7.6905762959563724, 80.0)
    point2_71 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_71, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_71)
    
    point1_72 = NXOpen.Point3d(-25.000000000000007, 39.287499999999994, 80.0)
    point2_72 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line15, workPart.ModelingViews.WorkView, point1_72, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_72)
    
    point1_73 = NXOpen.Point3d(-7.7187162998274559, 7.6905762959563724, 80.0)
    point2_73 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder32.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_73, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_73)
    
    dimensionlinearunits827 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits828 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits829 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits830 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits831 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits832 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits833 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits834 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits835 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits836 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits837 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits838 = sketchRapidDimensionBuilder32.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder32.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin20 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin20.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin20.View = NXOpen.View.Null
    assocOrigin20.ViewOfGeometry = workPart.ModelingViews.WorkView
    point67 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin20.PointOnGeometry = point67
    assocOrigin20.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin20.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin20.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.DimensionLine = 0
    assocOrigin20.AssociatedView = NXOpen.View.Null
    assocOrigin20.AssociatedPoint = NXOpen.Point.Null
    assocOrigin20.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin20.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin20.XOffsetFactor = 0.0
    assocOrigin20.YOffsetFactor = 0.0
    assocOrigin20.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder32.Origin.SetAssociativeOrigin(assocOrigin20)
    
    point68 = NXOpen.Point3d(-10.175269603821659, 38.664902708232084, 80.0)
    sketchRapidDimensionBuilder32.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point68)
    
    sketchRapidDimensionBuilder32.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder32.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder32.Style.DimensionStyle.TextCentered = False
    
    markId309 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject36 = sketchRapidDimensionBuilder32.Commit()
    
    theSession.DeleteUndoMark(markId309, None)
    
    theSession.SetUndoMarkName(markId308, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId308, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder32.Destroy()
    
    markId310 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder33 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines181 = []
    sketchRapidDimensionBuilder33.AppendedText.SetBefore(lines181)
    
    lines182 = []
    sketchRapidDimensionBuilder33.AppendedText.SetAfter(lines182)
    
    lines183 = []
    sketchRapidDimensionBuilder33.AppendedText.SetAbove(lines183)
    
    lines184 = []
    sketchRapidDimensionBuilder33.AppendedText.SetBelow(lines184)
    
    sketchRapidDimensionBuilder33.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder33.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder33.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder33.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder33.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId310, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder33.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder33.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits839 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits840 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits841 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits842 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits843 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits844 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits845 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits846 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits847 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits848 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder33.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder33.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder33.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder33.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder33.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits849 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits850 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits851 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits852 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits853 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits854 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits855 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits856 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits857 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits858 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    expression176 = workPart.Expressions.FindObject("p75")
    expression176.SetFormula("25")
    
    theSession.SetUndoMarkVisibility(markId310, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId311 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId311, None)
    
    markId312 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId310, "Edit Driving Value")
    
    point1_74 = NXOpen.Point3d(-7.1054273576010019e-15, 7.6905762959563724, 80.0)
    point2_74 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_74, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_74)
    
    point1_75 = NXOpen.Point3d(-7.1054273576010019e-15, 7.6905762959563724, 80.0)
    point2_75 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc11, workPart.ModelingViews.WorkView, point1_75, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_75)
    
    point1_76 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_76 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_76, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_76)
    
    dimensionlinearunits859 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits860 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits861 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits862 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits863 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits864 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    point69 = NXOpen.Point3d(15.065688200766358, 24.999999999999993, 80.0)
    sketchRapidDimensionBuilder33.SecondAssociativity.SetValue(edge18, workPart.ModelingViews.WorkView, point69)
    
    point1_77 = NXOpen.Point3d(15.065688200766358, 24.999999999999993, 80.0)
    point2_77 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge18, workPart.ModelingViews.WorkView, point1_77, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_77)
    
    point1_78 = NXOpen.Point3d(-7.1054273576010019e-15, 7.6905762959563724, 80.0)
    point2_78 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_78, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_78)
    
    point1_79 = NXOpen.Point3d(15.065688200766358, 24.999999999999993, 80.0)
    point2_79 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge18, workPart.ModelingViews.WorkView, point1_79, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_79)
    
    point1_80 = NXOpen.Point3d(-7.1054273576010019e-15, 7.6905762959563724, 80.0)
    point2_80 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder33.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc11, workPart.ModelingViews.WorkView, point1_80, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_80)
    
    dimensionlinearunits865 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits866 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits867 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits868 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits869 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits870 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits871 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits872 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits873 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits874 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits875 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits876 = sketchRapidDimensionBuilder33.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder33.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin21 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin21.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin21.View = NXOpen.View.Null
    assocOrigin21.ViewOfGeometry = workPart.ModelingViews.WorkView
    point70 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin21.PointOnGeometry = point70
    assocOrigin21.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin21.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin21.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.DimensionLine = 0
    assocOrigin21.AssociatedView = NXOpen.View.Null
    assocOrigin21.AssociatedPoint = NXOpen.Point.Null
    assocOrigin21.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin21.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin21.XOffsetFactor = 0.0
    assocOrigin21.YOffsetFactor = 0.0
    assocOrigin21.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder33.Origin.SetAssociativeOrigin(assocOrigin21)
    
    point71 = NXOpen.Point3d(53.692002416878339, 17.057113072486271, 80.0)
    sketchRapidDimensionBuilder33.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point71)
    
    sketchRapidDimensionBuilder33.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder33.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder33.Style.DimensionStyle.TextCentered = True
    
    markId313 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject37 = sketchRapidDimensionBuilder33.Commit()
    
    theSession.DeleteUndoMark(markId313, None)
    
    theSession.SetUndoMarkName(markId312, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId312, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder33.Destroy()
    
    markId314 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder34 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines185 = []
    sketchRapidDimensionBuilder34.AppendedText.SetBefore(lines185)
    
    lines186 = []
    sketchRapidDimensionBuilder34.AppendedText.SetAfter(lines186)
    
    lines187 = []
    sketchRapidDimensionBuilder34.AppendedText.SetAbove(lines187)
    
    lines188 = []
    sketchRapidDimensionBuilder34.AppendedText.SetBelow(lines188)
    
    sketchRapidDimensionBuilder34.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder34.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder34.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder34.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder34.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId314, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder34.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder34.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits877 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits878 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits879 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits880 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits881 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits882 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits883 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits884 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits885 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits886 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder34.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder34.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder34.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder34.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder34.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits887 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits888 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits889 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits890 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits891 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits892 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits893 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits894 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits895 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits896 = sketchRapidDimensionBuilder34.Style.UnitsStyle.DimensionLinearUnits
    
    expression177 = workPart.Expressions.FindObject("p76")
    expression177.SetFormula("25")
    
    theSession.SetUndoMarkVisibility(markId314, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId315 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId315, None)
    
    markId316 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId314, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder34.Destroy()
    
    theSession.UndoToMark(markId316, None)
    
    theSession.DeleteUndoMark(markId316, None)
    
    sketchRapidDimensionBuilder34.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId317 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId298, None)
    
    section16.DistanceTolerance = 0.01
    
    section16.ChainingTolerance = 0.0094999999999999998
    
    markId318 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves10 = [NXOpen.ICurve.Null] * 1 
    curves10[0] = arc11
    seedPoint10 = NXOpen.Point3d(2.4999999999999925, -3.4694469519536142e-15, 80.0)
    regionBoundaryRule10 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch14, curves10, seedPoint10, 0.01)
    
    section16.AllowSelfIntersection(True)
    
    rules19 = [None] * 1 
    rules19[0] = regionBoundaryRule10
    helpPoint12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section16.AddToSection(rules19, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint12, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId318, None)
    
    expression178 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs13 = section16.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression178)
    
    expression179 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction31 = workPart.Directions.CreateDirection(sketch14, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder20.Direction = direction31
    
    targetBodies116 = [NXOpen.Body.Null] * 1 
    targetBodies116[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies116)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies117 = [NXOpen.Body.Null] * 1 
    targetBodies117[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies117)
    
    scaleAboutPoint331 = NXOpen.Point3d(-127.96515145145378, 12.605522381784942, 0.0)
    viewCenter331 = NXOpen.Point3d(127.96515145145398, -12.605522381785072, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint331, viewCenter331)
    
    scaleAboutPoint332 = NXOpen.Point3d(-159.95643931431721, 15.756902977231215, 0.0)
    viewCenter332 = NXOpen.Point3d(159.95643931431741, -15.756902977231338, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint332, viewCenter332)
    
    scaleAboutPoint333 = NXOpen.Point3d(-201.13925391389887, 20.292981107040191, 0.0)
    viewCenter333 = NXOpen.Point3d(201.1392539138991, -20.292981107040294, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint333, viewCenter333)
    
    rotMatrix56 = NXOpen.Matrix3x3()
    
    rotMatrix56.Xx = 0.99891115420881693
    rotMatrix56.Xy = -0.046335290562099986
    rotMatrix56.Xz = 0.0054357010343733282
    rotMatrix56.Yx = 0.02915123948463743
    rotMatrix56.Yy = 0.71088738018677655
    rotMatrix56.Yz = 0.70270145718341182
    rotMatrix56.Zx = -0.036424047464808651
    rotMatrix56.Zy = -0.70177786623667959
    rotMatrix56.Zz = 0.71146406460662104
    translation56 = NXOpen.Point3d(-263.7521235784194, 1.1270486101624613, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix56, translation56, 0.35463821844144544)
    
    scaleAboutPoint334 = NXOpen.Point3d(-250.6780019104971, 64.161631441377182, 0.0)
    viewCenter334 = NXOpen.Point3d(250.67800191049733, -64.16163144137731, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint334, viewCenter334)
    
    scaleAboutPoint335 = NXOpen.Point3d(-313.34750238812143, 80.20203930172147, 0.0)
    viewCenter335 = NXOpen.Point3d(313.3475023881216, -80.202039301721626, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint335, viewCenter335)
    
    scaleAboutPoint336 = NXOpen.Point3d(-391.68437798515174, 100.25254912715182, 0.0)
    viewCenter336 = NXOpen.Point3d(391.68437798515191, -100.25254912715192, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint336, viewCenter336)
    
    scaleAboutPoint337 = NXOpen.Point3d(-489.60547248143962, 125.31568640893981, 0.0)
    viewCenter337 = NXOpen.Point3d(489.60547248144013, -125.31568640894005, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint337, viewCenter337)
    
    scaleAboutPoint338 = NXOpen.Point3d(-389.35292335428773, 100.25254912715185, 0.0)
    viewCenter338 = NXOpen.Point3d(389.35292335428812, -100.25254912715214, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint338, viewCenter338)
    
    scaleAboutPoint339 = NXOpen.Point3d(-310.54975683108449, 79.269457449375807, 0.0)
    viewCenter339 = NXOpen.Point3d(310.54975683108489, -79.269457449376119, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint339, viewCenter339)
    
    scaleAboutPoint340 = NXOpen.Point3d(-248.43980546486753, 63.415565959500583, 0.0)
    viewCenter340 = NXOpen.Point3d(248.43980546486804, -63.415565959500967, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint340, viewCenter340)
    
    scaleAboutPoint341 = NXOpen.Point3d(-198.75184437189407, 50.135600382099298, 0.0)
    viewCenter341 = NXOpen.Point3d(198.75184437189446, -50.135600382099604, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint341, viewCenter341)
    
    scaleAboutPoint342 = NXOpen.Point3d(-158.52399358911421, 40.108480305679393, 0.0)
    viewCenter342 = NXOpen.Point3d(158.5239935891147, -40.10848030567972, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint342, viewCenter342)
    
    scaleAboutPoint343 = NXOpen.Point3d(-126.81919487129134, 32.08678424454348, 0.0)
    viewCenter343 = NXOpen.Point3d(126.81919487129177, -32.086784244543807, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint343, viewCenter343)
    
    scaleAboutPoint344 = NXOpen.Point3d(-104.51124011079905, 24.447073710128304, 0.0)
    viewCenter344 = NXOpen.Point3d(104.51124011079958, -24.447073710128667, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint344, viewCenter344)
    
    scaleAboutPoint345 = NXOpen.Point3d(-83.608992088639184, 19.557658968102597, 0.0)
    viewCenter345 = NXOpen.Point3d(83.608992088639681, -19.557658968102952, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint345, viewCenter345)
    
    scaleAboutPoint346 = NXOpen.Point3d(-66.887193670911302, 15.646127174482046, 0.0)
    viewCenter346 = NXOpen.Point3d(66.887193670911813, -15.646127174482412, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint346, viewCenter346)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies118 = [NXOpen.Body.Null] * 1 
    targetBodies118[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies118)
    
    targetBodies119 = []
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies119)
    
    direction32 = extrudeBuilder20.Direction
    
    success10 = direction32.ReverseDirection()
    
    extrudeBuilder20.Direction = direction32
    
    targetBodies120 = [NXOpen.Body.Null] * 1 
    targetBodies120[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies120)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies121 = [NXOpen.Body.Null] * 1 
    targetBodies121[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies121)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies122 = [NXOpen.Body.Null] * 1 
    targetBodies122[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies122)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies123 = [NXOpen.Body.Null] * 1 
    targetBodies123[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies123)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies124 = [NXOpen.Body.Null] * 1 
    targetBodies124[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies124)
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies125 = [NXOpen.Body.Null] * 1 
    targetBodies125[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies125)
    
    extrudeBuilder20.Limits.EndExtend.Value.SetFormula("20")
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies126 = [NXOpen.Body.Null] * 1 
    targetBodies126[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies126)
    
    extrudeBuilder20.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder20.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies127 = [NXOpen.Body.Null] * 1 
    targetBodies127[0] = body1
    extrudeBuilder20.BooleanOperation.SetTargetBodies(targetBodies127)
    
    markId319 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder20.ParentFeatureInternal = True
    
    feature30 = extrudeBuilder20.CommitFeature()
    
    theSession.DeleteUndoMark(markId319, None)
    
    theSession.SetUndoMarkName(markId297, "Extrude")
    
    expression180 = extrudeBuilder20.Limits.StartExtend.Value
    expression181 = extrudeBuilder20.Limits.EndExtend.Value
    extrudeBuilder20.Destroy()
    
    workPart.Expressions.Delete(expression173)
    
    workPart.Expressions.Delete(expression179)
    
    markId320 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder21 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section17 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder21.Section = section17
    
    extrudeBuilder21.AllowSelfIntersectingSection(True)
    
    expression182 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder21.DistanceTolerance = 0.01
    
    extrudeBuilder21.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies128 = [NXOpen.Body.Null] * 1 
    targetBodies128[0] = NXOpen.Body.Null
    extrudeBuilder21.BooleanOperation.SetTargetBodies(targetBodies128)
    
    extrudeBuilder21.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder21.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder21.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies129 = [NXOpen.Body.Null] * 1 
    targetBodies129[0] = NXOpen.Body.Null
    extrudeBuilder21.BooleanOperation.SetTargetBodies(targetBodies129)
    
    extrudeBuilder21.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder21.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder21.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder21.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder17 = extrudeBuilder21.SmartVolumeProfile
    
    smartVolumeProfileBuilder17.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder17.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId320, "Extrude Dialog")
    
    section17.DistanceTolerance = 0.01
    
    section17.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section17.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    extrudeBuilder21.Destroy()
    
    section17.Destroy()
    
    workPart.Expressions.Delete(expression182)
    
    theSession.UndoToMark(markId320, None)
    
    theSession.DeleteUndoMark(markId320, None)
    
    markId321 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder10 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression183 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression184 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData10 = edgeBlendBuilder10.LimitsListData
    
    origin17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal17 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane17 = workPart.Planes.CreatePlane(origin17, normal17, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder10 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression185 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression186 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId321, "Edge Blend Dialog")
    
    rotMatrix57 = NXOpen.Matrix3x3()
    
    rotMatrix57.Xx = 0.99835028018050243
    rotMatrix57.Xy = -0.055991255347469036
    rotMatrix57.Xz = 0.012716028787581407
    rotMatrix57.Yx = 0.04977347555631572
    rotMatrix57.Yy = 0.9543619462261731
    rotMatrix57.Yz = 0.29447559614751478
    rotMatrix57.Zx = -0.028623752279477874
    rotMatrix57.Zy = -0.29335687297215973
    rotMatrix57.Zz = 0.95557439578791448
    translation57 = NXOpen.Point3d(-67.269510782495786, -47.765893168275937, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix57, translation57, 1.6910468027183794)
    
    scCollector6 = workPart.ScCollectors.CreateCollector()
    
    seedEdges7 = [NXOpen.Edge.Null] * 1 
    extrude10 = feature30
    edge19 = extrude10.FindObject("EDGE * 130 * 140 {(-3.75,-6.4951905283833,65)(7.5,-0,65)(-3.75,6.4951905283833,65) EXTRUDE(2)}")
    seedEdges7[0] = edge19
    edgeMultipleSeedTangentRule7 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges7, 0.5, True)
    
    rules20 = [None] * 1 
    rules20[0] = edgeMultipleSeedTangentRule7
    scCollector6.ReplaceRules(rules20, False)
    
    scCollector6.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId322 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder10.Tolerance = 0.01
    
    edgeBlendBuilder10.AllInstancesOption = False
    
    edgeBlendBuilder10.RemoveSelfIntersection = True
    
    edgeBlendBuilder10.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder10.LimitFailingAreas = True
    
    edgeBlendBuilder10.ConvexConcaveY = False
    
    edgeBlendBuilder10.RollOverSmoothEdge = True
    
    edgeBlendBuilder10.RollOntoEdge = True
    
    edgeBlendBuilder10.MoveSharpEdge = True
    
    edgeBlendBuilder10.TrimmingOption = False
    
    edgeBlendBuilder10.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder10.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder10.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder10.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex5 = edgeBlendBuilder10.AddChainset(scCollector6, "7.5")
    
    feature31 = edgeBlendBuilder10.CommitFeature()
    
    theSession.DeleteUndoMark(markId322, None)
    
    theSession.SetUndoMarkName(markId321, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder10)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression186)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression185)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder10.Destroy()
    
    workPart.Expressions.Delete(expression183)
    
    workPart.Expressions.Delete(expression184)
    
    markId323 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder11 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression187 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression188 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    blendLimitsData11 = edgeBlendBuilder11.LimitsListData
    
    origin18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal18 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane18 = workPart.Planes.CreatePlane(origin18, normal18, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder11 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression189 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression190 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId323, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    scaleAboutPoint347 = NXOpen.Point3d(-59.611744534777081, 8.4489086742202346, 0.0)
    viewCenter347 = NXOpen.Point3d(59.611744534777564, -8.4489086742205952, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint347, viewCenter347)
    
    scaleAboutPoint348 = NXOpen.Point3d(-48.941085801780218, 4.7564226610424258, 0.0)
    viewCenter348 = NXOpen.Point3d(48.941085801780666, -4.7564226610427776, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint348, viewCenter348)
    
    scaleAboutPoint349 = NXOpen.Point3d(-61.332818523970161, 5.945528326303072, 0.0)
    viewCenter349 = NXOpen.Point3d(61.332818523970587, -5.9455283263034184, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint349, viewCenter349)
    
    scaleAboutPoint350 = NXOpen.Point3d(-77.252752924005847, 7.6274869975599229, 0.0)
    viewCenter350 = NXOpen.Point3d(77.252752924006245, -7.6274869975602568, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint350, viewCenter350)
    
    scaleAboutPoint351 = NXOpen.Point3d(-97.788294840513785, 10.023300221152507, 0.0)
    viewCenter351 = NXOpen.Point3d(97.788294840514155, -10.023300221152862, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint351, viewCenter351)
    
    scaleAboutPoint352 = NXOpen.Point3d(-128.652725399551, -7.3341221130387302, 0.0)
    viewCenter352 = NXOpen.Point3d(128.65272539955137, 7.334122113038366, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint352, viewCenter352)
    
    scaleAboutPoint353 = NXOpen.Point3d(-162.72583438304252, -12.605522381785164, 0.0)
    viewCenter353 = NXOpen.Point3d(162.72583438304298, 12.605522381784805, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint353, viewCenter353)
    
    scaleAboutPoint354 = NXOpen.Point3d(-204.83973870400604, -21.009203969641899, 0.0)
    viewCenter354 = NXOpen.Point3d(204.83973870400652, 21.009203969641494, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint354, viewCenter354)
    
    rotMatrix58 = NXOpen.Matrix3x3()
    
    rotMatrix58.Xx = 0.7778527332529841
    rotMatrix58.Xy = -0.62805336934999645
    rotMatrix58.Xz = 0.022228149247698694
    rotMatrix58.Yx = 0.38601013372540838
    rotMatrix58.Yy = 0.50539220646266403
    rotMatrix58.Yz = 0.77173498968758114
    rotMatrix58.Zx = -0.49592469391244604
    rotMatrix58.Zy = -0.59171588021187582
    rotMatrix58.Zz = 0.63555567425122572
    translation58 = NXOpen.Point3d(-250.73047451975796, -52.604702467721594, -75.967411774198339)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix58, translation58, 0.44329777305180695)
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder11)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression190)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression189)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder11.Destroy()
    
    workPart.Expressions.Delete(expression187)
    
    workPart.Expressions.Delete(expression188)
    
    theSession.UndoToMark(markId323, None)
    
    theSession.DeleteUndoMark(markId323, None)
    
    markId324 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId324, "Name Parts Dialog")
    
    markId325 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    theSession.DeleteUndoMark(markId325, None)
    
    markId326 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    workPart.AssignPermanentName("C:\\Users\\Reader\\Desktop\\嚴\身\\身體.prt")
    
    theSession.DeleteUndoMark(markId326, None)
    
    theSession.SetUndoMarkName(markId324, "Name Parts")
    
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()