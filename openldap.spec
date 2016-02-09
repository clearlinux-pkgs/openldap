#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openldap
Version  : 2.4.44
Release  : 14
URL      : http://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-2.4.44.tgz
Source0  : http://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-2.4.44.tgz
Source1  : openldap.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : OLDAP-2.0.1 OLDAP-2.8 Zlib
Requires: openldap-bin
Requires: openldap-config
Requires: openldap-lib
Requires: openldap-doc
Requires: openldap-data
BuildRequires : db-dev
BuildRequires : groff
BuildRequires : openssl-dev
BuildRequires : pkgconfig(uuid)
Patch1: schemadir.patch

%description
For a description of what this distribution contains, see the
ANNOUNCEMENT file in this directory.  For a description of
changes from previous releases, see the CHANGES file in this
directory.

%package bin
Summary: bin components for the openldap package.
Group: Binaries
Requires: openldap-data
Requires: openldap-config

%description bin
bin components for the openldap package.


%package config
Summary: config components for the openldap package.
Group: Default

%description config
config components for the openldap package.


%package data
Summary: data components for the openldap package.
Group: Data

%description data
data components for the openldap package.


%package dev
Summary: dev components for the openldap package.
Group: Development
Requires: openldap-lib
Requires: openldap-bin
Requires: openldap-data
Provides: openldap-devel

%description dev
dev components for the openldap package.


%package doc
Summary: doc components for the openldap package.
Group: Documentation

%description doc
doc components for the openldap package.


%package lib
Summary: lib components for the openldap package.
Group: Libraries
Requires: openldap-data
Requires: openldap-config

%description lib
lib components for the openldap package.


%prep
%setup -q -n openldap-2.4.44
%patch1 -p1

%build
%configure --disable-static --enable-dynamic \
--disable-debug \
--enable-crypt \
--enable-modules \
--enable-rlookups \
--enable-backends=mod \
--enable-overlays=mod \
--disable-ndb \
--disable-sql
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/openldap.conf

%files
%defattr(-,root,root,-)
/var/openldap-data/DB_CONFIG.example

