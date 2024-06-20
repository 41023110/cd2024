# NX 1872
# Journal created by Admin on Thu Jun 20 17:29:01 2024 台北標準時間

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
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    scaleAboutPoint1 = NXOpen.Point3d(7.3746942234885831, 1.1799510757581844, 0.0)
    viewCenter1 = NXOpen.Point3d(-7.3746942234885831, -1.1799510757581844, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(5.663765163639245, -3.0678727969712445, 0.0)
    viewCenter2 = NXOpen.Point3d(-5.663765163639245, 3.0678727969712445, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(4.531012130911396, -2.4542982375769955, 0.0)
    viewCenter3 = NXOpen.Point3d(-4.531012130911396, 2.4542982375769955, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(3.6248097047291301, -1.9634385900616094, 0.0)
    viewCenter4 = NXOpen.Point3d(-3.6248097047291301, 1.9634385900615965, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(1.933231842522189, -0.4833079606305421, 0.0)
    viewCenter5 = NXOpen.Point3d(-1.933231842522189, 0.48330796063053177, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(2.416539803152749, -0.60413495078819046, 0.0)
    viewCenter6 = NXOpen.Point3d(-2.416539803152749, 0.60413495078817758, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(3.020674753940936, -0.75516868848523799, 0.0)
    viewCenter7 = NXOpen.Point3d(-3.020674753940904, 0.7551686884852058, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(3.7758434424261909, -0.94396086060654771, 0.0)
    viewCenter8 = NXOpen.Point3d(-3.7758434424261504, 0.94396086060652762, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(4.7198043030327126, -1.1799510757581846, 0.0)
    viewCenter9 = NXOpen.Point3d(-4.7198043030326877, 1.1799510757581593, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(5.899755378790859, -1.474938844697699, 0.0)
    viewCenter10 = NXOpen.Point3d(-5.899755378790859, 1.474938844697699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(7.3746942234885742, -1.8436735558721238, 0.0)
    viewCenter11 = NXOpen.Point3d(-7.3746942234885742, 1.8436735558721238, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(23.045919448401893, 3.4568879172602816, 0.0)
    viewCenter12 = NXOpen.Point3d(-23.045919448401893, -3.4568879172602816, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(18.436735558721473, 2.765510333808225, 0.0)
    viewCenter13 = NXOpen.Point3d(-18.436735558721473, -2.765510333808225, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(14.749388446977179, 2.2124082670465799, 0.0)
    viewCenter14 = NXOpen.Point3d(-14.749388446977179, -2.2124082670465799, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(11.799510757581745, 1.7699266136372642, 0.0)
    viewCenter15 = NXOpen.Point3d(-11.799510757581769, -1.7699266136372893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(9.4396086060653968, 1.4159412909097913, 0.0)
    viewCenter16 = NXOpen.Point3d(-9.4396086060654358, -1.4159412909098115, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-4.7198043030327419, -2.0767138933344005, 0.0)
    viewCenter17 = NXOpen.Point3d(4.7198043030326771, 2.0767138933343685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId9, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 5.5121448631627752, 0.0, ( 360.0 * math.pi/180.0 ))
    
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
    dimOrigin1 = NXOpen.Point3d(0.0, 0.0, 1.7125085219192677)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension1 = sketchDimensionalConstraint1.AssociatedDimension
    
    expression5 = sketchDimensionalConstraint1.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    scaleAboutPoint18 = NXOpen.Point3d(-1.3593036392734448, -0.75516868848524132, 0.0)
    viewCenter18 = NXOpen.Point3d(1.3593036392733804, 0.75516868848521557, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-1.3290968917340371, -0.84578893110346409, 0.0)
    viewCenter19 = NXOpen.Point3d(1.3290968917339856, 0.84578893110343323, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-1.9332318425222346, -0.96661592126110907, 0.0)
    viewCenter20 = NXOpen.Point3d(1.9332318425221686, 0.96661592126107609, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-2.7065245795310928, -1.0826098318124344, 0.0)
    viewCenter21 = NXOpen.Point3d(2.7065245795310466, 1.082609831812408, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(-3.3406246238783868, -1.1754049602535024, 0.0)
    viewCenter22 = NXOpen.Point3d(3.3406246238783237, 1.1754049602534813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-6.6812492477567353, -0.79185176269709723, 0.0)
    viewCenter23 = NXOpen.Point3d(6.6812492477566803, 0.79185176269707613, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-5.3449993982053883, -0.63348141015768111, 0.0)
    viewCenter24 = NXOpen.Point3d(5.3449993982053412, 0.63348141015766091, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(-4.2759995185643209, -0.50678512812614751, 0.0)
    viewCenter25 = NXOpen.Point3d(4.2759995185642667, 0.50678512812612597, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-3.420799614851461, -0.40542810250092021, 0.0)
    viewCenter26 = NXOpen.Point3d(3.4207996148514095, 0.40542810250089861, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId11, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 2.4567672942104113, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = arc2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = arc1
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = arc2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(0.0, 0.0, 0.22984900299264235)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension2 = sketchDimensionalConstraint2.AssociatedDimension
    
    expression6 = sketchDimensionalConstraint2.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId12, "Rapid Dimension Dialog")
    
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
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
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
    
    point4 = NXOpen.Point3d(0.0, 3.0538717397643738, 2.6985726532790952)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point4)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId13, None)
    
    theSession.SetUndoMarkName(markId12, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId12, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId14, "Rapid Dimension Dialog")
    
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
    
    theSession.SetUndoMarkVisibility(markId14, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.12211168746304409)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId14, "Edit Driving Value")
    
    scaleAboutPoint27 = NXOpen.Point3d(-4.7029659890105906, -1.2568271177528334, 0.0)
    viewCenter27 = NXOpen.Point3d(4.7029659890105409, 1.2568271177528128, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-3.7623727912084775, -1.0054616942022694, 0.0)
    viewCenter28 = NXOpen.Point3d(3.7623727912084277, 1.0054616942022472, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-3.0098982329667865, -0.80436935536181664, 0.0)
    viewCenter29 = NXOpen.Point3d(3.0098982329667381, 0.80436935536179566, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-2.4079185863734347, -0.64349548428945602, 0.0)
    viewCenter30 = NXOpen.Point3d(2.4079185863733845, 0.64349548428943482, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(-2.0508823821870328, -0.1826696858628212, 0.0)
    viewCenter31 = NXOpen.Point3d(2.0508823821869817, 0.18266968586279855, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-1.6407059057496309, -0.14613574869025925, 0.0)
    viewCenter32 = NXOpen.Point3d(1.640705905749581, 0.14613574869023657, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-1.3125647245997092, -0.11690859895220965, 0.0)
    viewCenter33 = NXOpen.Point3d(1.3125647245996599, 0.11690859895218746, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(-1.050051779679773, -0.093526879161769522, 0.0)
    viewCenter34 = NXOpen.Point3d(1.0500517796797231, 0.093526879161747775, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    point1_4 = NXOpen.Point3d(0.0, 0.66911961887608906, 0.073067950679355259)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc1, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    point1_5 = NXOpen.Point3d(0.0, 0.66911961887608906, 0.073067950679355259)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
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
    point5 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point5
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
    
    point6 = NXOpen.Point3d(0.0, 1.2476993252920714, 0.17963656532256272)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point6)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = False
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject4 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.SetUndoMarkName(markId16, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId16, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId18, "Rapid Dimension Dialog")
    
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
    expression8.SetFormula("1.2")
    
    theSession.SetUndoMarkVisibility(markId18, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId19, None)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId18, "Edit Driving Value")
    
    expression8.SetFormula("1.5")
    
    theSession.SetUndoMarkVisibility(markId20, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId21, None)
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId20, "Edit Driving Value")
    
    scaleAboutPoint35 = NXOpen.Point3d(-0.47613683936897955, 0.17344984862725121, 0.0)
    viewCenter35 = NXOpen.Point3d(0.47613683936892964, -0.17344984862727297, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-0.38090947149518917, 0.13875987890179867, 0.0)
    viewCenter36 = NXOpen.Point3d(0.38090947149513815, -0.13875987890182045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-0.30472757719615579, 0.1110079031214367, 0.0)
    viewCenter37 = NXOpen.Point3d(0.30472757719610566, -0.1110079031214586, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(-0.24378206175692996, 0.088806322497147275, 0.0)
    viewCenter38 = NXOpen.Point3d(0.24378206175687978, -0.088806322497168952, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-0.19502564940554856, 0.071045057997715585, 0.0)
    viewCenter39 = NXOpen.Point3d(0.19502564940549869, -0.071045057997737332, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(-0.24378206175692979, 0.088806322497147316, 0.0)
    viewCenter40 = NXOpen.Point3d(0.24378206175687975, -0.088806322497168994, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-0.30472757719615551, 0.11100790312143692, 0.0)
    viewCenter41 = NXOpen.Point3d(0.30472757719610616, -0.11100790312145864, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(-0.38090947149518889, 0.13875987890179872, 0.0)
    viewCenter42 = NXOpen.Point3d(0.38090947149513876, -0.13875987890182051, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(-0.47613683936897966, 0.1734498486272513, 0.0)
    viewCenter43 = NXOpen.Point3d(0.47613683936892981, -0.17344984862727245, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(-0.59517104921121822, 0.21681231078406704, 0.0)
    viewCenter44 = NXOpen.Point3d(0.59517104921116848, -0.21681231078408844, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(-0.74396381151401625, 0.27101538848008644, 0.0)
    viewCenter45 = NXOpen.Point3d(0.74396381151396684, -0.27101538848010776, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(-0.6177556649178928, 1.1890135916161007, 0.0)
    viewCenter46 = NXOpen.Point3d(0.61775566491784295, -1.1890135916161215, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(-0.77219458114736017, 1.4862669895201284, 0.0)
    viewCenter47 = NXOpen.Point3d(0.77219458114730921, -1.4862669895201495, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(-0.96524322643419314, 1.8578337369001621, 0.0)
    viewCenter48 = NXOpen.Point3d(0.96524322643414351, -1.8578337369001843, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(-0.86923785176197499, 2.8152927437663129, 0.0)
    viewCenter49 = NXOpen.Point3d(0.86923785176192958, -2.8152927437663342, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(-0.7265271596816536, 2.2626131544370716, 0.0)
    viewCenter50 = NXOpen.Point3d(0.72652715968160853, -2.2626131544370933, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(-0.58122172774532987, 1.8100905235496545, 0.0)
    viewCenter51 = NXOpen.Point3d(0.58122172774528313, -1.8100905235496765, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(-0.46497738219626616, 1.4480724188397216, 0.0)
    viewCenter52 = NXOpen.Point3d(0.46497738219622198, -1.4480724188397442, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId22, None)
    
    theSession.DeleteUndoMark(markId22, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    sketch2 = theSession.ActiveSketch
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    scaleAboutPoint53 = NXOpen.Point3d(30.973715738652121, 4.1298287651536327, 0.0)
    viewCenter53 = NXOpen.Point3d(-30.973715738652121, -4.1298287651536327, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(18.64322699697917, 3.539853227274528, 0.0)
    viewCenter54 = NXOpen.Point3d(-18.64322699697917, -3.539853227274528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(9.628400778186716, 3.020674753940936, 0.0)
    viewCenter55 = NXOpen.Point3d(-9.628400778186716, -3.020674753940936, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(5.7392820324877514, 2.5675735408497999, 0.0)
    viewCenter56 = NXOpen.Point3d(-5.7392820324877514, -2.5675735408497871, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(-3.3831557244138466, -0.96661592126108431, 0.0)
    viewCenter57 = NXOpen.Point3d(3.3831557244138466, 0.96661592126109463, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-3.5764789086660662, -2.1265550267744024, 0.0)
    viewCenter58 = NXOpen.Point3d(3.5764789086660662, 2.1265550267744189, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-3.402488042839058, -2.8611831269328407, 0.0)
    viewCenter59 = NXOpen.Point3d(3.4024880428390842, 2.8611831269328536, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(-3.2787612049176338, -2.660127015310529, 0.0)
    viewCenter60 = NXOpen.Point3d(3.27876120491766, 2.6601270153105445, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-2.6230089639341116, -2.1281016122484235, 0.0)
    viewCenter61 = NXOpen.Point3d(2.6230089639341285, 2.1281016122484404, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(-2.0984071711472922, -1.7024812897987385, 0.0)
    viewCenter62 = NXOpen.Point3d(2.0984071711472989, 1.702481289798752, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(-5.828028973450591, -0.76017769218920006, 0.0)
    viewCenter63 = NXOpen.Point3d(5.8280289734505972, 0.76017769218921893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(-4.687762435166781, -0.60814215375135794, 0.0)
    viewCenter64 = NXOpen.Point3d(4.6877624351667899, 0.60814215375137526, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(-3.9529239993838794, -0.42569950762594799, 0.0)
    viewCenter65 = NXOpen.Point3d(3.9529239993838865, 0.42569950762596526, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(-3.7948070394085232, -0.25947398560057244, 0.0)
    viewCenter66 = NXOpen.Point3d(3.7948070394085303, 0.25947398560059043, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("28")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId24, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.38538785997580899, 0.64252115965037349)
    section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId26, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId25, None)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.42667239211112012
    rotMatrix1.Xy = 0.90439508126791956
    rotMatrix1.Xz = 0.0044951961656929185
    rotMatrix1.Yx = -0.20944632837281887
    rotMatrix1.Yy = 0.093974216075686637
    rotMatrix1.Yz = 0.9732939341453366
    rotMatrix1.Zx = 0.87981981413316701
    rotMatrix1.Zy = -0.4162191534412536
    rotMatrix1.Zz = 0.22951843273978365
    translation1 = NXOpen.Point3d(-3.4491170110665754, -0.13188164233733324, -3.2484963450209667)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 20.393823505730197)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("5")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("1")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("1")
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.SetUndoMarkName(markId24, "Extrude")
    
    expression12 = extrudeBuilder1.Limits.StartExtend.Value
    expression13 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression9)
    
    workPart.Expressions.Delete(expression10)
    
    workPart.Expressions.Delete(expression11)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("1")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId28, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.74835894539034009
    rotMatrix2.Xy = 0.65891843234227765
    rotMatrix2.Xz = 0.076061740539234396
    rotMatrix2.Yx = -0.454105223811401
    rotMatrix2.Yy = 0.42537792984126688
    rotMatrix2.Yz = 0.78284229734421007
    rotMatrix2.Zx = 0.48347423360657077
    rotMatrix2.Zy = -0.62038706975851743
    rotMatrix2.Zz = 0.61755368116058384
    translation2 = NXOpen.Point3d(-3.6099602877061847, -0.0095521946180421868, -3.0503235547576701)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 20.393823505730197)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("0.8")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies4)
    
    targetBodies5 = []
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies5)
    
    extrudeBuilder2.Destroy()
    
    section2.Destroy()
    
    workPart.Expressions.Delete(expression14)
    
    theSession.UndoToMark(markId28, None)
    
    theSession.DeleteUndoMark(markId28, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrude1 = feature2
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(extrude1)
    
    section1.PrepareMappingData()
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId30, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("0.8")
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId31, None)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature3 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId32, None)
    
    theSession.SetUndoMarkName(markId30, "Extrude")
    
    section1.CleanMappingData()
    
    expression18 = extrudeBuilder3.Limits.StartExtend.Value
    expression19 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression15)
    
    workPart.Expressions.Delete(expression16)
    
    workPart.Expressions.Delete(expression17)
    
    theSession.DeleteUndoMark(markId30, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId29)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    scaleAboutPoint67 = NXOpen.Point3d(-2.0368707869645704, -0.15568439136034087, 0.0)
    viewCenter67 = NXOpen.Point3d(2.0368707869645806, 0.15568439136035858, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(-1.6294966295716546, -0.12454751308827093, 0.0)
    viewCenter68 = NXOpen.Point3d(1.6294966295716671, 0.12454751308828864, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-1.303597303657323, -0.099638010470615337, 0.0)
    viewCenter69 = NXOpen.Point3d(1.3035973036573358, 0.099638010470633032, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 3 
    objects1[0] = arc2
    objects1[1] = arc1
    objects1[2] = sketch2
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    theSession.SetUndoMarkName(markId34, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    extrude2 = feature3
    edge1 = extrude2.FindObject("EDGE * 130 * 140 {(0.8,-0.375,0.6495190528383)(0.8,0.75,-0)(0.8,-0.375,-0.6495190528383) EXTRUDE(2)}")
    seedEdges1[0] = edge1
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules2 = [None] * 1 
    rules2[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules2, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    seedEdges2 = [NXOpen.Edge.Null] * 2 
    seedEdges2[0] = edge1
    edge2 = extrude2.FindObject("EDGE * 120 * 140 {(0,-0.375,0.6495190528383)(0,0.75,-0)(0,-0.375,-0.6495190528383) EXTRUDE(2)}")
    seedEdges2[1] = edge2
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules3 = [None] * 1 
    rules3[0] = edgeMultipleSeedTangentRule2
    scCollector1.ReplaceRules(rules3, False)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId35, None)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    theSession.DeleteUndoMark(markId36, None)
    
    theSession.SetUndoMarkName(markId34, "Edge Blend")
    
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
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.54922262636615771
    rotMatrix3.Xy = 0.82417393859225885
    rotMatrix3.Xz = -0.13817317262328516
    rotMatrix3.Yx = -0.4227338752933702
    rotMatrix3.Yy = 0.41663252462840228
    rotMatrix3.Yz = 0.80480644263152745
    rotMatrix3.Zx = 0.72086793337400601
    rotMatrix3.Zy = -0.38360742741387083
    rotMatrix3.Zz = 0.57723025238287951
    translation3 = NXOpen.Point3d(-2.5363128160577992, 0.053873248958596853, -3.1452810346646451)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 39.831686534629299)
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId37, "Name Parts Dialog")
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    theSession.DeleteUndoMark(markId38, None)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    workPart.AssignPermanentName("C:\\Users\\Admin\\Desktop\\機器人組裝\車二.prt\\車二.prt")
    
    theSession.DeleteUndoMark(markId39, None)
    
    theSession.SetUndoMarkName(markId37, "Name Parts")
    
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()