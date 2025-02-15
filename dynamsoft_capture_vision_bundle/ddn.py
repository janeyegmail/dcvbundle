__version__ = "3.0.10.7501"

if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftDocumentNormalizer
else:
    import _DynamsoftDocumentNormalizer
from typing import List, Tuple, Union


from enum import IntEnum


class EnumImageColourMode(IntEnum):
    ICM_COLOUR = _DynamsoftDocumentNormalizer.ICM_COLOUR
    ICM_GRAYSCALE = _DynamsoftDocumentNormalizer.ICM_GRAYSCALE
    ICM_BINARY = _DynamsoftDocumentNormalizer.ICM_BINARY

class SimplifiedDocumentNormalizerSettings:
    """
    The SimplifiedDocumentNormalizerSettings class contains settings for document normalization. It is a sub-parameter of SimplifiedCaptureVisionSettings.

    Attributes:
        grayscale_transformation_modes(List[int]): Specifies how grayscale transformations should be applied, including whether to process inverted grayscale images and the specific transformation mode to use.
        grayscale_enhancement_modes(List[int]): Specifies how to enhance the quality of the grayscale image.
        colour_mode(int): Specifies the colour mode of the output image.
        page_size(List[int]): Specifies the page size (width by height in pixels) of the normalized image.
        brightness(int): Specifies the brightness of the normalized image.
        contrast(int): Specifies the contrast of the normalized image.
        max_threads_in_one_task(int): Specifies the maximum available threads count in one document normalization task.
        scale_down_threshold(int): Specifies the threshold for the image shrinking.
        min_quadrilateral_area_ratio(int): Specifies the minimum ratio between the target quadrilateral area and the total image area. Only those exceeding this value will be output (measured in percentages).
        expected_documents_count(int): Specifies the number of documents expected to be detected.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @property
    def grayscale_transformation_modes(self) -> List[int]:
        if not hasattr(self, '_grayscale_transformation_modes') or self._grayscale_transformation_modes is None:
            self._grayscale_transformation_modes = _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_grayscaleTransformationModes_get(self)
        return self._grayscale_transformation_modes

    @grayscale_transformation_modes.setter
    def grayscale_transformation_modes(self, value: List[int]):
        if not hasattr(self, '_grayscale_transformation_modes') or self._grayscale_transformation_modes is None:
            self._grayscale_transformation_modes = _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_grayscaleTransformationModes_get(self)
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_grayscaleTransformationModes_set(self, value)
        self._grayscale_transformation_modes = value
    @property
    def grayscale_enhancement_modes(self) -> List[int]:
        if not hasattr(self, '_grayscale_enhancement_modes') or self._grayscale_enhancement_modes is None:
            self._grayscale_enhancement_modes = _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_grayscaleEnhancementModes_get(self)
        return self._grayscale_enhancement_modes

    @grayscale_enhancement_modes.setter
    def grayscale_enhancement_modes(self, value: List[int]):
        if not hasattr(self, '_grayscale_enhancement_modes') or self._grayscale_enhancement_modes is None:
            self._grayscale_enhancement_modes = _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_grayscaleEnhancementModes_get(self)
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_grayscaleEnhancementModes_set(self, value)
        self._grayscale_enhancement_modes = value
    colour_mode: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_colourMode_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_colourMode_set,
        doc="""
            Specifies the colour mode of the output image.
            It is a list of 8 integers, where each integer represents a mode specified by the EnumColourMode enumeration.
            """
    )
    @property
    def page_size(self) -> List[int]:
        if not hasattr(self, '_page_size') or self._page_size is None:
            self._page_size = _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_pageSize_get(self)
        return self._page_size

    @page_size.setter
    def page_size(self, value: List[int]):
        if not hasattr(self, '_page_size') or self._page_size is None:
            self._page_size = _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_pageSize_get(self)
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_pageSize_set(self, value)
        self._page_size = value

    brightness: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_brightness_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_brightness_set,
        doc="""
            Specifies the brightness of the normalized image.
            Value Range: [-100,100]
            Default Value: 0
            """
    )
    contrast: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_contrast_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_contrast_set,
        doc="""
            Specifies the contrast of the normalized image.
            Value Range: [-100,100]
            Default Value: 0
            """
    )
    max_threads_in_one_task: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_maxThreadsInOneTask_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_maxThreadsInOneTask_set,
        doc="""
            Specifies the maximum available threads count in one document normalization task.
            Value Range: [1,256]
            Default Value: 4
            """
    )
    scale_down_threshold: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_scaleDownThreshold_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_scaleDownThreshold_set,
        doc="""
            Specifies the threshold for the image shrinking.
            Value Range: [512, 0x7fffffff]
            Default Value: 2300
            """
    )
    min_quadrilateral_area_ratio: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_minQuadrilateralAreaRatio_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_minQuadrilateralAreaRatio_set,
        doc="""
            Specifies the minimum ratio between the target quadrilateral area and the total image area.
            Only those exceeding this value will be output (measured in percentages).
            Value Range: [0, 100]
            Default Value: 0, which means no limitation.
            """
    )
    expected_documents_count: int = property(
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_expectedDocumentsCount_get,
        _DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_expectedDocumentsCount_set,
        doc="""
            Specifies the number of documents expected to be detected.
            Value Range: [0, 0x7fffffff]
            Default Value: 0, which means the count is unknown. The library will try to find at least 1 document.
            """
    )

    def __init__(self):
        _DynamsoftDocumentNormalizer.Class_init(
            self,
            _DynamsoftDocumentNormalizer.new_SimplifiedDocumentNormalizerSettings(),
        )

    __destroy__ = (
        _DynamsoftDocumentNormalizer.delete_SimplifiedDocumentNormalizerSettings
    )


_DynamsoftDocumentNormalizer.SimplifiedDocumentNormalizerSettings_register(
    SimplifiedDocumentNormalizerSettings
)

class DetectedQuadResultItem(CapturedResultItem):
    """
    The DetectedQuadResultItem class stores a captured result whose type is detected quad.

    Methods:
        get_location(self) -> Quadrilateral: Gets the location of current object.
        get_confidence_as_document_boundary(self) -> int: Gets the confidence of current object as a document boundary.
        get_cross_verification_status(self) -> EnumCrossVerificationStatus: Gets the status of current object as a verified document boundary.
        set_cross_verification_status(self, status: EnumCrossVerificationStatus) -> Sets the status of current object.
        get_local_to_original_matrix(self) -> List[float]: Gets the transformation matrix from the local coordinate system to the original image coordinate system.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_location(self) -> Quadrilateral:
        """
        Gets the location of current object.

        Returns:
            The location of current object.
        """
        return _DynamsoftDocumentNormalizer.CDetectedQuadResultItem_GetLocation(self)

    def get_confidence_as_document_boundary(self) -> int:
        """
        Gets the confidence of current object as a document boundary.

        Returns:
            The confidence as document boundary of the detected quad result.
        """
        return _DynamsoftDocumentNormalizer.CDetectedQuadResultItem_GetConfidenceAsDocumentBoundary(
            self
        )
    def get_cross_verification_status(self) -> EnumCrossVerificationStatus:
        """
        Gets the status of current object as a verified document boundary.
        
        Returns:
            Return the CrossVerificationStatus of the detected quad result.
        """
        return _DynamsoftDocumentNormalizer.CDetectedQuadResultItem_GetCrossVerificationStatus(self)

    def set_cross_verification_status(self, status: EnumCrossVerificationStatus) -> None:
        """
        Sets the status of current object.

        Args:
            status(EnumCrossVerificationStatus): The CrossVerificationStatus to be set.
        """
        _DynamsoftDocumentNormalizer.CDetectedQuadResultItem_SetCrossVerificationStatus(self, status)    

