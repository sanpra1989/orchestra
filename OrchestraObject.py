import abc

class OrchestraModule(object):
    __metaclass__ = abc.ABCMeta
        
        
    @abc.abstractmethod
    def OnFlowTableChange(self, input):
        """Called when Flow Table Topology within a device changes."""
        return
        
    @abc.abstractmethod
    def OnNetworkTopologyChange(self, input):
        """Called when Network Topology changes."""
        return
        
        
    @abc.abstractmethod
    def OnConfigChange(self, input):
        """Called when configuration changes."""
        return
    
