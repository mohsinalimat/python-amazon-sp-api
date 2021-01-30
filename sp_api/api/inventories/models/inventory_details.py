# coding: utf-8

"""
    Selling Partner API for FBA Inventory

    The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InventoryDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fulfillable_quantity': 'int',
        'inbound_working_quantity': 'int',
        'inbound_shipped_quantity': 'int',
        'inbound_receiving_quantity': 'int',
        'reserved_quantity': 'ReservedQuantity',
        'researching_quantity': 'ResearchingQuantity',
        'unfulfillable_quantity': 'UnfulfillableQuantity'
    }

    attribute_map = {
        'fulfillable_quantity': 'fulfillableQuantity',
        'inbound_working_quantity': 'inboundWorkingQuantity',
        'inbound_shipped_quantity': 'inboundShippedQuantity',
        'inbound_receiving_quantity': 'inboundReceivingQuantity',
        'reserved_quantity': 'reservedQuantity',
        'researching_quantity': 'researchingQuantity',
        'unfulfillable_quantity': 'unfulfillableQuantity'
    }

    def __init__(self, fulfillable_quantity=None, inbound_working_quantity=None, inbound_shipped_quantity=None, inbound_receiving_quantity=None, reserved_quantity=None, researching_quantity=None, unfulfillable_quantity=None):  # noqa: E501
        """InventoryDetails - a model defined in Swagger"""  # noqa: E501
        self._fulfillable_quantity = None
        self._inbound_working_quantity = None
        self._inbound_shipped_quantity = None
        self._inbound_receiving_quantity = None
        self._reserved_quantity = None
        self._researching_quantity = None
        self._unfulfillable_quantity = None
        self.discriminator = None
        if fulfillable_quantity is not None:
            self.fulfillable_quantity = fulfillable_quantity
        if inbound_working_quantity is not None:
            self.inbound_working_quantity = inbound_working_quantity
        if inbound_shipped_quantity is not None:
            self.inbound_shipped_quantity = inbound_shipped_quantity
        if inbound_receiving_quantity is not None:
            self.inbound_receiving_quantity = inbound_receiving_quantity
        if reserved_quantity is not None:
            self.reserved_quantity = reserved_quantity
        if researching_quantity is not None:
            self.researching_quantity = researching_quantity
        if unfulfillable_quantity is not None:
            self.unfulfillable_quantity = unfulfillable_quantity

    @property
    def fulfillable_quantity(self):
        """Gets the fulfillable_quantity of this InventoryDetails.  # noqa: E501

        The item quantity that can be picked, packed, and shipped.  # noqa: E501

        :return: The fulfillable_quantity of this InventoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._fulfillable_quantity

    @fulfillable_quantity.setter
    def fulfillable_quantity(self, fulfillable_quantity):
        """Sets the fulfillable_quantity of this InventoryDetails.

        The item quantity that can be picked, packed, and shipped.  # noqa: E501

        :param fulfillable_quantity: The fulfillable_quantity of this InventoryDetails.  # noqa: E501
        :type: int
        """

        self._fulfillable_quantity = fulfillable_quantity

    @property
    def inbound_working_quantity(self):
        """Gets the inbound_working_quantity of this InventoryDetails.  # noqa: E501

        The number of units in an inbound shipment for which you have notified Amazon.  # noqa: E501

        :return: The inbound_working_quantity of this InventoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._inbound_working_quantity

    @inbound_working_quantity.setter
    def inbound_working_quantity(self, inbound_working_quantity):
        """Sets the inbound_working_quantity of this InventoryDetails.

        The number of units in an inbound shipment for which you have notified Amazon.  # noqa: E501

        :param inbound_working_quantity: The inbound_working_quantity of this InventoryDetails.  # noqa: E501
        :type: int
        """

        self._inbound_working_quantity = inbound_working_quantity

    @property
    def inbound_shipped_quantity(self):
        """Gets the inbound_shipped_quantity of this InventoryDetails.  # noqa: E501

        The number of units in an inbound shipment that you have notified Amazon about and have provided a tracking number.  # noqa: E501

        :return: The inbound_shipped_quantity of this InventoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._inbound_shipped_quantity

    @inbound_shipped_quantity.setter
    def inbound_shipped_quantity(self, inbound_shipped_quantity):
        """Sets the inbound_shipped_quantity of this InventoryDetails.

        The number of units in an inbound shipment that you have notified Amazon about and have provided a tracking number.  # noqa: E501

        :param inbound_shipped_quantity: The inbound_shipped_quantity of this InventoryDetails.  # noqa: E501
        :type: int
        """

        self._inbound_shipped_quantity = inbound_shipped_quantity

    @property
    def inbound_receiving_quantity(self):
        """Gets the inbound_receiving_quantity of this InventoryDetails.  # noqa: E501

        The number of units that have not yet been received at an Amazon fulfillment center for processing, but are part of an inbound shipment with some units that have already been received and processed.  # noqa: E501

        :return: The inbound_receiving_quantity of this InventoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._inbound_receiving_quantity

    @inbound_receiving_quantity.setter
    def inbound_receiving_quantity(self, inbound_receiving_quantity):
        """Sets the inbound_receiving_quantity of this InventoryDetails.

        The number of units that have not yet been received at an Amazon fulfillment center for processing, but are part of an inbound shipment with some units that have already been received and processed.  # noqa: E501

        :param inbound_receiving_quantity: The inbound_receiving_quantity of this InventoryDetails.  # noqa: E501
        :type: int
        """

        self._inbound_receiving_quantity = inbound_receiving_quantity

    @property
    def reserved_quantity(self):
        """Gets the reserved_quantity of this InventoryDetails.  # noqa: E501


        :return: The reserved_quantity of this InventoryDetails.  # noqa: E501
        :rtype: ReservedQuantity
        """
        return self._reserved_quantity

    @reserved_quantity.setter
    def reserved_quantity(self, reserved_quantity):
        """Sets the reserved_quantity of this InventoryDetails.


        :param reserved_quantity: The reserved_quantity of this InventoryDetails.  # noqa: E501
        :type: ReservedQuantity
        """

        self._reserved_quantity = reserved_quantity

    @property
    def researching_quantity(self):
        """Gets the researching_quantity of this InventoryDetails.  # noqa: E501


        :return: The researching_quantity of this InventoryDetails.  # noqa: E501
        :rtype: ResearchingQuantity
        """
        return self._researching_quantity

    @researching_quantity.setter
    def researching_quantity(self, researching_quantity):
        """Sets the researching_quantity of this InventoryDetails.


        :param researching_quantity: The researching_quantity of this InventoryDetails.  # noqa: E501
        :type: ResearchingQuantity
        """

        self._researching_quantity = researching_quantity

    @property
    def unfulfillable_quantity(self):
        """Gets the unfulfillable_quantity of this InventoryDetails.  # noqa: E501


        :return: The unfulfillable_quantity of this InventoryDetails.  # noqa: E501
        :rtype: UnfulfillableQuantity
        """
        return self._unfulfillable_quantity

    @unfulfillable_quantity.setter
    def unfulfillable_quantity(self, unfulfillable_quantity):
        """Sets the unfulfillable_quantity of this InventoryDetails.


        :param unfulfillable_quantity: The unfulfillable_quantity of this InventoryDetails.  # noqa: E501
        :type: UnfulfillableQuantity
        """

        self._unfulfillable_quantity = unfulfillable_quantity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InventoryDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InventoryDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