_DynamsoftDocumentNormalizer.CDetectedQuadResultItem_register(DetectedQuadResultItem)


class DeskewedImageResultItem(CapturedResultItem):
    """
    The DeskewedImageResultItem class stores a captured result item whose type is normalized image.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of current object.
        get_source_deskew_quad(self) -> Quadrilateral: Gets the quadrilateral used for deskewing the image.
        get_cross_verification_status(self) -> EnumCrossVerificationStatus: Gets the status of current object as a verified deskewed image.
        set_cross_verification_status(self, status: EnumCrossVerificationStatus) -> None: Sets the status of current object.
        get_local_to_original_matrix(self) -> List[float]: Gets the transformation matrix from the local coordinate system to the original image coordinate system.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_image_data(self) -> ImageData:
        """
        Gets the image data of current object.

        Returns:
            The image data.
        """
        return _DynamsoftDocumentNormalizer.CDeskewedImageResultItem_GetImageData(
            self
        )

    def get_source_deskew_quad(self) -> Quadrilateral:
        """
        Gets the quadrilateral used for deskewing the image.

        Returns:
            A CQuadrilateral object representing the four corners of the quadrilateral used to deskew the image.
        """
        return _DynamsoftDocumentNormalizer.CDeskewedImageResultItem_GetSourceDeskewQuad(self)

    def get_cross_verification_status(self) -> EnumCrossVerificationStatus:
        """
        Gets the status of current object as a verified deskewed image.
        
        Returns:
            Return the CrossVerificationStatus of the deskewed image result.
        """
        return _DynamsoftDocumentNormalizer.CDeskewedImageResultItem_GetCrossVerificationStatus(self)

    def set_cross_verification_status(self, status: EnumCrossVerificationStatus) -> None:
        """
        Sets the status of current object.

        Args:
            status(EnumCrossVerificationStatus): The CrossVerificationStatus to be set.
        """
        _DynamsoftDocumentNormalizer.CDeskewedImageResultItem_SetCrossVerificationStatus(self, status)

    def get_original_to_local_matrix(self) -> List[float]:
        """
        Gets the transformation matrix from the local coordinate system to the original image coordinate system.
        
        Returns:
            A double array of size 9, representing the 3x3 transformation matrix that converts coordinates from the local image to the original image.
        """
        return _DynamsoftDocumentNormalizer.CDeskewedImageResultItem_GetOriginalToLocalMatrix(self)
_DynamsoftDocumentNormalizer.CDeskewedImageResultItem_register(
    DeskewedImageResultItem
)

class EnhancedImageResultItem(CapturedResultItem):
    """
    The `CEnhancedImageResultItem` class stores a captured result item whose type is enhanced image.
    
    Methods:
        get_image_data(self) -> ImageData: Gets the image data of current object.
        get_local_to_original_matrix(self) -> List[float]: Gets the transformation matrix from the local coordinate system to the original image coordinate system.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )
    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")
    
    def get_image_data(self) -> ImageData:
        """
        Gets the image data of current object.
        
        Returns:
            The image data.
        """
        return _DynamsoftDocumentNormalizer.CEnhancedImageResultItem_GetImageData(
            self
        )
    
    def get_original_to_local_matrix(self) -> List[float]:
        """
        Gets the transformation matrix from the local coordinate system to the original image coordinate system.
        
        Returns:
            A double array of size 9, representing the 3x3 transformation matrix that converts coordinates from the local image to the original image.
        """
        return _DynamsoftDocumentNormalizer.CEnhancedImageResultItem_GetOriginalToLocalMatrix(
            self
        )
    
    