%files bin
%defattr(-,root,root,-)
/usr/bin/ldapadd
/usr/bin/ldapcompare
/usr/bin/ldapdelete
/usr/bin/ldapexop
/usr/bin/ldapmodify
/usr/bin/ldapmodrdn
/usr/bin/ldappasswd
/usr/bin/ldapsearch
/usr/bin/ldapurl
/usr/bin/ldapwhoami
/usr/bin/slapacl
/usr/bin/slapadd
/usr/bin/slapauth
/usr/bin/slapcat
/usr/bin/slapdn
/usr/bin/slapindex
/usr/bin/slappasswd
/usr/bin/slapschema
/usr/bin/slaptest
/usr/libexec/openldap/accesslog-2.4.so.2
/usr/libexec/openldap/accesslog-2.4.so.2.10.7
/usr/libexec/openldap/accesslog.so
/usr/libexec/openldap/auditlog-2.4.so.2
/usr/libexec/openldap/auditlog-2.4.so.2.10.7
/usr/libexec/openldap/auditlog.so
/usr/libexec/openldap/back_bdb-2.4.so.2
/usr/libexec/openldap/back_bdb-2.4.so.2.10.7
/usr/libexec/openldap/back_bdb.so
/usr/libexec/openldap/back_dnssrv-2.4.so.2
/usr/libexec/openldap/back_dnssrv-2.4.so.2.10.7
/usr/libexec/openldap/back_dnssrv.so
/usr/libexec/openldap/back_hdb-2.4.so.2
/usr/libexec/openldap/back_hdb-2.4.so.2.10.7
/usr/libexec/openldap/back_hdb.so
/usr/libexec/openldap/back_ldap-2.4.so.2
/usr/libexec/openldap/back_ldap-2.4.so.2.10.7
/usr/libexec/openldap/back_ldap.so
/usr/libexec/openldap/back_mdb-2.4.so.2
/usr/libexec/openldap/back_mdb-2.4.so.2.10.7
/usr/libexec/openldap/back_mdb.so
/usr/libexec/openldap/back_meta-2.4.so.2
/usr/libexec/openldap/back_meta-2.4.so.2.10.7
/usr/libexec/openldap/back_meta.so
/usr/libexec/openldap/back_monitor-2.4.so.2
/usr/libexec/openldap/back_monitor-2.4.so.2.10.7
/usr/libexec/openldap/back_monitor.so
/usr/libexec/openldap/back_null-2.4.so.2
/usr/libexec/openldap/back_null-2.4.so.2.10.7
/usr/libexec/openldap/back_null.so
/usr/libexec/openldap/back_passwd-2.4.so.2
/usr/libexec/openldap/back_passwd-2.4.so.2.10.7
/usr/libexec/openldap/back_passwd.so
/usr/libexec/openldap/back_perl-2.4.so.2
/usr/libexec/openldap/back_perl-2.4.so.2.10.7
/usr/libexec/openldap/back_perl.so
/usr/libexec/openldap/back_relay-2.4.so.2
/usr/libexec/openldap/back_relay-2.4.so.2.10.7
/usr/libexec/openldap/back_relay.so
/usr/libexec/openldap/back_shell-2.4.so.2
/usr/libexec/openldap/back_shell-2.4.so.2.10.7
/usr/libexec/openldap/back_shell.so
/usr/libexec/openldap/back_sock-2.4.so.2
/usr/libexec/openldap/back_sock-2.4.so.2.10.7
/usr/libexec/openldap/back_sock.so
/usr/libexec/openldap/collect-2.4.so.2
/usr/libexec/openldap/collect-2.4.so.2.10.7
/usr/libexec/openldap/collect.so
/usr/libexec/openldap/constraint-2.4.so.2
/usr/libexec/openldap/constraint-2.4.so.2.10.7
/usr/libexec/openldap/constraint.so
/usr/libexec/openldap/dds-2.4.so.2
/usr/libexec/openldap/dds-2.4.so.2.10.7
/usr/libexec/openldap/dds.so
/usr/libexec/openldap/deref-2.4.so.2
/usr/libexec/openldap/deref-2.4.so.2.10.7
/usr/libexec/openldap/deref.so
/usr/libexec/openldap/dyngroup-2.4.so.2
/usr/libexec/openldap/dyngroup-2.4.so.2.10.7
/usr/libexec/openldap/dyngroup.so
/usr/libexec/openldap/dynlist-2.4.so.2
/usr/libexec/openldap/dynlist-2.4.so.2.10.7
/usr/libexec/openldap/dynlist.so
/usr/libexec/openldap/memberof-2.4.so.2
/usr/libexec/openldap/memberof-2.4.so.2.10.7
/usr/libexec/openldap/memberof.so
/usr/libexec/openldap/pcache-2.4.so.2
/usr/libexec/openldap/pcache-2.4.so.2.10.7
/usr/libexec/openldap/pcache.so
/usr/libexec/openldap/ppolicy-2.4.so.2
/usr/libexec/openldap/ppolicy-2.4.so.2.10.7
/usr/libexec/openldap/ppolicy.so
/usr/libexec/openldap/refint-2.4.so.2
/usr/libexec/openldap/refint-2.4.so.2.10.7
/usr/libexec/openldap/refint.so
/usr/libexec/openldap/retcode-2.4.so.2
/usr/libexec/openldap/retcode-2.4.so.2.10.7
/usr/libexec/openldap/retcode.so
/usr/libexec/openldap/rwm-2.4.so.2
/usr/libexec/openldap/rwm-2.4.so.2.10.7
/usr/libexec/openldap/rwm.so
/usr/libexec/openldap/seqmod-2.4.so.2
/usr/libexec/openldap/seqmod-2.4.so.2.10.7
/usr/libexec/openldap/seqmod.so
/usr/libexec/openldap/sssvlv-2.4.so.2
/usr/libexec/openldap/sssvlv-2.4.so.2.10.7
/usr/libexec/openldap/sssvlv.so
/usr/libexec/openldap/syncprov-2.4.so.2
/usr/libexec/openldap/syncprov-2.4.so.2.10.7
/usr/libexec/openldap/syncprov.so
/usr/libexec/openldap/translucent-2.4.so.2
/usr/libexec/openldap/translucent-2.4.so.2.10.7
/usr/libexec/openldap/translucent.so
/usr/libexec/openldap/unique-2.4.so.2
/usr/libexec/openldap/unique-2.4.so.2.10.7
/usr/libexec/openldap/unique.so
/usr/libexec/openldap/valsort-2.4.so.2
/usr/libexec/openldap/valsort-2.4.so.2.10.7
/usr/libexec/openldap/valsort.so
/usr/libexec/slapd

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/openldap.conf

%files data
%defattr(-,root,root,-)
/usr/share/openldap/schema/README
/usr/share/openldap/schema/collective.ldif
/usr/share/openldap/schema/collective.schema
/usr/share/openldap/schema/corba.ldif
/usr/share/openldap/schema/corba.schema
/usr/share/openldap/schema/core.ldif
/usr/share/openldap/schema/core.schema
/usr/share/openldap/schema/cosine.ldif
/usr/share/openldap/schema/cosine.schema
/usr/share/openldap/schema/duaconf.ldif
/usr/share/openldap/schema/duaconf.schema
/usr/share/openldap/schema/dyngroup.ldif
/usr/share/openldap/schema/dyngroup.schema
/usr/share/openldap/schema/inetorgperson.ldif
/usr/share/openldap/schema/inetorgperson.schema
/usr/share/openldap/schema/java.ldif
/usr/share/openldap/schema/java.schema
/usr/share/openldap/schema/misc.ldif
/usr/share/openldap/schema/misc.schema
/usr/share/openldap/schema/nis.ldif
/usr/share/openldap/schema/nis.schema
/usr/share/openldap/schema/openldap.ldif
/usr/share/openldap/schema/openldap.schema
/usr/share/openldap/schema/pmi.ldif
/usr/share/openldap/schema/pmi.schema
/usr/share/openldap/schema/ppolicy.ldif
/usr/share/openldap/schema/ppolicy.schema

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
