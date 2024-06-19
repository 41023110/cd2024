# NX 1872
# Journal created by Reader on Wed Jun 19 19:19:51 2024 台北標準時間

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
    
    fileNew1.NewFileName = "C:\\Users\\Reader\\Desktop\\嚴\機\\機器人頭.prt"
    
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
    
    rotMatrix1.Xx = 0.98297274667391399
    rotMatrix1.Xy = 0.13466163894715377
    rotMatrix1.Xz = 0.1250232870004897
    rotMatrix1.Yx = 0.072002572837635365
    rotMatrix1.Yy = -0.90825736913899047
    rotMatrix1.Yz = 0.41217008735409222
    rotMatrix1.Zx = 0.1690568212202678
    rotMatrix1.Zy = -0.39614996453462525
    rotMatrix1.Zz = -0.90248822529610329
    translation1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.90572327300951838)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.99858329234048926
    rotMatrix2.Xy = 0.030117979540689038
    rotMatrix2.Xz = -0.043867021403480672
    rotMatrix2.Yx = 0.052788897015543387
    rotMatrix2.Yy = -0.66435565532543794
    rotMatrix2.Yz = 0.7455500624297392
    rotMatrix2.Zx = -0.0066888422248659422
    rotMatrix2.Zy = -0.74680952762099317
    rotMatrix2.Zz = -0.66500435250018708
    translation2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.90572327300951838)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.97689304507518315
    rotMatrix3.Xy = -0.13178493934165469
    rotMatrix3.Xz = -0.16826380551517689
    rotMatrix3.Yx = 0.062965725984065565
    rotMatrix3.Yy = -0.57488092460261064
    rotMatrix3.Yz = 0.81581078681232455
    rotMatrix3.Zx = -0.20424322714604914
    rotMatrix3.Zy = -0.80755473640537756
    rotMatrix3.Zz = -0.55329924261126584
    translation3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.90572327300951838)
    
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
    
    theSession.SetUndoMarkName(markId4, "Create Sketch Dialog")
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.95982419861217849
    rotMatrix4.Xy = -0.24392745638856084
    rotMatrix4.Xz = -0.13869716571832044
    rotMatrix4.Yx = 0.24084970940054393
    rotMatrix4.Yy = 0.46255654997569651
    rotMatrix4.Yz = 0.85324841374376659
    rotMatrix4.Zx = -0.14397543276601754
    rotMatrix4.Zy = -0.85237364699665974
    rotMatrix4.Zz = 0.50272282687923575
    translation4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.90572327300951838)
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, True)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = datumPlane1
    plane2.SetGeometry(geom1)
    
    plane2.SetFlip(True)
    
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
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Rectangle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId9, "Curve")
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId11, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(-42.357952452581053, 0.0, -37.000000000000064)
    endPoint1 = NXOpen.Point3d(-42.357952452581017, 0.0, 36.999999999999936)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(-42.357952452581017, 0.0, 36.999999999999936)
    endPoint2 = NXOpen.Point3d(42.357952452581102, 0.0, 37.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(42.357952452581102, 0.0, 37.0)
    endPoint3 = NXOpen.Point3d(42.357952452581067, 0.0, -37.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(42.357952452581067, 0.0, -37.0)
    endPoint4 = NXOpen.Point3d(-42.357952452581053, 0.0, -37.000000000000064)
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
    dimOrigin1 = NXOpen.Point3d(-32.421142537014887, 0.0, -6.871947331444581e-14)
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
    dimOrigin2 = NXOpen.Point3d(5.0133487731365649e-14, 0.0, 27.063190084433831)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression6 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = line1
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = -42.357952452581053
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = -37.000000000000064
    dimObject1_3.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis2 = workPart.Datums.FindObject("SKETCH(1:1B) X axis")
    dimObject2_3.Geometry = datumAxis2
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 28.574999999999999
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(-35.33156677792249, 0.0, -7.0263856746585445)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_3, dimObject2_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression7 = sketchDimensionalConstraint3.AssociatedExpression
    
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
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    theSession.SetUndoMarkName(markId12, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
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
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
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
    
    point3 = NXOpen.Point3d(-16.651057171014646, 0.0, 36.999999999999957)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point3)
    
    point1_1 = NXOpen.Point3d(-42.357952452581017, 0.0, 36.999999999999936)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(42.357952452581102, 0.0, 37.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line2, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
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
    
    point5 = NXOpen.Point3d(-19.280171461174856, 0.0, 57.840514383524578)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId13, None)
    
    theSession.SetUndoMarkName(markId12, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId12, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines5 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines8)
    
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
    
    expression8 = workPart.Expressions.FindObject("p0")
    expression8.SetFormula("45")
    
    theSession.SetUndoMarkVisibility(markId14, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.53118714898197439)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId14, "Edit Driving Value")
    
    point6 = NXOpen.Point3d(-22.500000000000544, 0.0, 9.6400857305874297)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line1, workPart.ModelingViews.WorkView, point6)
    
    point1_3 = NXOpen.Point3d(-22.50000000000054, 0.0, 19.653924512333017)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line1, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(-22.500000000000558, 0.0, -19.653924512333088)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line1, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
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
    
    point8 = NXOpen.Point3d(-41.773704832545533, 0.0, 7.0109714404272214)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point8)
    
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
    
    lines9 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines12)
    
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
    
    expression9 = workPart.Expressions.FindObject("p1")
    expression9.SetFormula("45")
    
    theSession.SetUndoMarkVisibility(markId18, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId19, None)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId18, "Edit Driving Value")
    
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId20, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId22, "Extrude Dialog")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 4 
    curves1[0] = line3
    curves1[1] = line1
    curves1[2] = line4
    curves1[3] = line2
    seedPoint1 = NXOpen.Point3d(-7.5, 0.0, 7.5)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch2, curves1, seedPoint1, 0.01)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId23, None)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId25, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId24, None)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.6984380549686422
    rotMatrix5.Xy = -0.68494391635242557
    rotMatrix5.Xz = 0.20745147582848791
    rotMatrix5.Yx = 0.32314839950766833
    rotMatrix5.Yy = 0.56046536582682716
    rotMatrix5.Yz = 0.76253110467982355
    rotMatrix5.Zx = -0.63856040847146878
    rotMatrix5.Zy = -0.46554312921618629
    rotMatrix5.Zz = 0.61278887030717821
    translation5 = NXOpen.Point3d(-12.141683382225368, 3.1055272168688877, -1.5784694196718938)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.90572327300951838)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("45/2")
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    section1.Clear()
    
    theSession.DeleteUndoMark(markId27, None)
    
    workPart.Expressions.Delete(expression11)
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    targetBodies3 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)
    
    theSession.DeleteUndoMark(markId26, None)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("45/2")
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies4)
    
    targetBodies5 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies5)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("22.5")
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies6)
    
    targetBodies7 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies7)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule1
    helpPoint2 = NXOpen.Point3d(-22.499999999999922, 1.0658141036401503e-14, 10.371623552486961)
    section1.AddToSection(rules2, line1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId29, None)
    
    direction3 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction3
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId28, None)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.52727907084848769
    rotMatrix6.Xy = -0.79173069721828859
    rotMatrix6.Xz = 0.30844656672979376
    rotMatrix6.Yx = 0.26260213385537362
    rotMatrix6.Yy = 0.49708065299869325
    rotMatrix6.Yz = 0.82701326694860022
    rotMatrix6.Zx = -0.80809461125524085
    rotMatrix6.Zy = -0.35506806037242289
    rotMatrix6.Zz = 0.47001039537823563
    translation6 = NXOpen.Point3d(-16.270225391585313, 1.0335210282063336, -0.50376803334795639)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.90572327300951838)
    
    scaleAboutPoint1 = NXOpen.Point3d(17.819552411085834, 0.87637143005340246, 0.0)
    viewCenter1 = NXOpen.Point3d(-17.819552411085834, -0.87637143005340246, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(20.448666701245948, 0.73030952504449154, 0.0)
    viewCenter2 = NXOpen.Point3d(-20.448666701246012, -0.73030952504449154, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(25.560833376557511, 0.91288690630561431, 0.0)
    viewCenter3 = NXOpen.Point3d(-25.560833376557511, -0.91288690630561431, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(37.08603056866604, 2.8527715822050688, 0.0)
    viewCenter4 = NXOpen.Point3d(-37.08603056866604, -2.8527715822050688, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(29.668824454932835, 2.2822172657640554, 0.0)
    viewCenter5 = NXOpen.Point3d(-29.668824454932835, -2.2822172657640554, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(23.735059563946265, 1.8257738126112439, 0.0)
    viewCenter6 = NXOpen.Point3d(-23.735059563946265, -1.8257738126112439, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(18.988047651157014, 1.4606190500889953, 0.0)
    viewCenter7 = NXOpen.Point3d(-18.988047651157039, -1.4606190500890202, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(15.190438120925533, 1.1684952400711963, 0.0)
    viewCenter8 = NXOpen.Point3d(-15.190438120925654, -1.1684952400712163, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("22.5")
    
    extrudeBuilder1.Limits.SymmetricOption = True
    
    extrudeBuilder1.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId30, None)
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId31, None)
    
    theSession.SetUndoMarkName(markId22, "Extrude")
    
    expression13 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression10)
    
    workPart.Expressions.Delete(expression12)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.34312363672661028
    rotMatrix7.Xy = 0.76806274597900537
    rotMatrix7.Xz = -0.54069010362562564
    rotMatrix7.Yx = -0.52246084048371499
    rotMatrix7.Yy = 0.63443436260695585
    rotMatrix7.Yz = 0.56967333596066294
    rotMatrix7.Zx = 0.78057724799058181
    rotMatrix7.Zy = 0.087021019200469341
    rotMatrix7.Zz = 0.61897213357045189
    translation7 = NXOpen.Point3d(-25.246642341288556, -0.25456239659092084, -0.50376803334795639)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 1.4151926140773723)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.78706568508393582
    rotMatrix8.Xy = 0.61313185988210384
    rotMatrix8.Xz = -0.067800661950039448
    rotMatrix8.Yx = -0.052392551610457541
    rotMatrix8.Yy = 0.17595662467556894
    rotMatrix8.Yz = 0.98300268909526234
    rotMatrix8.Zx = 0.61464024266158779
    rotMatrix8.Zy = -0.77013543525167472
    rotMatrix8.Zz = 0.17061296395822279
    translation8 = NXOpen.Point3d(-25.246642341288556, -0.25456239659092084, -0.50376803334795639)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 1.4151926140773723)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.89562474366715272
    rotMatrix9.Xy = 0.44410797182297618
    rotMatrix9.Xz = -0.024988555268952394
    rotMatrix9.Yx = -0.13266011134221639
    rotMatrix9.Yy = 0.32031037511216021
    rotMatrix9.Yz = 0.93797790936363612
    rotMatrix9.Zx = 0.42456756045394894
    rotMatrix9.Zy = -0.83676124011499819
    rotMatrix9.Zz = 0.34579331059375978
    translation9 = NXOpen.Point3d(-25.246642341288556, -0.25456239659092084, -0.50376803334795639)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 1.4151926140773723)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 5 
    objects1[0] = sketch2
    objects1[1] = line1
    objects1[2] = line2
    objects1[3] = line3
    objects1[4] = line4
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    scaleAboutPoint9 = NXOpen.Point3d(-53.657301424069722, -4.8609401986962313, 0.0)
    viewCenter9 = NXOpen.Point3d(53.657301424069594, 4.8609401986962002, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-45.468486781650732, -2.6922130331240641, 0.0)
    viewCenter10 = NXOpen.Point3d(45.468486781650626, 2.6922130331240388, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-36.374789425320571, -2.1537704264992619, 0.0)
    viewCenter11 = NXOpen.Point3d(36.374789425320486, 2.1537704264992317, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-23.930782516658294, -1.3401238209328834, 0.0)
    viewCenter12 = NXOpen.Point3d(23.930782516658194, 1.3401238209328505, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-29.913478145822864, -1.6751547761660939, 0.0)
    viewCenter13 = NXOpen.Point3d(29.913478145822744, 1.6751547761660632, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-37.391847682278573, -2.0939434702076167, 0.0)
    viewCenter14 = NXOpen.Point3d(37.391847682278446, 2.0939434702076043, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-46.739809602848197, -2.6174293377595217, 0.0)
    viewCenter15 = NXOpen.Point3d(46.739809602848069, 2.6174293377594897, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-58.42476200356024, -3.271786672199382, 0.0)
    viewCenter16 = NXOpen.Point3d(58.424762003560119, 3.271786672199362, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.9999576008698704
    rotMatrix10.Xy = -0.0062739433353437343
    rotMatrix10.Xz = -0.0067404820004030386
    rotMatrix10.Yx = -1.2084290311179029e-06
    rotMatrix10.Yy = -0.73207423794318305
    rotMatrix10.Yz = 0.68122486018820738
    rotMatrix10.Zx = -0.0092084993952630603
    rotMatrix10.Zy = -0.68119596870131793
    rotMatrix10.Zz = -0.73204320621392038
    translation10 = NXOpen.Point3d(-47.246696802872272, -1.0627871842433887, -0.50376803334795639)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 0.90572327300951838)
    
    scaleAboutPoint17 = NXOpen.Point3d(-44.402819122705786, 2.044866670124589, 0.0)
    viewCenter17 = NXOpen.Point3d(44.402819122705687, -2.0448666701246139, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-46.374654840325945, -16.797119076023556, 0.0)
    viewCenter18 = NXOpen.Point3d(46.374654840325817, 16.797119076023556, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-59.337648909865941, -21.909285751335055, 0.0)
    viewCenter19 = NXOpen.Point3d(59.337648909865635, 21.909285751335055, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-75.313169770214344, -27.386607189168817, 0.0)
    viewCenter20 = NXOpen.Point3d(75.313169770214103, 27.386607189168817, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-100.56019827272948, -30.667294508704682, 0.0)
    viewCenter21 = NXOpen.Point3d(100.560198272729, 30.667294508704682, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(-122.13428336315555, -18.721313508220867, 0.0)
    viewCenter22 = NXOpen.Point3d(122.13428336315494, 18.721313508220867, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-97.707426690524443, -14.977050806576695, 0.0)
    viewCenter23 = NXOpen.Point3d(97.707426690523945, 14.977050806576695, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-78.165941352419551, -11.981640645261356, 0.0)
    viewCenter24 = NXOpen.Point3d(78.165941352419111, 11.981640645261404, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(-62.532753081935716, -9.5853125162090453, 0.0)
    viewCenter25 = NXOpen.Point3d(62.532753081935255, 9.5853125162091235, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-49.661047703026377, -7.6682500129672375, 0.0)
    viewCenter26 = NXOpen.Point3d(49.661047703025879, 7.6682500129672997, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-39.728838162421155, -6.1346000103737648, 0.0)
    viewCenter27 = NXOpen.Point3d(39.728838162420629, 6.1346000103738394, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-32.717866721993936, -12.386049544754727, 0.0)
    viewCenter28 = NXOpen.Point3d(32.71786672199346, 12.386049544754805, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-26.361252616006567, -11.03059506627212, 0.0)
    viewCenter29 = NXOpen.Point3d(26.361252616006119, 11.030595066272216, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-21.089002092805281, -8.8244760530176976, 0.0)
    viewCenter30 = NXOpen.Point3d(21.089002092804858, 8.8244760530177739, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.997839557914874
    rotMatrix11.Xy = -0.053040151412609531
    rotMatrix11.Xz = -0.038768015146199701
    rotMatrix11.Yx = -0.034348349260422413
    rotMatrix11.Yy = -0.92420188673944126
    rotMatrix11.Yz = 0.38035649521250359
    rotMatrix11.Zx = -0.056003638840101566
    rotMatrix11.Zy = -0.37820313970852071
    rotMatrix11.Zz = -0.92402704373372158
    translation11 = NXOpen.Point3d(-22.724137174974796, -4.4797895152894975, -0.50376803334795639)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 2.211238459495894)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane4
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId33, "Create Sketch Dialog")
    
    scalar1 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 130 * 150 {(-22.5,-22.5,-22.5)(0,-22.5,-22.5)(22.5,-22.5,-22.5) EXTRUDE(2)}")
    point9 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge2 = extrude1.FindObject("EDGE * 120 * 150 {(-22.5,22.5,-22.5)(0,22.5,-22.5)(22.5,22.5,-22.5) EXTRUDE(2)}")
    direction4 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 150 {(0,-0,-22.5) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction4, point9, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane5.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom4 = [NXOpen.NXObject.Null] * 1 
    geom4[0] = face1
    plane5.SetGeometry(geom4)
    
    plane5.SetFlip(False)
    
    plane5.SetExpression(None)
    
    plane5.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane5.Evaluate()
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane6.SynchronizeToPlane(plane5)
    
    scalar2 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point10 = workPart.Points.CreatePoint(edge1, scalar2, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane6.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom5 = [NXOpen.NXObject.Null] * 1 
    geom5[0] = face1
    plane6.SetGeometry(geom5)
    
    plane6.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane6.Evaluate()
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId34, None)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
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
    feature3 = sketch3.Feature
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId36)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId35, None)
    
    theSession.SetUndoMarkName(markId33, "Create Sketch")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression15)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point10)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression14)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane4.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression17)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression16)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane6.DestroyPlane()
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId38, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(-0.50000000000000355, -0.5, -22.5)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 2.8799300204876626, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = arc1
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(-0.50000000000000355, -1.8567057804719638, -22.5)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension4 = sketchDimensionalConstraint4.AssociatedDimension
    
    expression18 = sketchDimensionalConstraint4.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines13 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines16)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines17 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines20)
    
    theSession.SetUndoMarkName(markId39, "Rapid Dimension Dialog")
    
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
    
    point1_5 = NXOpen.Point3d(-0.50000000000000355, -0.5, -22.5)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(-0.50000000000000355, -0.5, -22.5)
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
    
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    point11 = NXOpen.Point3d(-22.500000000000004, -19.030036535084555, -22.5)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(perpendicularDimension1, workPart.ModelingViews.WorkView, point11)
    
    line5 = theSession.ActiveSketch.FindObject("Curve DATUM5")
    point1_8 = NXOpen.Point3d(-22.500000000000004, -36.787500000000001, -22.5)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line5, NXOpen.View.Null, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    point1_9 = NXOpen.Point3d(-0.50000000000000355, -0.5, -22.5)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    point1_10 = NXOpen.Point3d(-22.500000000000004, -36.787500000000001, -22.5)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line5, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    point1_11 = NXOpen.Point3d(-0.50000000000000355, -0.5, -22.5)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
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
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometryFromLeader(True)
    
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
    sketchRapidDimensionBuilder4.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point13 = NXOpen.Point3d(-12.927686993336902, -37.576392985494707, -22.5)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point13)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = True
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject6 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId40, None)
    
    theSession.SetUndoMarkName(markId39, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId39, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder5 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines21 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines24)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId41, "Rapid Dimension Dialog")
    
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
    
    expression19 = workPart.Expressions.FindObject("p4")
    expression19.SetFormula("22.5")
    
    theSession.SetUndoMarkVisibility(markId41, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(1.0227272727272727)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId42, None)
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId41, "Edit Driving Value")
    
    point1_12 = NXOpen.Point3d(-3.5527136788005009e-15, 0.0, -22.5)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(-3.5527136788005009e-15, 0.0, -22.5)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    point1_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    point14 = NXOpen.Point3d(3.2255912054074201, -22.5, -22.5)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(edge1, workPart.ModelingViews.WorkView, point14)
    
    point1_15 = NXOpen.Point3d(3.2255912054074201, -22.5, -22.5)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge1, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(-3.5527136788005009e-15, 0.0, -22.5)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(3.2255912054074201, -22.5, -22.5)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge1, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    point1_18 = NXOpen.Point3d(-3.5527136788005009e-15, 0.0, -22.5)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
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
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point15 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point15
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
    
    point16 = NXOpen.Point3d(35.651801515479363, -14.124226119169617, -22.5)
    sketchRapidDimensionBuilder5.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point16)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.TextCentered = False
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject7 = sketchRapidDimensionBuilder5.Commit()
    
    theSession.DeleteUndoMark(markId44, None)
    
    theSession.SetUndoMarkName(markId43, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId43, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines25 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines25)
    
    lines26 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines26)
    
    lines27 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines27)
    
    lines28 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines28)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId45, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
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
    
    expression20 = workPart.Expressions.FindObject("p5")
    expression20.SetFormula("22.5")
    
    theSession.SetUndoMarkVisibility(markId45, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId46, None)
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId45, "Edit Driving Value")
    
    point1_19 = NXOpen.Point3d(-3.5527136788005009e-15, 0.0, -22.5)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    point1_20 = NXOpen.Point3d(-3.5527136788005009e-15, 0.0, -22.5)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    point1_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin5 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin5.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin5.View = NXOpen.View.Null
    assocOrigin5.ViewOfGeometry = workPart.ModelingViews.WorkView
    point17 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin5.PointOnGeometry = point17
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
    sketchRapidDimensionBuilder6.Origin.SetAssociativeOrigin(assocOrigin5)
    
    point18 = NXOpen.Point3d(15.310636376319842, -6.9449913641721412, -22.5)
    sketchRapidDimensionBuilder6.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point18)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.TextCentered = False
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject8 = sketchRapidDimensionBuilder6.Commit()
    
    theSession.DeleteUndoMark(markId48, None)
    
    theSession.SetUndoMarkName(markId47, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId47, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines29 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines32)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId49, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    expression21 = workPart.Expressions.FindObject("p6")
    expression21.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId49, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId50, None)
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId49, "Edit Driving Value")
    
    sketchRapidDimensionBuilder7.Destroy()
    
    theSession.UndoToMark(markId51, None)
    
    theSession.DeleteUndoMark(markId51, None)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies8)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("22.5")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("22.5")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("22.5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId52, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves2 = [NXOpen.ICurve.Null] * 1 
    curves2[0] = arc1
    seedPoint2 = NXOpen.Point3d(2.499999999999996, 2.0585385248258077e-16, -22.5)
    regionBoundaryRule2 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves2, seedPoint2, 0.01)
    
    section2.AllowSelfIntersection(True)
    
    rules3 = [None] * 1 
    rules3[0] = regionBoundaryRule2
    helpPoint3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section2.AddToSection(rules3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId53, None)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId55, None)
    
    direction5 = workPart.Directions.CreateDirection(theSession.ActiveSketch, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder2.Direction = direction5
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies10[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies10)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies11)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId54, None)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies12)
    
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = 0.88432436562808359
    rotMatrix12.Xy = 0.34130868675399012
    rotMatrix12.Xz = 0.31855736799319462
    rotMatrix12.Yx = -0.17510053693489125
    rotMatrix12.Yy = -0.3900501209535237
    rotMatrix12.Yz = 0.90399154039695073
    rotMatrix12.Zx = 0.43279350540598188
    rotMatrix12.Zy = -0.85520131167486246
    rotMatrix12.Zz = -0.28516749146421488
    translation12 = NXOpen.Point3d(31.877988074891618, -2.2261896128778211, -30.110604221557686)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation12, 2.211238459495894)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies13 = [NXOpen.Body.Null] * 1 
    targetBodies13[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies13)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies14 = [NXOpen.Body.Null] * 1 
    targetBodies14[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies14)
    
    direction6 = extrudeBuilder2.Direction
    
    success1 = direction6.ReverseDirection()
    
    extrudeBuilder2.Direction = direction6
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies15 = [NXOpen.Body.Null] * 1 
    targetBodies15[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies15)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies16 = [NXOpen.Body.Null] * 1 
    targetBodies16[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies16)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies17 = [NXOpen.Body.Null] * 1 
    targetBodies17[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies17)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies18 = [NXOpen.Body.Null] * 1 
    targetBodies18[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies18)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies19 = [NXOpen.Body.Null] * 1 
    targetBodies19[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies19)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("13")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies20 = [NXOpen.Body.Null] * 1 
    targetBodies20[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies20)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies21 = [NXOpen.Body.Null] * 1 
    targetBodies21[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies21)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies22 = [NXOpen.Body.Null] * 1 
    targetBodies22[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies22)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies23 = [NXOpen.Body.Null] * 1 
    targetBodies23[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies23)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies24 = [NXOpen.Body.Null] * 1 
    targetBodies24[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies24)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies25 = [NXOpen.Body.Null] * 1 
    targetBodies25[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies25)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    facesOfFeatures1 = [NXOpen.Face.Null] * 1 
    facesOfFeatures1[0] = face1
    edgeBoundaryRule1 = workPart.ScRuleFactory.CreateRuleEdgeBoundary(facesOfFeatures1)
    
    section2.AllowSelfIntersection(True)
    
    rules4 = [None] * 1 
    rules4[0] = edgeBoundaryRule1
    helpPoint4 = NXOpen.Point3d(2.5579385164746782, -7.1590400896184292, -22.499999999922693)
    section2.AddToSection(rules4, face1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint4, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId57, None)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies26 = [NXOpen.Body.Null] * 1 
    targetBodies26[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies26)
    
    workPart.Expressions.Delete(expression23)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId56, None)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("7.5")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies27 = [NXOpen.Body.Null] * 1 
    targetBodies27[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies27)
    
    targetBodies28 = []
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies28)
    
    extrudeBuilder2.Destroy()
    
    section2.Destroy()
    
    workPart.Expressions.Delete(expression22)
    
    workPart.Expressions.Delete(expression24)
    
    workPart.Expressions.Delete(expression25)
    
    theSession.UndoToMark(markId52, None)
    
    theSession.DeleteUndoMark(markId52, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder1.Tolerance = 0.01
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder1.Section = section3
    
    smartVolumeProfileBuilder3 = revolveBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId58, "Revolve Dialog")
    
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
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves3 = [NXOpen.ICurve.Null] * 1 
    curves3[0] = arc1
    seedPoint3 = NXOpen.Point3d(2.499999999999996, 2.0585385248258077e-16, -22.5)
    regionBoundaryRule3 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves3, seedPoint3, 0.01)
    
    section3.AllowSelfIntersection(False)
    
    rules5 = [None] * 1 
    rules5[0] = regionBoundaryRule3
    helpPoint5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section3.AddToSection(rules5, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint5, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId59, None)
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId61, None)
    
    revolveBuilder1.Section = section3
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId60, None)
    
    revolveBuilder1.Section = section3
    
    revolveBuilder1.Destroy()
    
    section3.Destroy()
    
    workPart.Expressions.Delete(expression26)
    
    theSession.UndoToMark(markId58, None)
    
    theSession.DeleteUndoMark(markId58, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section4 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section4
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies29 = [NXOpen.Body.Null] * 1 
    targetBodies29[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies29)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("22.5")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("22.5")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies30 = [NXOpen.Body.Null] * 1 
    targetBodies30[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies30)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("22.5")
    
    smartVolumeProfileBuilder4 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder4.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder4.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId62, "Extrude Dialog")
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    section4.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves4 = [NXOpen.ICurve.Null] * 1 
    curves4[0] = arc1
    seedPoint4 = NXOpen.Point3d(2.499999999999996, 2.0585385248258077e-16, -22.5)
    regionBoundaryRule4 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves4, seedPoint4, 0.01)
    
    section4.AllowSelfIntersection(True)
    
    rules6 = [None] * 1 
    rules6[0] = regionBoundaryRule4
    helpPoint6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section4.AddToSection(rules6, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint6, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId63, None)
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId65, None)
    
    direction7 = workPart.Directions.CreateDirection(theSession.ActiveSketch, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction7
    
    targetBodies31 = [NXOpen.Body.Null] * 1 
    targetBodies31[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies31)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies32 = [NXOpen.Body.Null] * 1 
    targetBodies32[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies32)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId64, None)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies33 = [NXOpen.Body.Null] * 1 
    targetBodies33[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies33)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies34 = [NXOpen.Body.Null] * 1 
    targetBodies34[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies34)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies35 = [NXOpen.Body.Null] * 1 
    targetBodies35[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies35)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies36 = [NXOpen.Body.Null] * 1 
    targetBodies36[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies36)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies37 = [NXOpen.Body.Null] * 1 
    targetBodies37[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies37)
    
    direction8 = extrudeBuilder3.Direction
    
    success2 = direction8.ReverseDirection()
    
    extrudeBuilder3.Direction = direction8
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies38 = [NXOpen.Body.Null] * 1 
    targetBodies38[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies38)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies39 = [NXOpen.Body.Null] * 1 
    targetBodies39[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies39)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies40 = [NXOpen.Body.Null] * 1 
    targetBodies40[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies40)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies41 = [NXOpen.Body.Null] * 1 
    targetBodies41[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies41)
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("8")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies42 = [NXOpen.Body.Null] * 1 
    targetBodies42[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies42)
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies43 = [NXOpen.Body.Null] * 1 
    targetBodies43[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies43)
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId66, None)
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder3.ParentFeatureInternal = False
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    feature4 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId67, None)
    
    theSession.SetUndoMarkName(markId62, "Extrude")
    
    expression29 = extrudeBuilder3.Limits.StartExtend.Value
    expression30 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression27)
    
    workPart.Expressions.Delete(expression28)
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = 0.95925343416563713
    rotMatrix13.Xy = 0.20979072792389414
    rotMatrix13.Xz = 0.18926357155721896
    rotMatrix13.Yx = 0.024167867472422631
    rotMatrix13.Yy = -0.7283153124335191
    rotMatrix13.Yz = 0.68481582915167849
    rotMatrix13.Zx = 0.2815115685425153
    rotMatrix13.Zy = -0.65233783896998332
    rotMatrix13.Zz = -0.70370915911667964
    translation13 = NXOpen.Point3d(31.877988074891618, -2.2261896128778211, -30.110604221557686)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation13, 2.211238459495894)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId69, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    extrude2 = feature4
    edge3 = extrude2.FindObject("EDGE * 130 * 140 {(-3.75,6.4951905283833,-15)(7.5,0,-15)(-3.75,-6.4951905283833,-15) EXTRUDE(2)}")
    seedEdges1[0] = edge3
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules7 = [None] * 1 
    rules7[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules7, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = 0.99743492712581117
    rotMatrix14.Xy = 0.050955154634692482
    rotMatrix14.Xz = 0.050270651136443342
    rotMatrix14.Yx = -0.06662750348479099
    rotMatrix14.Yy = 0.40425545721243922
    rotMatrix14.Yz = 0.91221614823096764
    rotMatrix14.Zx = 0.026159929833842462
    rotMatrix14.Zy = -0.91322565531751887
    rotMatrix14.Zz = 0.40661352724789207
    translation14 = NXOpen.Point3d(31.877988074891618, -2.2261896128778211, -30.110604221557686)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation14, 2.211238459495894)
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = 0.99743492712581117
    rotMatrix15.Xy = 0.050955154634692482
    rotMatrix15.Xz = 0.050270651136443342
    rotMatrix15.Yx = -0.051733796643029031
    rotMatrix15.Yy = 0.027813390196698991
    rotMatrix15.Yz = 0.99827352444641193
    rotMatrix15.Zx = 0.04946898457038626
    rotMatrix15.Zy = -0.99831357175083812
    rotMatrix15.Zz = 0.030378150431751388
    translation15 = NXOpen.Point3d(31.877988074891618, -5.1991165269966606, -33.255624854540464)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation15, 2.211238459495894)
    
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = 0.99743492712581117
    rotMatrix16.Xy = 0.050955154634692482
    rotMatrix16.Xz = 0.050270651136443342
    rotMatrix16.Yx = -0.010298637364079424
    rotMatrix16.Yy = -0.59284215172972998
    rotMatrix16.Yz = 0.80525283060719655
    rotMatrix16.Zx = 0.070834343492197152
    rotMatrix16.Zy = -0.80370501762065172
    rotMatrix16.Zz = -0.59079669974823978
    translation16 = NXOpen.Point3d(31.877988074891618, -12.193872555721279, -35.323003420300545)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation16, 2.211238459495894)
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId70, None)
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
        feature5 = edgeBlendBuilder1.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3620008)
        
    theSession.UndoToMarkWithStatus(markId71, None)
    
    theSession.DeleteUndoMark(markId71, None)
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression34)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression33)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    scCollector1.Destroy()
    
    workPart.Expressions.Delete(expression31)
    
    workPart.Expressions.Delete(expression32)
    
    theSession.UndoToMark(markId69, None)
    
    theSession.DeleteUndoMark(markId69, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder2 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData2 = edgeBlendBuilder2.LimitsListData
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder2 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId72, "Edge Blend Dialog")
    
    scCollector2 = workPart.ScCollectors.CreateCollector()
    
    seedEdges2 = [NXOpen.Edge.Null] * 1 
    seedEdges2[0] = edge3
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules8 = [None] * 1 
    rules8[0] = edgeMultipleSeedTangentRule2
    scCollector2.ReplaceRules(rules8, False)
    
    scCollector2.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId73, None)
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    csIndex2 = edgeBlendBuilder2.AddChainset(scCollector2, "15")
    
    try:
        # Unable to terminate the blend faces. Blend adjacent edges first or reduce the radius.
        feature6 = edgeBlendBuilder2.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3620008)
        
    theSession.UndoToMarkWithStatus(markId74, None)
    
    theSession.DeleteUndoMark(markId74, None)
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.98560732402822526
    rotMatrix17.Xy = 0.16041604350433422
    rotMatrix17.Xz = 0.053337564701934903
    rotMatrix17.Yx = 0.022046058049169915
    rotMatrix17.Yy = -0.43478595098058292
    rotMatrix17.Yz = 0.90026393249668502
    rotMatrix17.Zx = 0.16760720195269077
    rotMatrix17.Zy = -0.88613084237956619
    rotMatrix17.Zz = -0.43206475907815461
    translation17 = NXOpen.Point3d(31.907873453266287, -11.268041856835056, -33.776248350171144)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation17, 2.211238459495894)
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    csIndex3 = edgeBlendBuilder2.AddChainset(scCollector2, "15")
    
    try:
        # Unable to terminate the blend faces. Blend adjacent edges first or reduce the radius.
        feature7 = edgeBlendBuilder2.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3620008)
        
    theSession.UndoToMarkWithStatus(markId75, None)
    
    theSession.DeleteUndoMark(markId75, None)
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId76, None)
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
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
    
    csIndex4 = edgeBlendBuilder2.AddChainset(scCollector2, "15")
    
    try:
        # Unable to terminate the blend faces. Blend adjacent edges first or reduce the radius.
        feature8 = edgeBlendBuilder2.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3620008)
        
    theSession.UndoToMarkWithStatus(markId77, None)
    
    theSession.DeleteUndoMark(markId77, None)
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder2)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression38)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression37)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder2.Destroy()
    
    scCollector2.Destroy()
    
    workPart.Expressions.Delete(expression35)
    
    workPart.Expressions.Delete(expression36)
    
    theSession.UndoToMark(markId72, None)
    
    theSession.DeleteUndoMark(markId72, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = extrude2
    nErrs3 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs4 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId78, None)
    
    rotMatrix18 = NXOpen.Matrix3x3()
    
    rotMatrix18.Xx = 0.99672968220275593
    rotMatrix18.Xy = -0.032085770731374863
    rotMatrix18.Xz = -0.074164977803315171
    rotMatrix18.Yx = -0.014204476321867832
    rotMatrix18.Yy = -0.97306880876618451
    rotMatrix18.Yz = 0.23007678339801479
    rotMatrix18.Zx = -0.079549817525963198
    rotMatrix18.Zy = -0.22827088452741587
    rotMatrix18.Zz = -0.97034232609355575
    translation18 = NXOpen.Point3d(31.907873453266287, -11.268041856835056, -33.776248350171144)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix18, translation18, 2.211238459495894)
    
    # ----------------------------------------------
    #   Menu: Edit->Settings...
    # ----------------------------------------------
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId80, "Sketch Settings Dialog")
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Line...
    # ----------------------------------------------
    theSession.UndoToMark(markId80, None)
    
    theSession.DeleteUndoMark(markId80, None)
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    rotMatrix19 = NXOpen.Matrix3x3()
    
    rotMatrix19.Xx = 0.99909008451368531
    rotMatrix19.Xy = -0.042165519970586138
    rotMatrix19.Xz = -0.0064087402854150176
    rotMatrix19.Yx = -0.041473956004197454
    rotMatrix19.Yy = -0.99555532251150025
    rotMatrix19.Yz = 0.084554779831647081
    rotMatrix19.Zx = -0.0099455517593381535
    rotMatrix19.Zy = -0.084212046315396
    rotMatrix19.Zz = -0.99639822222621788
    translation19 = NXOpen.Point3d(31.907873453266287, -11.268041856835056, -33.776248350171144)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix19, translation19, 2.211238459495894)
    
    point19 = workPart.Points.CreatePoint(arc1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumAxis3 = workPart.Datums.FindObject("SKETCH(3:1B) X axis")
    direction9 = workPart.Directions.CreateDirection(datumAxis3, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane2 = workPart.Datums.FindObject("SKETCH(3:1B) XY plane")
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane2, direction9, point19, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem3
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature9 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
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
    
    nXObject9 = sketchInPlaceBuilder3.Commit()
    
    sketchInPlaceBuilder3.Destroy()
    
    sketch4 = nXObject9
    sketch4.Activate(NXOpen.Sketch.ViewReorient.FalseValue)
    
    theSession.SetUndoMarkVisibility(markId82, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint5 = NXOpen.Point3d(0.0, 0.0, -22.5)
    endPoint5 = NXOpen.Point3d(3.7897418701309821e-15, -7.4996640685028995, -22.5)
    line6 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line6
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys3 = feature9
    point20 = datumCsys3.FindObject("POINT 1")
    geom2_5.Geometry = point20
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    conGeom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_7.Geometry = line6
    conGeom1_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_7.SplineDefiningPointIndex = 0
    conGeom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_7.Geometry = arc1
    conGeom2_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_7.SplineDefiningPointIndex = 0
    help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help1.Point.X = -0.070984925206258029
    help1.Point.Y = -7.4996640685028995
    help1.Point.Z = -22.5
    help1.Parameter = 0.0
    sketchHelpedGeometricConstraint1 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_7, conGeom2_7, help1)
    
    geom6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom6.Geometry = line6
    geom6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateVerticalConstraint(geom6)
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = line6
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line6
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = 0.0
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 0.0
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(4.0701173414158927, -3.7498320342514475, -22.5)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_5, dimObject2_4, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint5
    dimension5 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression39 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId83, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint6 = NXOpen.Point3d(0.21363181661125494, 7.4969568123960393, -22.5)
    endPoint6 = NXOpen.Point3d(4.9960036108132044e-16, -8.8817841970012523e-16, -22.5)
    line7 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_8.Geometry = line7
    conGeom1_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_8.SplineDefiningPointIndex = 0
    conGeom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_8.Geometry = arc1
    conGeom2_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_8.SplineDefiningPointIndex = 0
    help2 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help2.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help2.Point.X = 0.21363181661125494
    help2.Point.Y = 7.4969568123960393
    help2.Point.Z = -22.5
    help2.Parameter = 0.0
    sketchHelpedGeometricConstraint2 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_8, conGeom2_8, help2)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line7
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = point20
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = line7
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimObject2_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_5.Geometry = line7
    dimObject2_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_5.AssocValue = 0
    dimObject2_5.HelpPoint.X = 0.0
    dimObject2_5.HelpPoint.Y = 0.0
    dimObject2_5.HelpPoint.Z = 0.0
    dimObject2_5.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(4.1752817656361776, 3.632544198002333, -22.5)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_6, dimObject2_5, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint4 = sketchDimensionalConstraint6
    dimension6 = sketchHelpedDimensionalConstraint4.AssociatedDimension
    
    expression40 = sketchHelpedDimensionalConstraint4.AssociatedExpression
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = line7
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = 0.21363181661125494
    dimObject1_7.HelpPoint.Y = 7.4969568123960393
    dimObject1_7.HelpPoint.Z = -22.5
    dimObject1_7.View = NXOpen.NXObject.Null
    dimObject2_6 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis4 = workPart.Datums.FindObject("SKETCH(4:1B) X axis")
    dimObject2_6.Geometry = datumAxis4
    dimObject2_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_6.AssocValue = 0
    dimObject2_6.HelpPoint.X = 28.574999999999999
    dimObject2_6.HelpPoint.Y = 0.0
    dimObject2_6.HelpPoint.Z = -22.5
    dimObject2_6.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(2.9187087045588287, 2.8367225227058945, -22.5)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_7, dimObject2_6, dimOrigin7, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension7 = sketchDimensionalConstraint7.AssociatedDimension
    
    expression41 = sketchDimensionalConstraint7.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    scaleAboutPoint31 = NXOpen.Point3d(-33.742403348488338, 29.434862495489671, 0.0)
    viewCenter31 = NXOpen.Point3d(33.742403348487919, -29.434862495489618, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-27.18536893892399, 23.547889996391742, 0.0)
    viewCenter32 = NXOpen.Point3d(27.185368938923567, -23.547889996391678, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-19.374361525486727, 17.919369948473733, 0.0)
    viewCenter33 = NXOpen.Point3d(19.374361525486297, -17.919369948473655, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(-14.645638900195076, 19.527518533593163, 0.0)
    viewCenter34 = NXOpen.Point3d(14.645638900194635, -19.527518533593089, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(-11.247467782829585, 22.494935565658785, 0.0)
    viewCenter35 = NXOpen.Point3d(11.247467782829146, -22.494935565658714, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-9.5723130066635331, 27.221265112698799, 0.0)
    viewCenter36 = NXOpen.Point3d(9.5723130066630748, -27.22126511269872, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint36, viewCenter36)
    
    rotMatrix20 = NXOpen.Matrix3x3()
    
    rotMatrix20.Xx = 0.99898701846088145
    rotMatrix20.Xy = 0.040102927991356958
    rotMatrix20.Xz = -0.020413037822870017
    rotMatrix20.Yx = 0.017401918177045915
    rotMatrix20.Yy = 0.07404958465575015
    rotMatrix20.Yz = 0.99710271900946479
    rotMatrix20.Zx = 0.041498315512768634
    rotMatrix20.Zy = -0.99644789837644132
    rotMatrix20.Zz = 0.073276705921948765
    translation20 = NXOpen.Point3d(30.383795670090546, -0.25265553293079318, -33.93250909701014)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix20, translation20, 1.4151926140773723)
    
    rotMatrix21 = NXOpen.Matrix3x3()
    
    rotMatrix21.Xx = 0.98604345033072083
    rotMatrix21.Xy = 0.16469461201464503
    rotMatrix21.Xz = -0.024372091277351647
    rotMatrix21.Yx = 0.059621582376545669
    rotMatrix21.Yy = -0.21263037145648017
    rotMatrix21.Yz = 0.97531204855122755
    rotMatrix21.Zx = 0.1554463926078791
    rotMatrix21.Zy = -0.96315316015035668
    rotMatrix21.Zz = -0.21948213849325551
    translation21 = NXOpen.Point3d(30.423111758285906, -0.38089776293677358, -34.278626381186541)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix21, translation21, 1.4151926140773723)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Revolve...
    # ----------------------------------------------
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    revolveBuilder2 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    
    revolveBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    revolveBuilder2.Limits.EndExtend.Value.SetFormula("360")
    
    revolveBuilder2.Tolerance = 0.01
    
    section5 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    revolveBuilder2.Section = section5
    
    smartVolumeProfileBuilder5 = revolveBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder5.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder5.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId84, "Revolve Dialog")
    
    section5.DistanceTolerance = 0.01
    
    section5.ChainingTolerance = 0.0094999999999999998
    
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
    
    section5.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = workPart.Features.FindObject("SKETCH(4)")
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section5.AllowSelfIntersection(False)
    
    rules9 = [None] * 1 
    rules9[0] = curveFeatureRule2
    helpPoint7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section5.AddToSection(rules9, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint7, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId85, None)
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId87, None)
    
    revolveBuilder2.Section = section5
    
    theSession.DeleteUndoMark(markId86, None)
    
    revolveBuilder2.Section = section5
    
    scaleAboutPoint37 = NXOpen.Point3d(-2.5505765517399487e-13, -15.891535264968324, 0.0)
    viewCenter37 = NXOpen.Point3d(-2.5505765517399487e-13, 15.89153526496842, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    rotMatrix22 = NXOpen.Matrix3x3()
    
    rotMatrix22.Xx = 0.99342868169098297
    rotMatrix22.Xy = 0.071675933762316957
    rotMatrix22.Xz = -0.089230123349762533
    rotMatrix22.Yx = 0.1026962086107021
    rotMatrix22.Yy = -0.9024021700966931
    rotMatrix22.Yz = 0.41847797091574324
    rotMatrix22.Zx = -0.050526657624476015
    rotMatrix22.Zy = -0.42489161432542988
    rotMatrix22.Zz = -0.90383304484026394
    translation22 = NXOpen.Point3d(30.40067911802911, 2.6665701128706423, -33.652983241105751)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix22, translation22, 1.7689907675967154)
    
    scaleAboutPoint38 = NXOpen.Point3d(31.857854225301036, -11.367121695412621, 0.0)
    viewCenter38 = NXOpen.Point3d(-31.857854225301562, 11.367121695412724, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(42.065828642563069, -12.713228211974656, 0.0)
    viewCenter39 = NXOpen.Point3d(-42.065828642563574, 12.713228211974752, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(53.049683899232321, -15.65783621695409, 0.0)
    viewCenter40 = NXOpen.Point3d(-53.049683899232839, 15.65783621695417, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(66.604228684058342, -19.280171461174803, 0.0)
    viewCenter41 = NXOpen.Point3d(-66.604228684058867, 19.280171461174906, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(83.985595380117445, -23.735059563946276, 0.0)
    viewCenter42 = NXOpen.Point3d(-83.985595380117942, 23.7350595639464, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(106.35132458460539, -28.755937548627227, 0.0)
    viewCenter43 = NXOpen.Point3d(-106.35132458460571, 28.755937548627305, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(133.50971004719781, -34.803813302902014, 0.0)
    viewCenter44 = NXOpen.Point3d(-133.50971004719821, 34.803813302902114, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(169.73990914120245, -40.651995046422414, 0.0)
    viewCenter45 = NXOpen.Point3d(-169.7399091412027, 40.651995046422535, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(135.79192731296195, -32.521596037137932, 0.0)
    viewCenter46 = NXOpen.Point3d(-135.79192731296214, 32.521596037138025, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(109.54642875667521, -26.017276829710344, 0.0)
    viewCenter47 = NXOpen.Point3d(-109.54642875667537, 26.017276829710422, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(88.367452530384639, -20.813821463768278, 0.0)
    viewCenter48 = NXOpen.Point3d(-88.367452530384767, 20.813821463768338, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(71.278209644343335, -17.23530479105024, 0.0)
    viewCenter49 = NXOpen.Point3d(-71.278209644343463, 17.235304791050289, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(57.256266763488853, -13.788243832840172, 0.0)
    viewCenter50 = NXOpen.Point3d(-57.256266763489009, 13.788243832840232, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(45.805013410791055, -11.030595066272138, 0.0)
    viewCenter51 = NXOpen.Point3d(-45.805013410791247, 11.030595066272202, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(36.64401072863285, -8.8244760530177242, 0.0)
    viewCenter52 = NXOpen.Point3d(-36.644010728633013, 8.8244760530177633, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(24.768359904741207, -6.5809651920810008, 0.0)
    viewCenter53 = NXOpen.Point3d(-24.768359904741377, 6.5809651920810417, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(19.814687923792945, -5.2647721536647927, 0.0)
    viewCenter54 = NXOpen.Point3d(-19.814687923793116, 5.2647721536648335, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(15.851750339034345, -4.2118177229318343, 0.0)
    viewCenter55 = NXOpen.Point3d(-15.851750339034513, 4.2118177229318663, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(12.681400271227442, -3.3694541783454617, 0.0)
    viewCenter56 = NXOpen.Point3d(-12.681400271227631, 3.3694541783454981, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(10.145120216981939, -2.6955633426763694, 0.0)
    viewCenter57 = NXOpen.Point3d(-10.145120216982123, 2.6955633426764032, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(8.1160961735855377, -2.1564506741410927, 0.0)
    viewCenter58 = NXOpen.Point3d(-8.1160961735857189, 2.1564506741411291, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features3 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature3 = feature3
    features3[0] = sketchFeature3
    curveFeatureRule3 = workPart.ScRuleFactory.CreateRuleCurveFeature(features3)
    
    section5.AllowSelfIntersection(False)
    
    rules10 = [None] * 1 
    rules10[0] = curveFeatureRule3
    helpPoint8 = NXOpen.Point3d(2.7301481417067524, -6.9834388817195689, -22.5)
    section5.AddToSection(rules10, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint8, NXOpen.Section.Mode.Create, False)
    
    theSession.UndoToMark(markId89, None)
    
    theSession.DeleteUndoMark(markId89, None)
    
    revolveBuilder2.Section = section5
    
    theSession.DeleteUndoMark(markId88, None)
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features4 = [NXOpen.Features.Feature.Null] * 1 
    features4[0] = sketchFeature3
    curveFeatureRule4 = workPart.ScRuleFactory.CreateRuleCurveFeature(features4)
    
    section5.AllowSelfIntersection(False)
    
    rules11 = [None] * 1 
    rules11[0] = curveFeatureRule4
    helpPoint9 = NXOpen.Point3d(-3.8117587152268828, -6.4575365238591518, -22.5)
    section5.AddToSection(rules11, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint9, NXOpen.Section.Mode.Create, False)
    
    theSession.UndoToMark(markId91, None)
    
    theSession.DeleteUndoMark(markId91, None)
    
    revolveBuilder2.Section = section5
    
    theSession.DeleteUndoMark(markId90, None)
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.ActiveSketch.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMarksUpToMark(markId93, None, True)
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    scaleAboutPoint59 = NXOpen.Point3d(-7.0762723030205565, 2.9726806021821521, 0.0)
    viewCenter59 = NXOpen.Point3d(7.0762723030205565, -2.9726806021821521, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(-5.6610178424164452, 2.37814448174572, 0.0)
    viewCenter60 = NXOpen.Point3d(5.6610178424164452, -2.3781444817457218, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-4.4874552394680158, 1.9163019302182913, 0.0)
    viewCenter61 = NXOpen.Point3d(4.4874552394680105, -1.9163019302182924, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(-3.5899641915744129, 1.5330415441746332, 0.0)
    viewCenter62 = NXOpen.Point3d(3.5899641915744089, -1.5330415441746332, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(-2.6778596181697907, 1.4028984490576499, 0.0)
    viewCenter63 = NXOpen.Point3d(2.6778596181697907, -1.4028984490576499, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(-3.3473245227122406, 1.7536230613220627, 0.0)
    viewCenter64 = NXOpen.Point3d(3.3473245227122366, -1.7536230613220627, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(-4.1841556533903006, 2.192028826652578, 0.0)
    viewCenter65 = NXOpen.Point3d(4.1841556533902953, -2.192028826652578, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(-5.2301945667378753, 2.7400360333157225, 0.0)
    viewCenter66 = NXOpen.Point3d(5.2301945667378691, -2.7400360333157225, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(-1.4109462278473304, 3.5112096967803677, 0.0)
    viewCenter67 = NXOpen.Point3d(1.4109462278473228, -3.5112096967803677, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(-1.7636827848091579, 4.2813063020558157, 0.0)
    viewCenter68 = NXOpen.Point3d(1.7636827848091532, -4.2813063020558157, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-2.1709454125990639, 5.2843167407449894, 0.0)
    viewCenter69 = NXOpen.Point3d(2.1709454125990524, -5.2843167407449929, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(-2.7136817657488224, 6.6053959259312398, 0.0)
    viewCenter70 = NXOpen.Point3d(2.7136817657488224, -6.6053959259312398, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-3.3921022071860274, 8.2567449074140491, 0.0)
    viewCenter71 = NXOpen.Point3d(3.3921022071860274, -8.2567449074140491, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(-4.2401277589825339, 10.32093113426756, 0.0)
    viewCenter72 = NXOpen.Point3d(4.2401277589825339, -10.32093113426756, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-5.3001596987281676, 12.901163917834451, 0.0)
    viewCenter73 = NXOpen.Point3d(5.3001596987281676, -12.901163917834451, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(-6.62519962341021, 16.126454897293065, 0.0)
    viewCenter74 = NXOpen.Point3d(6.62519962341021, -16.126454897293065, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    # ----------------------------------------------
    #   Menu: Edit->Settings...
    # ----------------------------------------------
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId95, "Sketch Settings Dialog")
    
    theSession.UndoToMark(markId95, None)
    
    theSession.DeleteUndoMark(markId95, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    theSession.DeleteUndoMark(markId96, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    theSession.DeleteUndoMark(markId97, None)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.UndoToMark(markId92, None)
    
    theSession.DeleteUndoMark(markId92, None)
    
    section5.DistanceTolerance = 0.01
    
    section5.ChainingTolerance = 0.0094999999999999998
    
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
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    rotMatrix23 = NXOpen.Matrix3x3()
    
    rotMatrix23.Xx = 0.99863379737500546
    rotMatrix23.Xy = 0.013129932427289201
    rotMatrix23.Xz = 0.050578094219031242
    rotMatrix23.Yx = -0.031842991921823056
    rotMatrix23.Yy = -0.61452970349211045
    rotMatrix23.Yz = 0.78825076428212681
    rotMatrix23.Zx = 0.041431420514401525
    rotMatrix23.Zy = -0.78878441186444959
    rotMatrix23.Zz = -0.61327203506584538
    translation23 = NXOpen.Point3d(32.267273766638773, -6.876393144517567, -31.525352250365003)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix23, translation23, 2.1619747127852915)
    
    scaleAboutPoint75 = NXOpen.Point3d(49.564062598100037, -23.619417485020584, 0.0)
    viewCenter75 = NXOpen.Point3d(-49.564062598100456, 23.619417485020644, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(61.955078247625089, -29.524271856275735, 0.0)
    viewCenter76 = NXOpen.Point3d(-61.955078247625508, 29.524271856275789, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(77.44384780953142, -36.905339820344651, 0.0)
    viewCenter77 = NXOpen.Point3d(-77.443847809531803, 36.905339820344736, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(96.804809761914314, -46.131674775430838, 0.0)
    viewCenter78 = NXOpen.Point3d(-96.804809761914726, 46.131674775430916, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(116.52430804674874, -57.963373746331492, 0.0)
    viewCenter79 = NXOpen.Point3d(-116.52430804674914, 57.96337374633157, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(93.219446437398972, -46.370698997065197, 0.0)
    viewCenter80 = NXOpen.Point3d(-93.21944643739937, 46.370698997065283, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(74.766776527226611, -37.287778574959617, 0.0)
    viewCenter81 = NXOpen.Point3d(-74.766776527227009, 37.287778574959717, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(59.966396723627177, -29.830222859967687, 0.0)
    viewCenter82 = NXOpen.Point3d(-59.966396723627597, 29.830222859967765, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(47.973117378901698, -23.864178287974138, 0.0)
    viewCenter83 = NXOpen.Point3d(-47.973117378902138, 23.864178287974223, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(38.378493903121331, -19.091342630379305, 0.0)
    viewCenter84 = NXOpen.Point3d(-38.378493903121786, 19.09134263037939, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(33.444116115577145, -11.278577800100985, 0.0)
    viewCenter85 = NXOpen.Point3d(-33.4441161155776, 11.278577800101072, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(41.805145144471467, -14.098222250126248, 0.0)
    viewCenter86 = NXOpen.Point3d(-41.805145144471936, 14.098222250126332, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(52.256431430589394, -17.622777812657819, 0.0)
    viewCenter87 = NXOpen.Point3d(-52.256431430589856, 17.622777812657905, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(65.320539288236802, -22.028472265822288, 0.0)
    viewCenter88 = NXOpen.Point3d(-65.320539288237271, 22.02847226582238, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(52.256431430589366, -17.622777812657809, 0.0)
    viewCenter89 = NXOpen.Point3d(-52.256431430589871, 17.622777812657912, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(41.805145144471453, -14.09822225012624, 0.0)
    viewCenter90 = NXOpen.Point3d(-41.80514514447195, 14.098222250126341, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(33.444116115577124, -11.27857780010098, 0.0)
    viewCenter91 = NXOpen.Point3d(-33.4441161155776, 11.278577800101079, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(26.75529289246164, -9.0228622400807712, 0.0)
    viewCenter92 = NXOpen.Point3d(-26.755292892462119, 9.0228622400808725, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(21.404234313969276, -7.2182897920646054, 0.0)
    viewCenter93 = NXOpen.Point3d(-21.404234313969752, 7.2182897920647129, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint93, viewCenter93)
    
    point21 = workPart.Points.CreatePoint(arc1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4, nXObject10 = workPart.Xforms.CreateExtractXform(arc1, NXOpen.SmartObject.UpdateOption.WithinModeling, False)
    
    arc2 = nXObject10
    point22 = workPart.Points.CreatePoint(arc2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    revolveBuilder2.Destroy()
    
    section5.Destroy()
    
    workPart.Points.DeletePoint(point22)
    
    workPart.Expressions.Delete(expression42)
    
    theSession.UndoToMark(markId84, None)
    
    theSession.DeleteUndoMark(markId84, None)
    
    scaleAboutPoint94 = NXOpen.Point3d(-5.3736157340928168, 4.691888364842085, 0.0)
    viewCenter94 = NXOpen.Point3d(5.3736157340923452, -4.6918883648419722, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-4.2988925872743033, 3.7535106918736796, 0.0)
    viewCenter95 = NXOpen.Point3d(4.2988925872738273, -3.7535106918735699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-3.4391140698194902, 3.0028085534989541, 0.0)
    viewCenter96 = NXOpen.Point3d(3.439114069819015, -3.0028085534988445, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(-2.7512912558556444, 2.4022468427991734, 0.0)
    viewCenter97 = NXOpen.Point3d(2.7512912558551612, -2.4022468427990633, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(-2.2010330046845605, 1.9217974742393518, 0.0)
    viewCenter98 = NXOpen.Point3d(2.2010330046840818, -1.9217974742392396, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-2.7512912558556444, 2.4022468427991734, 0.0)
    viewCenter99 = NXOpen.Point3d(2.7512912558551612, -2.4022468427990615, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(-3.4391140698194937, 3.0028085534989537, 0.0)
    viewCenter100 = NXOpen.Point3d(3.4391140698190168, -3.0028085534988418, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(-4.2988925872743069, 3.7535106918736778, 0.0)
    viewCenter101 = NXOpen.Point3d(4.2988925872738255, -3.7535106918735686, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(-5.3736157340928159, 4.6918883648420842, 0.0)
    viewCenter102 = NXOpen.Point3d(5.3736157340923443, -4.6918883648419714, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(-6.7170196676159666, 5.8648604560525861, 0.0)
    viewCenter103 = NXOpen.Point3d(6.7170196676154834, -5.8648604560524795, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(-8.3962745845198938, 7.331075570065722, 0.0)
    viewCenter104 = NXOpen.Point3d(8.3962745845194124, -7.3310755700656154, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(-10.49534323064981, 9.16384446258213, 0.0)
    viewCenter105 = NXOpen.Point3d(10.495343230649329, -9.1638444625820306, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(-13.119179038312211, 11.45480557822766, 0.0)
    viewCenter106 = NXOpen.Point3d(13.11917903831171, -11.454805578227544, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint106, viewCenter106)
    
    rotMatrix24 = NXOpen.Matrix3x3()
    
    rotMatrix24.Xx = 0.99920236453940325
    rotMatrix24.Xy = 0.00046827410484946187
    rotMatrix24.Xz = -0.039930131708119002
    rotMatrix24.Yx = 0.035101289283689829
    rotMatrix24.Yy = -0.4870750795641367
    rotMatrix24.Yz = 0.87265443696701028
    rotMatrix24.Zx = -0.019040330603424967
    rotMatrix24.Zy = -0.87335997594745995
    rotMatrix24.Zz = -0.48670300823352219
    translation24 = NXOpen.Point3d(-9.8042981834343532, 16.887171210780025, -31.341669306344613)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix24, translation24, 2.1619747127852929)
    
    scaleAboutPoint107 = NXOpen.Point3d(-3.1818904383968141, 0.85666281033759006, 0.0)
    viewCenter107 = NXOpen.Point3d(3.1818904383963025, -0.85666281033747527, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint107, viewCenter107)
    
    scaleAboutPoint108 = NXOpen.Point3d(-0.30595100369224609, -0.76487750922989783, 0.0)
    viewCenter108 = NXOpen.Point3d(0.30595100369172434, 0.76487750922998909, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint108, viewCenter108)
    
    scaleAboutPoint109 = NXOpen.Point3d(0.38243875461468801, -1.3385356411523537, 0.0)
    viewCenter109 = NXOpen.Point3d(-0.38243875461520976, 1.3385356411524516, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(0.47804844326844159, -1.9121937730748262, 0.0)
    viewCenter110 = NXOpen.Point3d(-0.4780484432689307, 1.9121937730749077, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint110, viewCenter110)
    
    scaleAboutPoint111 = NXOpen.Point3d(0.59756055408560294, -2.3902422163435326, 0.0)
    viewCenter111 = NXOpen.Point3d(-0.59756055408613784, 2.390242216343609, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint111, viewCenter111)
    
    scaleAboutPoint112 = NXOpen.Point3d(-1.9106653989712979e-13, -2.9878027704294148, 0.0)
    viewCenter112 = NXOpen.Point3d(-2.2291096321331808e-13, 2.9878027704295422, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint112, viewCenter112)
    
    scaleAboutPoint113 = NXOpen.Point3d(-0.29878027704320903, -2.3902422163435579, 0.0)
    viewCenter113 = NXOpen.Point3d(0.29878027704269949, 2.3902422163436596, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(-0.23902422163460799, -1.9121937730748257, 0.0)
    viewCenter114 = NXOpen.Point3d(0.23902422163411885, 1.9121937730749072, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint114, viewCenter114)
    
    scaleAboutPoint115 = NXOpen.Point3d(-0.19121937730771899, -1.5297550184598605, 0.0)
    viewCenter115 = NXOpen.Point3d(0.19121937730726246, 1.529755018459942, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(-0.15297550184620129, -1.2238040147678755, 0.0)
    viewCenter116 = NXOpen.Point3d(0.15297550184575781, 1.2238040147679667, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint116, viewCenter116)
    
    scaleAboutPoint117 = NXOpen.Point3d(-0.12238040147702363, -0.97904321181428988, 0.0)
    viewCenter117 = NXOpen.Point3d(0.1223804014765645, 0.97904321181437337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(-0.097904321181669002, -0.78323456945142367, 0.0)
    viewCenter118 = NXOpen.Point3d(0.097904321181201515, 0.78323456945150716, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint118, viewCenter118)
    
    scaleAboutPoint119 = NXOpen.Point3d(-0.078323456945388614, -0.62658765556113216, 0.0)
    viewCenter119 = NXOpen.Point3d(0.078323456944907791, 0.62658765556121898, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint119, viewCenter119)
    
    scaleAboutPoint120 = NXOpen.Point3d(-0.062658765556353635, -0.50127012444888974, 0.0)
    viewCenter120 = NXOpen.Point3d(0.062658765555883483, 0.50127012444898589, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(-0.050127012445125643, -0.40101609955910317, 0.0)
    viewCenter121 = NXOpen.Point3d(0.050127012444659766, 0.4010160995591972, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(-1.162946688721769, 0.28071126969144872, 0.0)
    viewCenter122 = NXOpen.Point3d(1.1629466887212903, -0.28071126969135984, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint122, viewCenter122)
    
    scaleAboutPoint123 = NXOpen.Point3d(-1.5539373857919365, 0.350889087114298, 0.0)
    viewCenter123 = NXOpen.Point3d(1.5539373857914534, -0.35088908711420397, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint123, viewCenter123)
    
    scaleAboutPoint124 = NXOpen.Point3d(-2.0050804977959751, 0.43861135889285657, 0.0)
    viewCenter124 = NXOpen.Point3d(2.0050804977954946, -0.43861135889276576, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint124, viewCenter124)
    
    scaleAboutPoint125 = NXOpen.Point3d(-2.506350622244915, 0.54826419861605713, 0.0)
    viewCenter125 = NXOpen.Point3d(2.5063506222444274, -0.54826419861597031, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint125, viewCenter125)
    
    scaleAboutPoint126 = NXOpen.Point3d(-3.1329382778060935, 0.68533024827005473, 0.0)
    viewCenter126 = NXOpen.Point3d(3.1329382778055841, -0.68533024826998801, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint126, viewCenter126)
    
    scaleAboutPoint127 = NXOpen.Point3d(-4.0385532487343374, 0.85666281033755798, 0.0)
    viewCenter127 = NXOpen.Point3d(4.0385532487338365, -0.85666281033749536, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint127, viewCenter127)
    
    scaleAboutPoint128 = NXOpen.Point3d(-5.3541425646098544, 1.0708285129219344, 0.0)
    viewCenter128 = NXOpen.Point3d(5.3541425646093321, -1.0708285129218822, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(-6.8838975830697269, 1.3385356411524179, 0.0)
    viewCenter129 = NXOpen.Point3d(6.8838975830692055, -1.3385356411523528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint129, viewCenter129)
    
    scaleAboutPoint130 = NXOpen.Point3d(-5.5071180664558597, 1.0708285129219344, 0.0)
    viewCenter130 = NXOpen.Point3d(5.5071180664553117, -1.0708285129218822, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint130, viewCenter130)
    
    scaleAboutPoint131 = NXOpen.Point3d(-4.4056944531647089, 0.85666281033754754, 0.0)
    viewCenter131 = NXOpen.Point3d(4.4056944531642088, -0.85666281033749536, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint131, viewCenter131)
    
    scaleAboutPoint132 = NXOpen.Point3d(-3.524555562531817, 0.68533024827004629, 0.0)
    viewCenter132 = NXOpen.Point3d(3.5245555625313076, -0.68533024826999622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(-2.8979679069706425, 0.54826419861604381, 0.0)
    viewCenter133 = NXOpen.Point3d(2.8979679069701483, -0.54826419861599041, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(-2.3183743255765568, 0.43861135889284575, 0.0)
    viewCenter134 = NXOpen.Point3d(2.3183743255760758, -0.43861135889278696, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint134, viewCenter134)
    
    scaleAboutPoint135 = NXOpen.Point3d(-4.6116851449304361, 2.0050804977957655, 0.0)
    viewCenter135 = NXOpen.Point3d(4.611685144929953, -2.00508049779571, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint135, viewCenter135)
    
    scaleAboutPoint136 = NXOpen.Point3d(-5.7646064311629797, 2.5063506222447014, 0.0)
    viewCenter136 = NXOpen.Point3d(5.7646064311624992, -2.5063506222446423, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint136, viewCenter136)
    
    scaleAboutPoint137 = NXOpen.Point3d(-7.2057580389536708, 3.132938277805863, 0.0)
    viewCenter137 = NXOpen.Point3d(7.2057580389531832, -3.132938277805803, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(-9.0071975486920373, 3.9161728472573198, 0.0)
    viewCenter138 = NXOpen.Point3d(9.0071975486915363, -3.9161728472572612, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint138, viewCenter138)
    
    scaleAboutPoint139 = NXOpen.Point3d(-11.258996935864984, 4.8952160590716494, 0.0)
    viewCenter139 = NXOpen.Point3d(11.258996935864483, -4.8952160590715872, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(-14.226721671677131, 6.1190200738395486, 0.0)
    viewCenter140 = NXOpen.Point3d(14.226721671676648, -6.1190200738395095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(-17.783402089596347, 7.6487750922994193, 0.0)
    viewCenter141 = NXOpen.Point3d(17.783402089595889, -7.6487750922993865, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint141, viewCenter141)
    
    rotMatrix25 = NXOpen.Matrix3x3()
    
    rotMatrix25.Xx = 0.98195415338647973
    rotMatrix25.Xy = -0.10297899039591904
    rotMatrix25.Xz = 0.15862335321155782
    rotMatrix25.Yx = -0.1889909680448506
    rotMatrix25.Yy = -0.56520251718844505
    rotMatrix25.Yz = 0.80301215965968697
    rotMatrix25.Zx = 0.0069609370426431437
    rotMatrix25.Zy = -0.81849950647564895
    rotMatrix25.Zz = -0.57446505834089312
    translation25 = NXOpen.Point3d(-27.29623420459113, 26.473610935833214, -31.420648156819549)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix25, translation25, 1.106931052946071)
    
    rotMatrix26 = NXOpen.Matrix3x3()
    
    rotMatrix26.Xx = 0.99472786223039922
    rotMatrix26.Xy = -0.067870842286567187
    rotMatrix26.Xz = 0.076876712142562781
    rotMatrix26.Yx = -0.01799281725418031
    rotMatrix26.Yy = -0.85353202788854055
    rotMatrix26.Yz = -0.5207296188001308
    rotMatrix26.Zx = 0.10095909384397309
    rotMatrix26.Zy = 0.51660103187642237
    rotMatrix26.Zz = -0.85025327710889487
    translation26 = NXOpen.Point3d(-27.335034345204537, 25.954204052806553, -31.706167558103594)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix26, translation26, 1.106931052946071)
    
    rotMatrix27 = NXOpen.Matrix3x3()
    
    rotMatrix27.Xx = 0.99907781167293785
    rotMatrix27.Xy = 0.023853432262742672
    rotMatrix27.Xz = 0.035700700162582651
    rotMatrix27.Yx = -0.037341515086712254
    rotMatrix27.Yy = 0.07230806384836215
    rotMatrix27.Yz = 0.99668307658629562
    rotMatrix27.Zx = 0.021192863747986103
    rotMatrix27.Zy = -0.99709706532101672
    rotMatrix27.Zz = 0.073132105496638039
    translation27 = NXOpen.Point3d(-27.348247316636247, 26.012975722472866, -31.463877634187039)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix27, translation27, 1.106931052946071)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = theSession.ActiveSketch
    nErrs5 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs6 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId99, None)
    
    rotMatrix28 = NXOpen.Matrix3x3()
    
    rotMatrix28.Xx = 0.99823075733095479
    rotMatrix28.Xy = 0.054728037227474088
    rotMatrix28.Xz = 0.023242139740009934
    rotMatrix28.Yx = 0.0057297385460070571
    rotMatrix28.Yy = -0.47761595854653577
    rotMatrix28.Yz = 0.8785500362744636
    rotMatrix28.Zx = 0.059182135942025052
    rotMatrix28.Zy = -0.87686249667943761
    rotMatrix28.Zz = -0.47708451735770735
    translation28 = NXOpen.Point3d(-27.348247316636247, 26.012975722472866, -31.463877634187039)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix28, translation28, 1.106931052946071)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete5 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = sketch3
    nErrs7 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    notifyOnDelete6 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id3 = theSession.NewestVisibleUndoMark
    
    nErrs8 = theSession.UpdateManager.DoUpdate(id3)
    
    theSession.DeleteUndoMark(markId101, None)
    
    rotMatrix29 = NXOpen.Matrix3x3()
    
    rotMatrix29.Xx = 0.59413671939447155
    rotMatrix29.Xy = -0.80435828741238724
    rotMatrix29.Xz = -0.0030502685432819317
    rotMatrix29.Yx = 0.76753344282680047
    rotMatrix29.Yy = 0.56806236712285385
    rotMatrix29.Yz = -0.29698074213863934
    rotMatrix29.Zx = 0.24061166391015285
    rotMatrix29.Zy = 0.17410598074101519
    rotMatrix29.Zz = 0.95487859681772913
    translation29 = NXOpen.Point3d(-27.348247316636247, 26.012975722472866, -31.463877634187039)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix29, translation29, 1.106931052946071)
    
    rotMatrix30 = NXOpen.Matrix3x3()
    
    rotMatrix30.Xx = 0.70932690952561572
    rotMatrix30.Xy = -0.21031407696853874
    rotMatrix30.Xz = 0.67277286245188983
    rotMatrix30.Yx = -0.52060677056798565
    rotMatrix30.Yy = 0.48715002610621394
    rotMatrix30.Yz = 0.7011800357279756
    rotMatrix30.Zx = -0.47520934950988614
    rotMatrix30.Zy = -0.84761597501084418
    rotMatrix30.Zz = 0.2360576900776658
    translation30 = NXOpen.Point3d(-27.348247316636247, 26.012975722472866, -31.463877634187039)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix30, translation30, 1.106931052946071)
    
    rotMatrix31 = NXOpen.Matrix3x3()
    
    rotMatrix31.Xx = 0.96785997269932711
    rotMatrix31.Xy = -0.25068634552194841
    rotMatrix31.Xz = -0.020085552402301747
    rotMatrix31.Yx = 0.086449895290754614
    rotMatrix31.Yy = 0.25664095245813157
    rotMatrix31.Yz = 0.96263276337635661
    rotMatrix31.Zx = -0.23616411423133904
    rotMatrix31.Zy = -0.93343011398295406
    rotMatrix31.Zz = 0.2700643135608507
    translation31 = NXOpen.Point3d(-27.348247316636247, 26.012975722472866, -31.463877634187039)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix31, translation31, 1.106931052946071)
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects5 = [NXOpen.DisplayableObject.Null] * 1 
    objects5[0] = body1
    theSession.DisplayManager.BlankObjects(objects5)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show")
    
    objects6 = [NXOpen.DisplayableObject.Null] * 5 
    objects6[0] = sketch2
    objects6[1] = line1
    objects6[2] = line2
    objects6[3] = line3
    objects6[4] = line4
    theSession.DisplayManager.ShowObjects(objects6, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show")
    
    objects7 = [NXOpen.DisplayableObject.Null] * 1 
    objects7[0] = body1
    theSession.DisplayManager.ShowObjects(objects7, NXOpen.DisplayManager.LayerSetting.ChangeLayerToSelectable)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly)
    
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects8 = [NXOpen.DisplayableObject.Null] * 5 
    objects8[0] = sketch2
    objects8[1] = line1
    objects8[2] = line2
    objects8[3] = line3
    objects8[4] = line4
    theSession.DisplayManager.BlankObjects(objects8)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder4.PlaneReference = plane9
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId107, "Create Sketch Dialog")
    
    scalar3 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge4 = extrude1.FindObject("EDGE * 130 * 140 {(-22.5,-22.5,22.5)(-22.5,-22.5,0)(-22.5,-22.5,-22.5) EXTRUDE(2)}")
    point23 = workPart.Points.CreatePoint(edge4, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction10 = workPart.Directions.CreateDirection(edge1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face2 = extrude1.FindObject("FACE 130 {(0,-22.5,0) EXTRUDE(2)}")
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(face2, direction10, point23, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder4.Csystem = cartesianCoordinateSystem4
    
    origin10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal10 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane10 = workPart.Planes.CreatePlane(origin10, normal10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane10.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom7 = [NXOpen.NXObject.Null] * 1 
    geom7[0] = face2
    plane10.SetGeometry(geom7)
    
    plane10.SetFlip(False)
    
    plane10.SetExpression(None)
    
    plane10.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane10.Evaluate()
    
    origin11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane11 = workPart.Planes.CreatePlane(origin11, normal11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane11.SynchronizeToPlane(plane10)
    
    scalar4 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point24 = workPart.Points.CreatePoint(edge4, scalar4, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane11.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom8 = [NXOpen.NXObject.Null] * 1 
    geom8[0] = face2
    plane11.SetGeometry(geom8)
    
    plane11.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane11.Evaluate()
    
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId108, None)
    
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
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
    
    nXObject11 = sketchInPlaceBuilder4.Commit()
    
    sketch5 = nXObject11
    feature10 = sketch5.Feature
    
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId110)
    
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId109, None)
    
    theSession.SetUndoMarkName(markId107, "Create Sketch")
    
    sketchInPlaceBuilder4.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression44)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point24)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression43)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane9.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression46)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression45)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane11.DestroyPlane()
    
    scaleAboutPoint142 = NXOpen.Point3d(54.258498310998668, -29.160955039391514, 0.0)
    viewCenter142 = NXOpen.Point3d(-54.258498310999151, 29.160955039391531, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint142, viewCenter142)
    
    scaleAboutPoint143 = NXOpen.Point3d(67.823122888748372, -36.451193799239391, 0.0)
    viewCenter143 = NXOpen.Point3d(-67.823122888748884, 36.451193799239412, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint143, viewCenter143)
    
    scaleAboutPoint144 = NXOpen.Point3d(84.778903610935544, -45.563992249049207, 0.0)
    viewCenter144 = NXOpen.Point3d(-84.778903610936055, 45.563992249049271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(119.97895500005758, -56.021301945552274, 0.0)
    viewCenter145 = NXOpen.Point3d(-119.97895500005805, 56.021301945552352, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint145, viewCenter145)
    
    scaleAboutPoint146 = NXOpen.Point3d(95.983164000046045, -44.817041556441815, 0.0)
    viewCenter146 = NXOpen.Point3d(-95.9831640000465, 44.817041556441872, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint146, viewCenter146)
    
    scaleAboutPoint147 = NXOpen.Point3d(76.786531200036805, -35.853633245153453, 0.0)
    viewCenter147 = NXOpen.Point3d(-76.786531200037231, 35.853633245153532, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint147, viewCenter147)
    
    scaleAboutPoint148 = NXOpen.Point3d(61.429224960029394, -28.682906596122741, 0.0)
    viewCenter148 = NXOpen.Point3d(-61.429224960029799, 28.682906596122841, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(37.861436706881875, -22.946325276898175, 0.0)
    viewCenter149 = NXOpen.Point3d(-37.861436706882266, 22.946325276898289, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Rectangle...
    # ----------------------------------------------
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId112, "Create Rectangle")
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId114, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(-0.50000000000000355, -22.5, -0.5)
    arc3 = workPart.Curves.CreateArc(center2, nXMatrix2, 5.306627083720282, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_8.Geometry = arc3
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = 0.0
    dimObject1_8.HelpPoint.Y = 0.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(-0.50000000000000355, -22.5, 1.2345253752615983)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_8, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension8 = sketchDimensionalConstraint8.AssociatedDimension
    
    expression47 = sketchDimensionalConstraint8.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines33 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines36)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines37 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines40)
    
    theSession.SetUndoMarkName(markId115, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    point1_22 = NXOpen.Point3d(-0.50000000000000355, -22.5, -0.5)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(-0.50000000000000355, -22.5, -0.5)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc3, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    point1_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    edge5 = extrude1.FindObject("EDGE * 130 * 170 {(22.5,-22.5,22.5)(0,-22.5,22.5)(-22.5,-22.5,22.5) EXTRUDE(2)}")
    point25 = NXOpen.Point3d(15.206967303650584, -22.5, 22.5)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(edge5, workPart.ModelingViews.WorkView, point25)
    
    point1_25 = NXOpen.Point3d(15.206967303650584, -22.5, 22.5)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge5, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(-0.50000000000000355, -22.5, -0.5)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    point1_27 = NXOpen.Point3d(15.206967303650584, -22.5, 22.5)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge5, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    point1_28 = NXOpen.Point3d(-0.50000000000000355, -22.5, -0.5)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin6 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin6.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin6.View = NXOpen.View.Null
    assocOrigin6.ViewOfGeometry = workPart.ModelingViews.WorkView
    point26 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin6.PointOnGeometry = point26
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
    sketchRapidDimensionBuilder8.Origin.SetAssociativeOrigin(assocOrigin6)
    
    point27 = NXOpen.Point3d(36.9294885657809, -22.5, 14.618475071884166)
    sketchRapidDimensionBuilder8.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point27)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.TextCentered = False
    
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject12 = sketchRapidDimensionBuilder8.Commit()
    
    theSession.DeleteUndoMark(markId116, None)
    
    theSession.SetUndoMarkName(markId115, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId115, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder9 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder9.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId117, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder9.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder9.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    expression48 = workPart.Expressions.FindObject("p4")
    expression48.SetFormula("22.5")
    
    theSession.SetUndoMarkVisibility(markId117, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId118, None)
    
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId117, "Edit Driving Value")
    
    edge6 = extrude1.FindObject("EDGE * 130 * 160 {(22.5,-22.5,-22.5)(22.5,-22.5,0)(22.5,-22.5,22.5) EXTRUDE(2)}")
    point28 = NXOpen.Point3d(22.500000000000004, -22.5, 17.525009606957944)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(edge6, workPart.ModelingViews.WorkView, point28)
    
    point1_29 = NXOpen.Point3d(-0.50000000000000355, -22.5, 0.0)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin7 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin7.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin7.View = NXOpen.View.Null
    assocOrigin7.ViewOfGeometry = workPart.ModelingViews.WorkView
    point29 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin7.PointOnGeometry = point29
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
    sketchRapidDimensionBuilder9.Origin.SetAssociativeOrigin(assocOrigin7)
    
    point30 = NXOpen.Point3d(11.229604255654882, -22.5, 32.975535293402757)
    sketchRapidDimensionBuilder9.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point30)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.TextCentered = True
    
    sketchRapidDimensionBuilder9.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.TextCentered = True
    
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject13 = sketchRapidDimensionBuilder9.Commit()
    
    theSession.DeleteUndoMark(markId120, None)
    
    theSession.SetUndoMarkName(markId119, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId119, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder9.Destroy()
    
    markId121 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder10 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines45 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBelow(lines48)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder10.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId121, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder10.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder10.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits271 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits272 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits273 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits274 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits275 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits276 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits277 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits278 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    expression49 = workPart.Expressions.FindObject("p5")
    expression49.SetFormula("22.5")
    
    theSession.SetUndoMarkVisibility(markId121, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId122 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId122, None)
    
    markId123 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId121, "Edit Driving Value")
    
    point1_30 = NXOpen.Point3d(3.6649399439519947, -22.5, 3.8377736010477217)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc3, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(3.6649399439519947, -22.5, 3.8377736010477217)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc3, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    point1_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder10.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    dimensionlinearunits279 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits280 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits281 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits282 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits283 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits284 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometryFromLeader(True)
    
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
    sketchRapidDimensionBuilder10.Origin.SetAssociativeOrigin(assocOrigin8)
    
    point32 = NXOpen.Point3d(17.195648827648419, -22.5, 9.4173080091205765)
    sketchRapidDimensionBuilder10.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point32)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.TextCentered = False
    
    markId124 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject14 = sketchRapidDimensionBuilder10.Commit()
    
    theSession.DeleteUndoMark(markId124, None)
    
    theSession.SetUndoMarkName(markId123, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId123, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder10.Destroy()
    
    markId125 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder11 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines49 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBefore(lines49)
    
    lines50 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAfter(lines50)
    
    lines51 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAbove(lines51)
    
    lines52 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBelow(lines52)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder11.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId125, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder11.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits285 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits286 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits287 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits288 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits289 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits290 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits291 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits292 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits293 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits294 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder11.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits295 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits296 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits297 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits298 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits299 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits300 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits301 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits302 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits303 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits304 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    expression50 = workPart.Expressions.FindObject("p6")
    expression50.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId125, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId126 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId126, None)
    
    markId127 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId125, "Edit Driving Value")
    
    sketchRapidDimensionBuilder11.Destroy()
    
    theSession.UndoToMark(markId127, None)
    
    theSession.DeleteUndoMark(markId127, None)
    
    sketchRapidDimensionBuilder11.Destroy()
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch6 = theSession.ActiveSketch
    
    markId128 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId129 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder4 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section6 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder4.Section = section6
    
    extrudeBuilder4.AllowSelfIntersectingSection(True)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder4.DistanceTolerance = 0.01
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies44 = [NXOpen.Body.Null] * 1 
    targetBodies44[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies44)
    
    extrudeBuilder4.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("7.5")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies45 = [NXOpen.Body.Null] * 1 
    targetBodies45[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies45)
    
    extrudeBuilder4.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder4.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder6 = extrudeBuilder4.SmartVolumeProfile
    
    smartVolumeProfileBuilder6.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder6.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId129, "Extrude Dialog")
    
    section6.DistanceTolerance = 0.01
    
    section6.ChainingTolerance = 0.0094999999999999998
    
    section6.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId130 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId131 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features5 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature4 = feature10
    features5[0] = sketchFeature4
    curveFeatureRule5 = workPart.ScRuleFactory.CreateRuleCurveFeature(features5)
    
    section6.AllowSelfIntersection(True)
    
    rules12 = [None] * 1 
    rules12[0] = curveFeatureRule5
    helpPoint10 = NXOpen.Point3d(-4.6536170137440109, -22.5, -1.7897465126897141)
    section6.AddToSection(rules12, arc3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint10, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId131, None)
    
    direction11 = workPart.Directions.CreateDirection(sketch6, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder4.Direction = direction11
    
    targetBodies46 = [NXOpen.Body.Null] * 1 
    targetBodies46[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies46)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies47 = [NXOpen.Body.Null] * 1 
    targetBodies47[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies47)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId130, None)
    
    rotMatrix32 = NXOpen.Matrix3x3()
    
    rotMatrix32.Xx = 0.53596588627742003
    rotMatrix32.Xy = -0.82156529772320797
    rotMatrix32.Xz = 0.19434770470430573
    rotMatrix32.Yx = 0.18569943530175909
    rotMatrix32.Yy = 0.33929151029656573
    rotMatrix32.Yz = 0.92216971906980461
    rotMatrix32.Zx = -0.82356316605070612
    rotMatrix32.Zy = -0.45816125176366457
    rotMatrix32.Zz = 0.33441288687322468
    translation32 = NXOpen.Point3d(-27.079672137127993, 25.631009297936195, -22.840039942541512)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix32, translation32, 1.106931052946071)
    
    direction12 = extrudeBuilder4.Direction
    
    success3 = direction12.ReverseDirection()
    
    extrudeBuilder4.Direction = direction12
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies48 = [NXOpen.Body.Null] * 1 
    targetBodies48[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies48)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies49 = [NXOpen.Body.Null] * 1 
    targetBodies49[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies49)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies50 = [NXOpen.Body.Null] * 1 
    targetBodies50[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies50)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies51 = [NXOpen.Body.Null] * 1 
    targetBodies51[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies51)
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("9")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies52 = [NXOpen.Body.Null] * 1 
    targetBodies52[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies52)
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("10")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies53 = [NXOpen.Body.Null] * 1 
    targetBodies53[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies53)
    
    markId132 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId132, None)
    
    markId133 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder4.ParentFeatureInternal = False
    
    feature11 = extrudeBuilder4.CommitFeature()
    
    theSession.DeleteUndoMark(markId133, None)
    
    theSession.SetUndoMarkName(markId129, "Extrude")
    
    expression53 = extrudeBuilder4.Limits.StartExtend.Value
    expression54 = extrudeBuilder4.Limits.EndExtend.Value
    extrudeBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression51)
    
    workPart.Expressions.Delete(expression52)
    
    rotMatrix33 = NXOpen.Matrix3x3()
    
    rotMatrix33.Xx = 0.90389267610189317
    rotMatrix33.Xy = -0.3560780674383322
    rotMatrix33.Xz = 0.23703679034853509
    rotMatrix33.Yx = 0.12591843668436697
    rotMatrix33.Yy = 0.75107256637727382
    rotMatrix33.Yz = 0.6481007231429502
    rotMatrix33.Zx = -0.40880628345503434
    rotMatrix33.Zy = -0.5559661949478848
    rotMatrix33.Zz = 0.72372578555889788
    translation33 = NXOpen.Point3d(-27.079672137127993, 25.631009297936195, -22.840039942541512)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix33, translation33, 1.106931052946071)
    
    scaleAboutPoint150 = NXOpen.Point3d(-12.190235303352429, 28.682906596122784, 0.0)
    viewCenter150 = NXOpen.Point3d(12.190235303351939, -28.682906596122766, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(-6.6926782057622232, 25.623396559203041, 0.0)
    viewCenter151 = NXOpen.Point3d(6.6926782057617666, -25.623396559203009, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint151, viewCenter151)
    
    rotMatrix34 = NXOpen.Matrix3x3()
    
    rotMatrix34.Xx = 0.74824652280386617
    rotMatrix34.Xy = -0.033858306442362873
    rotMatrix34.Xz = 0.6625562287057436
    rotMatrix34.Yx = 0.40612268255503353
    rotMatrix34.Yy = 0.81307695241583666
    rotMatrix34.Yz = -0.41709739409935909
    rotMatrix34.Zx = -0.52458698785446922
    rotMatrix34.Zy = 0.58117078775092224
    rotMatrix34.Zz = 0.6221326286562574
    translation34 = NXOpen.Point3d(-23.303089435305139, 14.769748666871045, -22.840039942541512)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix34, translation34, 1.7295797702282358)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()