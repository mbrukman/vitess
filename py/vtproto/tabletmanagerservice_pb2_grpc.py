# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import tabletmanagerdata_pb2 as tabletmanagerdata__pb2


class TabletManagerStub(object):
  """TabletManager is a service definition for tabletmanagerdata.TabletManager.

  Various read-only methods

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/Ping',
        request_serializer=tabletmanagerdata__pb2.PingRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.PingResponse.FromString,
        )
    self.Sleep = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/Sleep',
        request_serializer=tabletmanagerdata__pb2.SleepRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SleepResponse.FromString,
        )
    self.ExecuteHook = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ExecuteHook',
        request_serializer=tabletmanagerdata__pb2.ExecuteHookRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ExecuteHookResponse.FromString,
        )
    self.GetSchema = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/GetSchema',
        request_serializer=tabletmanagerdata__pb2.GetSchemaRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.GetSchemaResponse.FromString,
        )
    self.GetPermissions = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/GetPermissions',
        request_serializer=tabletmanagerdata__pb2.GetPermissionsRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.GetPermissionsResponse.FromString,
        )
    self.SetReadOnly = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/SetReadOnly',
        request_serializer=tabletmanagerdata__pb2.SetReadOnlyRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SetReadOnlyResponse.FromString,
        )
    self.SetReadWrite = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/SetReadWrite',
        request_serializer=tabletmanagerdata__pb2.SetReadWriteRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SetReadWriteResponse.FromString,
        )
    self.ChangeType = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ChangeType',
        request_serializer=tabletmanagerdata__pb2.ChangeTypeRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ChangeTypeResponse.FromString,
        )
    self.RefreshState = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/RefreshState',
        request_serializer=tabletmanagerdata__pb2.RefreshStateRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.RefreshStateResponse.FromString,
        )
    self.RunHealthCheck = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/RunHealthCheck',
        request_serializer=tabletmanagerdata__pb2.RunHealthCheckRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.RunHealthCheckResponse.FromString,
        )
    self.IgnoreHealthError = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/IgnoreHealthError',
        request_serializer=tabletmanagerdata__pb2.IgnoreHealthErrorRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.IgnoreHealthErrorResponse.FromString,
        )
    self.ReloadSchema = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ReloadSchema',
        request_serializer=tabletmanagerdata__pb2.ReloadSchemaRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ReloadSchemaResponse.FromString,
        )
    self.PreflightSchema = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/PreflightSchema',
        request_serializer=tabletmanagerdata__pb2.PreflightSchemaRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.PreflightSchemaResponse.FromString,
        )
    self.ApplySchema = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ApplySchema',
        request_serializer=tabletmanagerdata__pb2.ApplySchemaRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ApplySchemaResponse.FromString,
        )
    self.ExecuteFetchAsDba = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ExecuteFetchAsDba',
        request_serializer=tabletmanagerdata__pb2.ExecuteFetchAsDbaRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ExecuteFetchAsDbaResponse.FromString,
        )
    self.ExecuteFetchAsAllPrivs = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ExecuteFetchAsAllPrivs',
        request_serializer=tabletmanagerdata__pb2.ExecuteFetchAsAllPrivsRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ExecuteFetchAsAllPrivsResponse.FromString,
        )
    self.ExecuteFetchAsApp = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ExecuteFetchAsApp',
        request_serializer=tabletmanagerdata__pb2.ExecuteFetchAsAppRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ExecuteFetchAsAppResponse.FromString,
        )
    self.SlaveStatus = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/SlaveStatus',
        request_serializer=tabletmanagerdata__pb2.SlaveStatusRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SlaveStatusResponse.FromString,
        )
    self.MasterPosition = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/MasterPosition',
        request_serializer=tabletmanagerdata__pb2.MasterPositionRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.MasterPositionResponse.FromString,
        )
    self.StopSlave = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/StopSlave',
        request_serializer=tabletmanagerdata__pb2.StopSlaveRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.StopSlaveResponse.FromString,
        )
    self.StopSlaveMinimum = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/StopSlaveMinimum',
        request_serializer=tabletmanagerdata__pb2.StopSlaveMinimumRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.StopSlaveMinimumResponse.FromString,
        )
    self.StartSlave = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/StartSlave',
        request_serializer=tabletmanagerdata__pb2.StartSlaveRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.StartSlaveResponse.FromString,
        )
    self.TabletExternallyReparented = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/TabletExternallyReparented',
        request_serializer=tabletmanagerdata__pb2.TabletExternallyReparentedRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.TabletExternallyReparentedResponse.FromString,
        )
    self.TabletExternallyElected = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/TabletExternallyElected',
        request_serializer=tabletmanagerdata__pb2.TabletExternallyElectedRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.TabletExternallyElectedResponse.FromString,
        )
    self.GetSlaves = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/GetSlaves',
        request_serializer=tabletmanagerdata__pb2.GetSlavesRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.GetSlavesResponse.FromString,
        )
    self.WaitBlpPosition = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/WaitBlpPosition',
        request_serializer=tabletmanagerdata__pb2.WaitBlpPositionRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.WaitBlpPositionResponse.FromString,
        )
    self.StopBlp = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/StopBlp',
        request_serializer=tabletmanagerdata__pb2.StopBlpRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.StopBlpResponse.FromString,
        )
    self.StartBlp = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/StartBlp',
        request_serializer=tabletmanagerdata__pb2.StartBlpRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.StartBlpResponse.FromString,
        )
    self.RunBlpUntil = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/RunBlpUntil',
        request_serializer=tabletmanagerdata__pb2.RunBlpUntilRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.RunBlpUntilResponse.FromString,
        )
    self.ResetReplication = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/ResetReplication',
        request_serializer=tabletmanagerdata__pb2.ResetReplicationRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.ResetReplicationResponse.FromString,
        )
    self.InitMaster = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/InitMaster',
        request_serializer=tabletmanagerdata__pb2.InitMasterRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.InitMasterResponse.FromString,
        )
    self.PopulateReparentJournal = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/PopulateReparentJournal',
        request_serializer=tabletmanagerdata__pb2.PopulateReparentJournalRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.PopulateReparentJournalResponse.FromString,
        )
    self.InitSlave = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/InitSlave',
        request_serializer=tabletmanagerdata__pb2.InitSlaveRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.InitSlaveResponse.FromString,
        )
    self.DemoteMaster = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/DemoteMaster',
        request_serializer=tabletmanagerdata__pb2.DemoteMasterRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.DemoteMasterResponse.FromString,
        )
    self.PromoteSlaveWhenCaughtUp = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/PromoteSlaveWhenCaughtUp',
        request_serializer=tabletmanagerdata__pb2.PromoteSlaveWhenCaughtUpRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.PromoteSlaveWhenCaughtUpResponse.FromString,
        )
    self.SlaveWasPromoted = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/SlaveWasPromoted',
        request_serializer=tabletmanagerdata__pb2.SlaveWasPromotedRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SlaveWasPromotedResponse.FromString,
        )
    self.SetMaster = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/SetMaster',
        request_serializer=tabletmanagerdata__pb2.SetMasterRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SetMasterResponse.FromString,
        )
    self.SlaveWasRestarted = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/SlaveWasRestarted',
        request_serializer=tabletmanagerdata__pb2.SlaveWasRestartedRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.SlaveWasRestartedResponse.FromString,
        )
    self.StopReplicationAndGetStatus = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/StopReplicationAndGetStatus',
        request_serializer=tabletmanagerdata__pb2.StopReplicationAndGetStatusRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.StopReplicationAndGetStatusResponse.FromString,
        )
    self.PromoteSlave = channel.unary_unary(
        '/tabletmanagerservice.TabletManager/PromoteSlave',
        request_serializer=tabletmanagerdata__pb2.PromoteSlaveRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.PromoteSlaveResponse.FromString,
        )
    self.Backup = channel.unary_stream(
        '/tabletmanagerservice.TabletManager/Backup',
        request_serializer=tabletmanagerdata__pb2.BackupRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.BackupResponse.FromString,
        )
    self.RestoreFromBackup = channel.unary_stream(
        '/tabletmanagerservice.TabletManager/RestoreFromBackup',
        request_serializer=tabletmanagerdata__pb2.RestoreFromBackupRequest.SerializeToString,
        response_deserializer=tabletmanagerdata__pb2.RestoreFromBackupResponse.FromString,
        )


class TabletManagerServicer(object):
  """TabletManager is a service definition for tabletmanagerdata.TabletManager.

  Various read-only methods

  """

  def Ping(self, request, context):
    """Ping returns the input payload
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sleep(self, request, context):
    """Sleep sleeps for the provided duration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteHook(self, request, context):
    """ExecuteHook executes the hook remotely
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSchema(self, request, context):
    """GetSchema asks the tablet for its schema
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPermissions(self, request, context):
    """GetPermissions asks the tablet for its permissions
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetReadOnly(self, request, context):
    """
    Various read-write methods


    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetReadWrite(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeType(self, request, context):
    """ChangeType asks the remote tablet to change its type
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RefreshState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunHealthCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IgnoreHealthError(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReloadSchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PreflightSchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplySchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteFetchAsDba(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteFetchAsAllPrivs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteFetchAsApp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SlaveStatus(self, request, context):
    """
    Replication related methods


    SlaveStatus returns the current slave status.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MasterPosition(self, request, context):
    """MasterPosition returns the current master position
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopSlave(self, request, context):
    """StopSlave makes mysql stop its replication
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopSlaveMinimum(self, request, context):
    """StopSlaveMinimum stops the mysql replication after it reaches
    the provided minimum point
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartSlave(self, request, context):
    """StartSlave starts the mysql replication
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TabletExternallyReparented(self, request, context):
    """TabletExternallyReparented tells a tablet that its underlying MySQL is
    currently the master. It is only used in environments (tabletmanagerdata.such as Vitess+MoB)
    in which MySQL is reparented by some agent external to Vitess, and then
    that agent simply notifies Vitess.

    This call is idempotent with respect to a single target tablet.
    However, the tablet assumes there is a cooling-off period following the
    initial external reparent from A to B, before this call is repeated on any
    tablet other than B. This assumption is configurable with the vttablet flag
    "finalize_external_reparent_timeout".

    For more information, see the design doc at go/vt-fast-failover.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TabletExternallyElected(self, request, context):
    """TabletExternallyElected is an notification that may be sent in
    anticipation of potentially later sending TabletExternallyReparented.
    The tablet can use this extra lead time to prepare to react quickly if
    TabletExternallyReparented does follow.

    This call is effectively a no-op if it is not followed by a call to
    TabletExternallyReparented, so the external agent doing the reparent can
    still change its mind.

    The agent does not need to wait for this call or cancel it before calling
    TabletExternallyReparented if the external reparent operation finishes
    before TabletExternallyElected returns.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSlaves(self, request, context):
    """GetSlaves asks for the list of mysql slaves
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WaitBlpPosition(self, request, context):
    """WaitBlpPosition tells the remote tablet to wait until it reaches
    the specified binolg player position
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopBlp(self, request, context):
    """StopBlp asks the tablet to stop all its binlog players,
    and returns the current position for all of them
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartBlp(self, request, context):
    """StartBlp asks the tablet to restart its binlog players
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunBlpUntil(self, request, context):
    """RunBlpUntil asks the tablet to restart its binlog players
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetReplication(self, request, context):
    """
    Reparenting related functions


    ResetReplication makes the target not replicating
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InitMaster(self, request, context):
    """InitMaster initializes the tablet as a master
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PopulateReparentJournal(self, request, context):
    """PopulateReparentJournal tells the tablet to add an entry to its
    reparent journal
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InitSlave(self, request, context):
    """InitSlave tells the tablet to reparent to the master unconditionnally
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DemoteMaster(self, request, context):
    """DemoteMaster tells the soon-to-be-former master it's gonna change
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PromoteSlaveWhenCaughtUp(self, request, context):
    """PromoteSlaveWhenCaughtUp tells the remote tablet to catch up,
    and then be the master
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SlaveWasPromoted(self, request, context):
    """SlaveWasPromoted tells the remote tablet it is now the master
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetMaster(self, request, context):
    """SetMaster tells the slave to reparent
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SlaveWasRestarted(self, request, context):
    """SlaveWasRestarted tells the remote tablet its master has changed
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopReplicationAndGetStatus(self, request, context):
    """StopReplicationAndGetStatus stops MySQL replication, and returns the
    replication status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PromoteSlave(self, request, context):
    """PromoteSlave makes the slave the new master
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Backup(self, request, context):
    """
    Backup related methods


    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreFromBackup(self, request, context):
    """RestoreFromBackup deletes all local data and restores it from the latest backup.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TabletManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=tabletmanagerdata__pb2.PingRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.PingResponse.SerializeToString,
      ),
      'Sleep': grpc.unary_unary_rpc_method_handler(
          servicer.Sleep,
          request_deserializer=tabletmanagerdata__pb2.SleepRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SleepResponse.SerializeToString,
      ),
      'ExecuteHook': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteHook,
          request_deserializer=tabletmanagerdata__pb2.ExecuteHookRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ExecuteHookResponse.SerializeToString,
      ),
      'GetSchema': grpc.unary_unary_rpc_method_handler(
          servicer.GetSchema,
          request_deserializer=tabletmanagerdata__pb2.GetSchemaRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.GetSchemaResponse.SerializeToString,
      ),
      'GetPermissions': grpc.unary_unary_rpc_method_handler(
          servicer.GetPermissions,
          request_deserializer=tabletmanagerdata__pb2.GetPermissionsRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.GetPermissionsResponse.SerializeToString,
      ),
      'SetReadOnly': grpc.unary_unary_rpc_method_handler(
          servicer.SetReadOnly,
          request_deserializer=tabletmanagerdata__pb2.SetReadOnlyRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SetReadOnlyResponse.SerializeToString,
      ),
      'SetReadWrite': grpc.unary_unary_rpc_method_handler(
          servicer.SetReadWrite,
          request_deserializer=tabletmanagerdata__pb2.SetReadWriteRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SetReadWriteResponse.SerializeToString,
      ),
      'ChangeType': grpc.unary_unary_rpc_method_handler(
          servicer.ChangeType,
          request_deserializer=tabletmanagerdata__pb2.ChangeTypeRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ChangeTypeResponse.SerializeToString,
      ),
      'RefreshState': grpc.unary_unary_rpc_method_handler(
          servicer.RefreshState,
          request_deserializer=tabletmanagerdata__pb2.RefreshStateRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.RefreshStateResponse.SerializeToString,
      ),
      'RunHealthCheck': grpc.unary_unary_rpc_method_handler(
          servicer.RunHealthCheck,
          request_deserializer=tabletmanagerdata__pb2.RunHealthCheckRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.RunHealthCheckResponse.SerializeToString,
      ),
      'IgnoreHealthError': grpc.unary_unary_rpc_method_handler(
          servicer.IgnoreHealthError,
          request_deserializer=tabletmanagerdata__pb2.IgnoreHealthErrorRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.IgnoreHealthErrorResponse.SerializeToString,
      ),
      'ReloadSchema': grpc.unary_unary_rpc_method_handler(
          servicer.ReloadSchema,
          request_deserializer=tabletmanagerdata__pb2.ReloadSchemaRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ReloadSchemaResponse.SerializeToString,
      ),
      'PreflightSchema': grpc.unary_unary_rpc_method_handler(
          servicer.PreflightSchema,
          request_deserializer=tabletmanagerdata__pb2.PreflightSchemaRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.PreflightSchemaResponse.SerializeToString,
      ),
      'ApplySchema': grpc.unary_unary_rpc_method_handler(
          servicer.ApplySchema,
          request_deserializer=tabletmanagerdata__pb2.ApplySchemaRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ApplySchemaResponse.SerializeToString,
      ),
      'ExecuteFetchAsDba': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteFetchAsDba,
          request_deserializer=tabletmanagerdata__pb2.ExecuteFetchAsDbaRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ExecuteFetchAsDbaResponse.SerializeToString,
      ),
      'ExecuteFetchAsAllPrivs': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteFetchAsAllPrivs,
          request_deserializer=tabletmanagerdata__pb2.ExecuteFetchAsAllPrivsRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ExecuteFetchAsAllPrivsResponse.SerializeToString,
      ),
      'ExecuteFetchAsApp': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteFetchAsApp,
          request_deserializer=tabletmanagerdata__pb2.ExecuteFetchAsAppRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ExecuteFetchAsAppResponse.SerializeToString,
      ),
      'SlaveStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SlaveStatus,
          request_deserializer=tabletmanagerdata__pb2.SlaveStatusRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SlaveStatusResponse.SerializeToString,
      ),
      'MasterPosition': grpc.unary_unary_rpc_method_handler(
          servicer.MasterPosition,
          request_deserializer=tabletmanagerdata__pb2.MasterPositionRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.MasterPositionResponse.SerializeToString,
      ),
      'StopSlave': grpc.unary_unary_rpc_method_handler(
          servicer.StopSlave,
          request_deserializer=tabletmanagerdata__pb2.StopSlaveRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.StopSlaveResponse.SerializeToString,
      ),
      'StopSlaveMinimum': grpc.unary_unary_rpc_method_handler(
          servicer.StopSlaveMinimum,
          request_deserializer=tabletmanagerdata__pb2.StopSlaveMinimumRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.StopSlaveMinimumResponse.SerializeToString,
      ),
      'StartSlave': grpc.unary_unary_rpc_method_handler(
          servicer.StartSlave,
          request_deserializer=tabletmanagerdata__pb2.StartSlaveRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.StartSlaveResponse.SerializeToString,
      ),
      'TabletExternallyReparented': grpc.unary_unary_rpc_method_handler(
          servicer.TabletExternallyReparented,
          request_deserializer=tabletmanagerdata__pb2.TabletExternallyReparentedRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.TabletExternallyReparentedResponse.SerializeToString,
      ),
      'TabletExternallyElected': grpc.unary_unary_rpc_method_handler(
          servicer.TabletExternallyElected,
          request_deserializer=tabletmanagerdata__pb2.TabletExternallyElectedRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.TabletExternallyElectedResponse.SerializeToString,
      ),
      'GetSlaves': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlaves,
          request_deserializer=tabletmanagerdata__pb2.GetSlavesRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.GetSlavesResponse.SerializeToString,
      ),
      'WaitBlpPosition': grpc.unary_unary_rpc_method_handler(
          servicer.WaitBlpPosition,
          request_deserializer=tabletmanagerdata__pb2.WaitBlpPositionRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.WaitBlpPositionResponse.SerializeToString,
      ),
      'StopBlp': grpc.unary_unary_rpc_method_handler(
          servicer.StopBlp,
          request_deserializer=tabletmanagerdata__pb2.StopBlpRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.StopBlpResponse.SerializeToString,
      ),
      'StartBlp': grpc.unary_unary_rpc_method_handler(
          servicer.StartBlp,
          request_deserializer=tabletmanagerdata__pb2.StartBlpRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.StartBlpResponse.SerializeToString,
      ),
      'RunBlpUntil': grpc.unary_unary_rpc_method_handler(
          servicer.RunBlpUntil,
          request_deserializer=tabletmanagerdata__pb2.RunBlpUntilRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.RunBlpUntilResponse.SerializeToString,
      ),
      'ResetReplication': grpc.unary_unary_rpc_method_handler(
          servicer.ResetReplication,
          request_deserializer=tabletmanagerdata__pb2.ResetReplicationRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.ResetReplicationResponse.SerializeToString,
      ),
      'InitMaster': grpc.unary_unary_rpc_method_handler(
          servicer.InitMaster,
          request_deserializer=tabletmanagerdata__pb2.InitMasterRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.InitMasterResponse.SerializeToString,
      ),
      'PopulateReparentJournal': grpc.unary_unary_rpc_method_handler(
          servicer.PopulateReparentJournal,
          request_deserializer=tabletmanagerdata__pb2.PopulateReparentJournalRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.PopulateReparentJournalResponse.SerializeToString,
      ),
      'InitSlave': grpc.unary_unary_rpc_method_handler(
          servicer.InitSlave,
          request_deserializer=tabletmanagerdata__pb2.InitSlaveRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.InitSlaveResponse.SerializeToString,
      ),
      'DemoteMaster': grpc.unary_unary_rpc_method_handler(
          servicer.DemoteMaster,
          request_deserializer=tabletmanagerdata__pb2.DemoteMasterRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.DemoteMasterResponse.SerializeToString,
      ),
      'PromoteSlaveWhenCaughtUp': grpc.unary_unary_rpc_method_handler(
          servicer.PromoteSlaveWhenCaughtUp,
          request_deserializer=tabletmanagerdata__pb2.PromoteSlaveWhenCaughtUpRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.PromoteSlaveWhenCaughtUpResponse.SerializeToString,
      ),
      'SlaveWasPromoted': grpc.unary_unary_rpc_method_handler(
          servicer.SlaveWasPromoted,
          request_deserializer=tabletmanagerdata__pb2.SlaveWasPromotedRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SlaveWasPromotedResponse.SerializeToString,
      ),
      'SetMaster': grpc.unary_unary_rpc_method_handler(
          servicer.SetMaster,
          request_deserializer=tabletmanagerdata__pb2.SetMasterRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SetMasterResponse.SerializeToString,
      ),
      'SlaveWasRestarted': grpc.unary_unary_rpc_method_handler(
          servicer.SlaveWasRestarted,
          request_deserializer=tabletmanagerdata__pb2.SlaveWasRestartedRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.SlaveWasRestartedResponse.SerializeToString,
      ),
      'StopReplicationAndGetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.StopReplicationAndGetStatus,
          request_deserializer=tabletmanagerdata__pb2.StopReplicationAndGetStatusRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.StopReplicationAndGetStatusResponse.SerializeToString,
      ),
      'PromoteSlave': grpc.unary_unary_rpc_method_handler(
          servicer.PromoteSlave,
          request_deserializer=tabletmanagerdata__pb2.PromoteSlaveRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.PromoteSlaveResponse.SerializeToString,
      ),
      'Backup': grpc.unary_stream_rpc_method_handler(
          servicer.Backup,
          request_deserializer=tabletmanagerdata__pb2.BackupRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.BackupResponse.SerializeToString,
      ),
      'RestoreFromBackup': grpc.unary_stream_rpc_method_handler(
          servicer.RestoreFromBackup,
          request_deserializer=tabletmanagerdata__pb2.RestoreFromBackupRequest.FromString,
          response_serializer=tabletmanagerdata__pb2.RestoreFromBackupResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tabletmanagerservice.TabletManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