_DynamsoftDocumentNormalizer.CEnhancedImageResultItem_register(EnhancedImageResultItem)

class ProcessedDocumentResult(CapturedResultBase):
    """
    The `CDocumentResult` class stores a collection of captured result items.

    Methods:
        get_detected_quad_result_items(self, index: int) -> DetectedQuadResultItem: Retrieves the detected quad result items.
        get_deskewed_image_result_items(self, index: int) -> DeskewedImageResultItem: Retrieves the deskewed image result items.
        get_enhanced_image_result_items(self, index: int) -> EnhancedImageResultItem: Retrieves the enhanced image result items.
        has_item(self, item: Union[DetectedQuadResultItem, DeskewedImageResultItem, EnhancedImageResultItem]) -> bool: Checks if the specified item is present in the array.
        remove_item(self, item: Union[DetectedQuadResultItem, DeskewedImageResultItem, EnhancedImageResultItem]) -> int: Removes the specified item from the array in the recognition result.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")
    
    def get_detected_quad_result_items(self) -> List[DetectedQuadResultItem]:
        """
        Retrieves the detected quad result items.
                
        Returns:
            A DetectedQuadResultItem object representing the detected quad result items.
        """
        list = []
        count = _DynamsoftDocumentNormalizer.CProcessedDocumentResult_GetDetectedQuadResultItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftDocumentNormalizer.CProcessedDocumentResult_GetDetectedQuadResultItem(self, i))
        return list

    def get_deskewed_image_result_items(self) -> List[DeskewedImageResultItem]:
        """
        Retrieves the deskewed image result items.

        Returns:
            A DeskewedImageResultItem object representing the deskewed image result items.
        """
        list = []
        count = _DynamsoftDocumentNormalizer.CProcessedDocumentResult_GetDeskewedImageResultItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftDocumentNormalizer.CProcessedDocumentResult_GetDeskewedImageResultItem(self, i))
        return list
    
    def get_enhanced_image_result_items(self) -> List[EnhancedImageResultItem]:
        """
        Retrieves the enhanced image result items.
        
        Returns:
            A EnhancedImageResultItem object representing the enhanced image result items.
        """
        list = []
        count = _DynamsoftDocumentNormalizer.CProcessedDocumentResult_GetEnhancedImageResultItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftDocumentNormalizer.CProcessedDocumentResult_GetEnhancedImageResultItem(self, i))
        return list

    def has_item(self, item: Union[DetectedQuadResultItem, DeskewedImageResultItem, EnhancedImageResultItem]) -> bool:
        """
        Check if the DetectedQuadResultItem,DeskewedImageResultItem or EnhancedImageResultItem is present in the array.

        Args:
            item (Union[DetectedQuadResultItem, DeskewedImageResultItem, EnhancedImageResultItem]): The specific item to check.
        
        Returns:
            A bool value indicating whether the item is present in the array or not.
        """
        return _DynamsoftDocumentNormalizer.CProcessedDocumentResult_HasItem(self, item)
    
    def remove_item(self, item: Union[DetectedQuadResultItem, DeskewedImageResultItem, EnhancedImageResultItem]) -> int:
        """
        Remove the DetectedQuadResultItem,DeskewedImageResultItem or EnhancedImageResultItem from the array in the recognition result.

        Args:
            item (Union[DetectedQuadResultItem, DeskewedImageResultItem, EnhancedImageResultItem]): The specific item to remove.
        
        Returns:
            The value indicating whether the deletion was successful or not.
        """
        return _DynamsoftDocumentNormalizer.CProcessedDocumentResult_RemoveItem(self, item)
    
    __destroy__ = _DynamsoftDocumentNormalizer.CProcessedDocumentResult_Release

class DocumentNormalizerModule:
    """
    The DocumentNormalizerModule class defines general functions in the document normalizer module.
    
    Methods:
        get_version() -> str: Returns the version of the document normalizer module.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns the version of the document normalizer module.

        Returns:
            A string representing the version of the document normalizer module.
        """
        return __version__ + " (Algotithm " + _DynamsoftDocumentNormalizer.CDocumentNormalizerModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftDocumentNormalizer.Class_init(
            self, _DynamsoftDocumentNormalizer.new_CDocumentNormalizerModule()
        )

    __destroy__ = _DynamsoftDocumentNormalizer.delete_CDocumentNormalizerModule


_DynamsoftDocumentNormalizer.CDocumentNormalizerModule_register(
    DocumentNormalizerModule
)

class DetectedQuadElement(RegionObjectElement):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        _DynamsoftDocumentNormalizer.Class_init(
            self, _DynamsoftDocumentNormalizer.CDocumentNormalizerModule_CreateDetectedQuadElement()
        )

    def get_confidence_as_document_boundary(self) -> int:
        return _DynamsoftDocumentNormalizer.CDetectedQuadElement_GetConfidenceAsDocumentBoundary(self)
    def set_location(self, location: Quadrilateral):
        return _DynamsoftDocumentNormalizer.CDetectedQuadElement_SetLocation(self, location)

# Register CDetectedQuadElement in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CDetectedQuadElement_register(DetectedQuadElement)
class DeskewedImageElement(RegionObjectElement):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        _DynamsoftDocumentNormalizer.Class_init(
            self, _DynamsoftDocumentNormalizer.CDocumentNormalizerModule_CreateDeskewedImageElement()
        )
    
    def set_image_data(self, image_data: ImageData) -> int:
        return _DynamsoftDocumentNormalizer.CDeskewedImageElement_SetImageData(self, image_data)
    
    def get_source_deskew_quad(self) -> Quadrilateral:
        return _DynamsoftDocumentNormalizer.CDeskewedImageElement_GetSourceDeskewQuad(self)

# Register CDeskewedImageElement in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CDeskewedImageElement_register(DeskewedImageElement)

class EnhancedImageElement(RegionObjectElement):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        _DynamsoftDocumentNormalizer.Class_init(
            self, _DynamsoftDocumentNormalizer.CDocumentNormalizerModule_CreateEnhancedImageElement()
        )

    def set_image_data(self, image_data: ImageData) -> int:
        return _DynamsoftDocumentNormalizer.CEnhancedImageElement_SetImageData(self, image_data)
    
_DynamsoftDocumentNormalizer.CEnhancedImageElement_register(EnhancedImageElement)

class LongLinesUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    

    def get_count(self) -> int:
        return _DynamsoftDocumentNormalizer.CLongLinesUnit_GetCount(self)

    def get_long_line(self, index: int) -> LineSegment:
        return _DynamsoftDocumentNormalizer.CLongLinesUnit_GetLongLine(self, index)

    def remove_all_long_lines(self) -> None:
        return _DynamsoftDocumentNormalizer.CLongLinesUnit_RemoveAllLongLines(self)

    def remove_long_line(self, index: int) -> int:
        return _DynamsoftDocumentNormalizer.CLongLinesUnit_RemoveLongLine(self, index)

    def add_long_line(self, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CLongLinesUnit_AddLongLine(self, line, matrix_to_original_image)

    def set_long_line(self, index: int, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CLongLinesUnit_SetLongLine(self, index, line, matrix_to_original_image)

# Register CLongLinesUnit in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CLongLinesUnit_register(LongLinesUnit)

class LogicLinesUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    

    def get_count(self) -> int:
        return _DynamsoftDocumentNormalizer.CLogicLinesUnit_GetCount(self)

    def get_logic_line(self, index: int) -> LineSegment:
        return _DynamsoftDocumentNormalizer.CLogicLinesUnit_GetLogicLine(self, index)

    def remove_all_logic_lines(self) -> None:
        return _DynamsoftDocumentNormalizer.CLogicLinesUnit_RemoveAllLogicLines(self)

    def remove_logic_line(self, index: int) -> int:
        return _DynamsoftDocumentNormalizer.CLogicLinesUnit_RemoveLogicLine(self, index)

    def add_logic_line(self, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CLogicLinesUnit_AddLogicLine(self, line, matrix_to_original_image)

    def set_logic_line(self, index: int, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CLogicLinesUnit_SetLogicLine(self, index, line, matrix_to_original_image)

# Register CLogicLinesUnit in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CLogicLinesUnit_register(LogicLinesUnit)

class CornersUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    

    def get_count(self) -> int:
        return _DynamsoftDocumentNormalizer.CCornersUnit_GetCount(self)

    def get_corner(self, index: int) -> Tuple[int, Corner]:
        return _DynamsoftDocumentNormalizer.CCornersUnit_GetCorner(self, index)

    def remove_all_corners(self) -> None:
        return _DynamsoftDocumentNormalizer.CCornersUnit_RemoveAllCorners(self)

    def remove_corner(self, index: int) -> int:
        return _DynamsoftDocumentNormalizer.CCornersUnit_RemoveCorner(self, index)

    def add_corner(self, corner: Corner, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CCornersUnit_AddCorner(self, corner, matrix_to_original_image)

    def set_corner(self, index: int, corner: Corner, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CCornersUnit_SetCorner(self, index, corner, matrix_to_original_image)

# Register CCornersUnit in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CCornersUnit_register(CornersUnit)
class CandidateQuadEdgesUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    

    def get_count(self) -> int:
        return _DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_GetCount(self)

    def get_candidate_quad_edge(self, index: int) -> Tuple[int, Edge]:
        return _DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_GetCandidateQuadEdge(self, index)

    def remove_all_candidate_quad_edges(self) -> None:
        return _DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_RemoveAllCandidateQuadEdges(self)

    def remove_candidate_quad_edge(self, index: int) -> int:
        return _DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_RemoveCandidateQuadEdge(self, index)

    def add_candidate_quad_edge(self, edge: Edge, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_AddCandidateQuadEdge(self, edge, matrix_to_original_image)

    def set_candidate_quad_edge(self, index: int, edge: Edge, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_SetCandidateQuadEdge(self, index, edge, matrix_to_original_image)

# Register CCandidateQuadEdgesUnit in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CCandidateQuadEdgesUnit_register(CandidateQuadEdgesUnit)
class DetectedQuadsUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    

    def get_count(self) -> int:
        return _DynamsoftDocumentNormalizer.CDetectedQuadsUnit_GetCount(self)

    def get_detected_quad(self, index: int) -> DetectedQuadElement:
        return _DynamsoftDocumentNormalizer.CDetectedQuadsUnit_GetDetectedQuad(self, index)

    def remove_all_detected_quads(self) -> None:
        return _DynamsoftDocumentNormalizer.CDetectedQuadsUnit_RemoveAllDetectedQuads(self)

    def remove_detected_quad(self, index: int) -> int:
        return _DynamsoftDocumentNormalizer.CDetectedQuadsUnit_RemoveDetectedQuad(self, index)

    def add_detected_quad(self, element: DetectedQuadElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CDetectedQuadsUnit_AddDetectedQuad(self, element, matrix_to_original_image)

    def set_detected_quad(self, index: int, element: DetectedQuadElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CDetectedQuadsUnit_SetDetectedQuad(self, index, element, matrix_to_original_image)

# Register CDetectedQuadsUnit in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CDetectedQuadsUnit_register(DetectedQuadsUnit)
class DeskewedImageUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    
    def get_deskewed_image(self) -> DeskewedImageElement:
        return _DynamsoftDocumentNormalizer.CDeskewedImageUnit_GetDeskewedImage(self)

    def set_deskewed_image(self, element: DeskewedImageElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        return _DynamsoftDocumentNormalizer.CDeskewedImageUnit_SetDeskewedImage(self, element, matrix_to_original_image)

# Register CDeskewedImageUnit in _DynamsoftDocumentNormalizer:
_DynamsoftDocumentNormalizer.CDeskewedImageUnit_register(DeskewedImageUnit)

class EnhancedImageUnit(IntermediateResultUnit):
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")

    def get_enhanced_image(self) -> EnhancedImageElement:
        return _DynamsoftDocumentNormalizer.CEnhancedImageUnit_GetEnhancedImage(self)

    def set_enhanced_image(self, element: EnhancedImageElement) -> int:
        return _DynamsoftDocumentNormalizer.CEnhancedImageUnit_SetEnhancedImage(self, element)
    