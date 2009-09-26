# Copyright (c) 2009 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'includes': [
    '../../build/common.gypi',
  ],
  'target_defaults': {
    'defines': [
      'FEATURE_ENABLE_SSL',
      'FEATURE_ENABLE_VOICEMAIL',  # TODO(ncarter): Do we really need this?
      '_USE_32BIT_TIME_T',
      'SAFE_TO_DEFINE_TALK_BASE_LOGGING_MACROS',
    ],
    'include_dirs': [
      './overrides',
      './files',
    ],
    'dependencies': [
      '../expat/expat.gyp:expat',
      '../../base/base.gyp:base',
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        './overrides',
        './files',
      ],
      'defines': [
        'FEATURE_ENABLE_SSL',
        'FEATURE_ENABLE_VOICEMAIL',
      ],
    },
    'conditions': [
      ['OS=="win"', {
        'include_dirs': [
          '../third_party/platformsdk_win2008_6_1/files/Include',
        ],
      }],
      ['OS=="linux"', {
        'defines': [
          'POSIX',
        ],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'libjingle',
      'type': '<(library)',
      'sources': [

        # 'files/talk/p2p/client/socketmonitor.cc',  # unneeded
        # 'files/talk/p2p/client/socketmonitor.h',   # unneeded
        # 'files/talk/base/Equifax_Secure_Global_eBusiness_CA-1.h', # openssl
        # 'files/talk/base/basictypes.h',  # overridden
        # 'files/talk/base/natserver_main.cc',  # has a main()
        # 'files/talk/base/openssladapter.cc',  # openssl
        # 'files/talk/base/openssladapter.h',   # openssl
        'files/talk/base/asynchttprequest.cc',
        'files/talk/base/asynchttprequest.h',
        'files/talk/base/asyncpacketsocket.cc',
        'files/talk/base/asyncpacketsocket.h',
        'files/talk/base/asynctcpsocket.h',
        'files/talk/base/asyncudpsocket.cc',
        'files/talk/base/asyncudpsocket.h',
        'files/talk/base/autodetectproxy.cc',
        'files/talk/base/autodetectproxy.h',
        'files/talk/base/base64.cc',
        'files/talk/base/base64.h',
        'files/talk/base/basicdefs.h',
        'files/talk/base/bytebuffer.cc',
        'files/talk/base/bytebuffer.h',
        'files/talk/base/common.cc',
        'files/talk/base/common.h',
        'files/talk/base/criticalsection.h',
        'files/talk/base/cryptstring.h',
        'files/talk/base/diskcache.cc',
        'files/talk/base/diskcache.h',
        'files/talk/base/diskcachestd.cc',
        'files/talk/base/diskcachestd.h',
        'files/talk/base/fileutils.cc',
        'files/talk/base/fileutils.h',
        'files/talk/base/firewallsocketserver.cc',
        'files/talk/base/firewallsocketserver.h',
        'files/talk/base/helpers.cc',
        'files/talk/base/helpers.h',
        'files/talk/base/host.cc',
        'files/talk/base/host.h',
        'files/talk/base/httpbase.cc',
        'files/talk/base/httpbase.h',
        'files/talk/base/httpclient.cc',
        'files/talk/base/httpclient.h',
        'files/talk/base/httpcommon-inl.h',
        'files/talk/base/httpcommon.cc',
        'files/talk/base/httpcommon.h',
        'files/talk/base/httpserver.cc',
        'files/talk/base/httpserver.h',
        'files/talk/base/logging.cc',
        'files/talk/base/logging.h',
        'files/talk/base/md5c.c',
        'files/talk/base/md5c.h',
        'files/talk/base/messagequeue.cc',
        'files/talk/base/messagequeue.h',
        'files/talk/base/natserver.cc',
        'files/talk/base/natserver.h',
        'files/talk/base/natsocketfactory.cc',
        'files/talk/base/natsocketfactory.h',
        'files/talk/base/nattypes.cc',
        'files/talk/base/nattypes.h',
        'files/talk/base/network.cc',
        'files/talk/base/network.h',
        'files/talk/base/pathutils.cc',
        'files/talk/base/pathutils.h',
        'files/talk/base/physicalsocketserver.cc',
        'files/talk/base/physicalsocketserver.h',
        'files/talk/base/proxydetect.cc',
        'files/talk/base/proxydetect.h',
        'files/talk/base/proxyinfo.cc',
        'files/talk/base/proxyinfo.h',
        'files/talk/base/signalthread.cc',
        'files/talk/base/signalthread.h',
        'files/talk/base/socketadapters.cc',
        'files/talk/base/socketadapters.h',
        'files/talk/base/socketaddress.cc',
        'files/talk/base/socketaddress.h',
        'files/talk/base/socketaddresspair.cc',
        'files/talk/base/socketaddresspair.h',
        'files/talk/base/socketfactory.h',
        'files/talk/base/socketpool.cc',
        'files/talk/base/socketpool.h',
        'files/talk/base/socketserver.h',
        'files/talk/base/socketstream.h',
        'files/talk/base/ssladapter.cc',
        'files/talk/base/ssladapter.h',
        'files/talk/base/stl_decl.h',
        'files/talk/base/stream.cc',
        'files/talk/base/stream.h',
        'files/talk/base/streamutils.cc',
        'files/talk/base/streamutils.h',
        'files/talk/base/stringdigest.cc',
        'files/talk/base/stringdigest.h',
        'files/talk/base/stringencode.cc',
        'files/talk/base/stringencode.h',
        'files/talk/base/stringutils.cc',
        'files/talk/base/stringutils.h',
        'files/talk/base/tarstream.cc',
        'files/talk/base/tarstream.h',
        'files/talk/base/task.cc',
        'files/talk/base/task.h',
        'files/talk/base/taskrunner.cc',
        'files/talk/base/taskrunner.h',
        'files/talk/base/testclient.cc',
        'files/talk/base/testclient.h',
        'files/talk/base/thread.cc',
        'files/talk/base/thread.h',
        'files/talk/base/time.cc',
        'files/talk/base/time.h',
        'files/talk/base/urlencode.cc',
        'files/talk/base/urlencode.h',
        'files/talk/base/virtualsocketserver.cc',
        'files/talk/base/virtualsocketserver.h',
        'files/talk/p2p/base/candidate.h',
        'files/talk/p2p/base/common.h',
        'files/talk/p2p/base/constants.cc',
        'files/talk/p2p/base/constants.h',
        'files/talk/p2p/base/p2ptransport.cc',
        'files/talk/p2p/base/p2ptransport.h',
        'files/talk/p2p/base/p2ptransportchannel.cc',
        'files/talk/p2p/base/p2ptransportchannel.h',
        'files/talk/p2p/base/port.cc',
        'files/talk/p2p/base/port.h',
        'files/talk/p2p/base/portallocator.h',
        'files/talk/p2p/base/rawtransport.cc',
        'files/talk/p2p/base/rawtransport.h',
        'files/talk/p2p/base/rawtransportchannel.cc',
        'files/talk/p2p/base/rawtransportchannel.h',
        'files/talk/p2p/base/relayport.cc',
        'files/talk/p2p/base/relayport.h',
        'files/talk/p2p/base/session.cc',
        'files/talk/p2p/base/session.h',
        'files/talk/p2p/base/sessionclient.h',
        'files/talk/p2p/base/sessiondescription.h',
        'files/talk/p2p/base/sessionid.h',
        'files/talk/p2p/base/sessionmanager.cc',
        'files/talk/p2p/base/sessionmanager.h',
        'files/talk/p2p/base/stun.cc',
        'files/talk/p2p/base/stun.h',
        'files/talk/p2p/base/stunport.cc',
        'files/talk/p2p/base/stunport.h',
        'files/talk/p2p/base/stunrequest.cc',
        'files/talk/p2p/base/stunrequest.h',
        'files/talk/p2p/base/tcpport.cc',
        'files/talk/p2p/base/tcpport.h',
        'files/talk/p2p/base/transport.cc',
        'files/talk/p2p/base/transport.h',
        'files/talk/p2p/base/transportchannel.cc',
        'files/talk/p2p/base/transportchannel.h',
        'files/talk/p2p/base/transportchannelimpl.h',
        'files/talk/p2p/base/transportchannelproxy.cc',
        'files/talk/p2p/base/transportchannelproxy.h',
        'files/talk/p2p/base/udpport.cc',
        'files/talk/p2p/base/udpport.h',
        'files/talk/p2p/client/basicportallocator.cc',
        'files/talk/p2p/client/basicportallocator.h',
        'files/talk/p2p/client/httpportallocator.cc',
        'files/talk/p2p/client/httpportallocator.h',
        'files/talk/xmllite/qname.cc',
        'files/talk/xmllite/qname.h',
        'files/talk/xmllite/xmlbuilder.cc',
        'files/talk/xmllite/xmlbuilder.h',
        'files/talk/xmllite/xmlconstants.cc',
        'files/talk/xmllite/xmlconstants.h',
        'files/talk/xmllite/xmlelement.cc',
        'files/talk/xmllite/xmlelement.h',
        'files/talk/xmllite/xmlnsstack.cc',
        'files/talk/xmllite/xmlnsstack.h',
        'files/talk/xmllite/xmlparser.cc',
        'files/talk/xmllite/xmlparser.h',
        'files/talk/xmllite/xmlprinter.cc',
        'files/talk/xmllite/xmlprinter.h',
        'files/talk/xmpp/jid.cc',
        'files/talk/xmpp/jid.h',
        'files/talk/xmpp/ratelimitmanager.cc',
        'files/talk/xmpp/ratelimitmanager.h',
        'files/talk/xmpp/saslmechanism.cc',
        'files/talk/xmpp/saslmechanism.h',
        'files/talk/xmpp/xmppclient.cc',
        'files/talk/xmpp/xmppclient.h',
        'files/talk/xmpp/xmppconstants.cc',
        'files/talk/xmpp/xmppconstants.h',
        'files/talk/xmpp/xmppengineimpl.cc',
        'files/talk/xmpp/xmppengineimpl.h',
        'files/talk/xmpp/xmppengineimpl_iq.cc',
        'files/talk/xmpp/xmppengineimpl_iq.h',
        'files/talk/xmpp/xmpplogintask.cc',
        'files/talk/xmpp/xmpplogintask.h',
        'files/talk/xmpp/xmppstanzaparser.cc',
        'files/talk/xmpp/xmppstanzaparser.h',
        'files/talk/xmpp/xmpptask.cc',
        'files/talk/xmpp/xmpptask.h',
        'overrides/talk/base/basictypes.h',
        'overrides/talk/base/constructormagic.h',
        'overrides/talk/base/scoped_ptr.h',
        'overrides/config.h',
      ],
      'conditions': [
        ['OS=="win"', {
          'sources': [
            'files/talk/base/convert.h',  # win32 only
            'files/talk/base/diskcache_win32.cc',  # win32 only
            'files/talk/base/diskcache_win32.h',   # win32 only
            'files/talk/base/schanneladapter.cc',
            'files/talk/base/schanneladapter.h',
            'files/talk/base/win32.h',
            'files/talk/base/win32filesystem.cc',
            'files/talk/base/win32filesystem.h',
            'files/talk/base/win32socketserver.cc',
            'files/talk/base/win32socketserver.h',
            'files/talk/base/win32window.h',
            'files/talk/base/winfirewall.cc',
            'files/talk/base/winfirewall.h',
            'files/talk/base/winping.cc',
            'files/talk/base/winping.h',
          ],
        }],
      ],
    },
  ],
}

