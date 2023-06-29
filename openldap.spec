#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x7F67D5FD1CE1CBCE (project@openldap.org)
#
Name     : openldap
Version  : 2.6.4
Release  : 58
URL      : https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-2.6.4.tgz
Source0  : https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-2.6.4.tgz
Source1  : openldap.tmpfiles
Source2  : https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-2.6.4.tgz.asc
Summary  : OpenLDAP Lightweight ASN.1 Basic Encoding Rules library
Group    : Development/Tools
License  : OLDAP-2.0.1 OLDAP-2.8 Zlib
Requires: openldap-bin = %{version}-%{release}
Requires: openldap-config = %{version}-%{release}
Requires: openldap-data = %{version}-%{release}
Requires: openldap-lib = %{version}-%{release}
Requires: openldap-libexec = %{version}-%{release}
Requires: openldap-license = %{version}-%{release}
Requires: openldap-man = %{version}-%{release}
Requires: openldap-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : cyrus-sasl-dev
BuildRequires : groff
BuildRequires : openssl-dev
BuildRequires : pkgconfig(uuid)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-stateless.patch

%description
For a description of what this distribution contains, see the
ANNOUNCEMENT file in this directory.  For a description of
changes from previous releases, see the CHANGES file in this
directory.

%package bin
Summary: bin components for the openldap package.
Group: Binaries
Requires: openldap-data = %{version}-%{release}
Requires: openldap-libexec = %{version}-%{release}
Requires: openldap-config = %{version}-%{release}
Requires: openldap-license = %{version}-%{release}
Requires: openldap-services = %{version}-%{release}

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
Requires: openldap-lib = %{version}-%{release}
Requires: openldap-bin = %{version}-%{release}
Requires: openldap-data = %{version}-%{release}
Provides: openldap-devel = %{version}-%{release}
Requires: openldap = %{version}-%{release}

%description dev
dev components for the openldap package.


%package extras
Summary: extras components for the openldap package.
Group: Default

%description extras
extras components for the openldap package.


%package lib
Summary: lib components for the openldap package.
Group: Libraries
Requires: openldap-data = %{version}-%{release}
Requires: openldap-libexec = %{version}-%{release}
Requires: openldap-license = %{version}-%{release}

%description lib
lib components for the openldap package.


%package libexec
Summary: libexec components for the openldap package.
Group: Default
Requires: openldap-config = %{version}-%{release}
Requires: openldap-license = %{version}-%{release}

%description libexec
libexec components for the openldap package.


%package license
Summary: license components for the openldap package.
Group: Default

%description license
license components for the openldap package.


%package man
Summary: man components for the openldap package.
Group: Default

%description man
man components for the openldap package.


%package services
Summary: services components for the openldap package.
Group: Systemd services
Requires: systemd

%description services
services components for the openldap package.


%prep
%setup -q -n openldap-2.6.4
cd %{_builddir}/openldap-2.6.4
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688073309
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --enable-dynamic \
--disable-debug \
--enable-crypt \
--enable-modules \
--enable-rlookups \
--enable-backends=mod \
--enable-overlays=mod \
--disable-ndb \
--disable-sql \
--with-tls=openssl \
--with-cyrus-sasl \
--enable-ipv6=yes \
--enable-lmpasswd \
--enable-spasswd \
--with-gnu-ld \
--with-pic \
--disable-bdb \
--disable-hdb \
--disable-wt
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1688073309
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openldap
cp %{_builddir}/openldap-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/openldap/bc06cbdf781c87d2df2fe385214f936d010dd2a2 || :
cp %{_builddir}/openldap-%{version}/build/LICENSE-2.0.1 %{buildroot}/usr/share/package-licenses/openldap/09fc2e9f527fcb0d594bc658d21e42d3a5124b83 || :
cp %{_builddir}/openldap-%{version}/contrib/slapd-modules/ppm/LICENSE %{buildroot}/usr/share/package-licenses/openldap/7d003e7541a517109ed166c1db227c0f21ca3db6 || :
cp %{_builddir}/openldap-%{version}/libraries/liblmdb/COPYRIGHT %{buildroot}/usr/share/package-licenses/openldap/7578422c24f1c556f2a5884294bdf7a545a53a64 || :
cp %{_builddir}/openldap-%{version}/libraries/liblmdb/LICENSE %{buildroot}/usr/share/package-licenses/openldap/bc06cbdf781c87d2df2fe385214f936d010dd2a2 || :
cp %{_builddir}/openldap-%{version}/libraries/librewrite/Copyright %{buildroot}/usr/share/package-licenses/openldap/0da054d8429802e25641decec43d4fbc1fbe4f2f || :
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/openldap.conf
## Remove excluded files
rm -f %{buildroot}*/etc/openldap/ldap.conf
rm -f %{buildroot}*/etc/openldap/ldap.conf.default
rm -f %{buildroot}*/etc/openldap/DB_CONFIG.example
rm -f %{buildroot}*/etc/openldap/slapd.conf
rm -f %{buildroot}*/etc/openldap/slapd.conf.default
rm -f %{buildroot}*/etc/openldap/slapd.ldif
rm -f %{buildroot}*/etc/openldap/slapd.ldif.default
rm -f %{buildroot}*/var/openldap-data/DB_CONFIG.example

%files
%defattr(-,root,root,-)

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
/usr/bin/ldapvc
/usr/bin/ldapwhoami
/usr/bin/slapacl
/usr/bin/slapadd
/usr/bin/slapauth
/usr/bin/slapcat
/usr/bin/slapdn
/usr/bin/slapindex
/usr/bin/slapmodify
/usr/bin/slappasswd
/usr/bin/slapschema
/usr/bin/slaptest

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
/usr/share/openldap/schema/dsee.ldif
/usr/share/openldap/schema/dsee.schema
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
/usr/share/openldap/schema/msuser.ldif
/usr/share/openldap/schema/msuser.schema
/usr/share/openldap/schema/namedobject.ldif
/usr/share/openldap/schema/namedobject.schema
/usr/share/openldap/schema/nis.ldif
/usr/share/openldap/schema/nis.schema
/usr/share/openldap/schema/openldap.ldif
/usr/share/openldap/schema/openldap.schema
/usr/share/openldap/schema/pmi.ldif
/usr/share/openldap/schema/pmi.schema

%files dev
%defattr(-,root,root,-)
/usr/include/lber.h
/usr/include/lber_types.h
/usr/include/ldap.h
/usr/include/ldap_cdefs.h
/usr/include/ldap_features.h
/usr/include/ldap_schema.h
/usr/include/ldap_utf8.h
/usr/include/ldif.h
/usr/include/openldap.h
/usr/include/slapi-plugin.h
/usr/lib64/liblber.so
/usr/lib64/libldap.so
/usr/lib64/pkgconfig/lber.pc
/usr/lib64/pkgconfig/ldap.pc
/usr/share/man/man3/ber_alloc_t.3
/usr/share/man/man3/ber_bvarray_add.3
/usr/share/man/man3/ber_bvarray_free.3
/usr/share/man/man3/ber_bvdup.3
/usr/share/man/man3/ber_bvecadd.3
/usr/share/man/man3/ber_bvecfree.3
/usr/share/man/man3/ber_bvfree.3
/usr/share/man/man3/ber_bvstr.3
/usr/share/man/man3/ber_bvstrdup.3
/usr/share/man/man3/ber_dupbv.3
/usr/share/man/man3/ber_first_element.3
/usr/share/man/man3/ber_flush.3
/usr/share/man/man3/ber_free.3
/usr/share/man/man3/ber_get_bitstring.3
/usr/share/man/man3/ber_get_boolean.3
/usr/share/man/man3/ber_get_enum.3
/usr/share/man/man3/ber_get_int.3
/usr/share/man/man3/ber_get_next.3
/usr/share/man/man3/ber_get_null.3
/usr/share/man/man3/ber_get_stringa.3
/usr/share/man/man3/ber_get_stringb.3
/usr/share/man/man3/ber_next_element.3
/usr/share/man/man3/ber_peek_tag.3
/usr/share/man/man3/ber_printf.3
/usr/share/man/man3/ber_put_enum.3
/usr/share/man/man3/ber_put_int.3
/usr/share/man/man3/ber_put_null.3
/usr/share/man/man3/ber_put_ostring.3
/usr/share/man/man3/ber_put_seq.3
/usr/share/man/man3/ber_put_set.3
/usr/share/man/man3/ber_put_string.3
/usr/share/man/man3/ber_scanf.3
/usr/share/man/man3/ber_skip_tag.3
/usr/share/man/man3/ber_start_set.3
/usr/share/man/man3/ber_str2bv.3
/usr/share/man/man3/lber-decode.3
/usr/share/man/man3/lber-encode.3
/usr/share/man/man3/lber-memory.3
/usr/share/man/man3/lber-sockbuf.3
/usr/share/man/man3/lber-types.3
/usr/share/man/man3/ld_errno.3
/usr/share/man/man3/ldap.3
/usr/share/man/man3/ldap_abandon.3
/usr/share/man/man3/ldap_abandon_ext.3
/usr/share/man/man3/ldap_add.3
/usr/share/man/man3/ldap_add_ext.3
/usr/share/man/man3/ldap_add_ext_s.3
/usr/share/man/man3/ldap_add_s.3
/usr/share/man/man3/ldap_attributetype2name.3
/usr/share/man/man3/ldap_attributetype2str.3
/usr/share/man/man3/ldap_attributetype_free.3
/usr/share/man/man3/ldap_bind.3
/usr/share/man/man3/ldap_bind_s.3
/usr/share/man/man3/ldap_compare.3
/usr/share/man/man3/ldap_compare_ext.3
/usr/share/man/man3/ldap_compare_ext_s.3
/usr/share/man/man3/ldap_compare_s.3
/usr/share/man/man3/ldap_control_create.3
/usr/share/man/man3/ldap_control_dup.3
/usr/share/man/man3/ldap_control_find.3
/usr/share/man/man3/ldap_control_free.3
/usr/share/man/man3/ldap_controls.3
/usr/share/man/man3/ldap_controls_dup.3
/usr/share/man/man3/ldap_controls_free.3
/usr/share/man/man3/ldap_count_entries.3
/usr/share/man/man3/ldap_count_messages.3
/usr/share/man/man3/ldap_count_references.3
/usr/share/man/man3/ldap_count_values.3
/usr/share/man/man3/ldap_count_values_len.3
/usr/share/man/man3/ldap_dcedn2dn.3
/usr/share/man/man3/ldap_delete.3
/usr/share/man/man3/ldap_delete_ext.3
/usr/share/man/man3/ldap_delete_ext_s.3
/usr/share/man/man3/ldap_delete_s.3
/usr/share/man/man3/ldap_destroy.3
/usr/share/man/man3/ldap_dn2ad_canonical.3
/usr/share/man/man3/ldap_dn2dcedn.3
/usr/share/man/man3/ldap_dn2str.3
/usr/share/man/man3/ldap_dn2ufn.3
/usr/share/man/man3/ldap_dnfree.3
/usr/share/man/man3/ldap_dup.3
/usr/share/man/man3/ldap_err2string.3
/usr/share/man/man3/ldap_errlist.3
/usr/share/man/man3/ldap_error.3
/usr/share/man/man3/ldap_explode_dn.3
/usr/share/man/man3/ldap_explode_rdn.3
/usr/share/man/man3/ldap_extended_operation.3
/usr/share/man/man3/ldap_extended_operation_s.3
/usr/share/man/man3/ldap_first_attribute.3
/usr/share/man/man3/ldap_first_entry.3
/usr/share/man/man3/ldap_first_message.3
/usr/share/man/man3/ldap_first_reference.3
/usr/share/man/man3/ldap_free_urldesc.3
/usr/share/man/man3/ldap_get_attribute_ber.3
/usr/share/man/man3/ldap_get_dn.3
/usr/share/man/man3/ldap_get_option.3
/usr/share/man/man3/ldap_get_values.3
/usr/share/man/man3/ldap_get_values_len.3
/usr/share/man/man3/ldap_init.3
/usr/share/man/man3/ldap_init_fd.3
/usr/share/man/man3/ldap_initialize.3
/usr/share/man/man3/ldap_install_tls.3
/usr/share/man/man3/ldap_is_ldap_url.3
/usr/share/man/man3/ldap_matchingrule2name.3
/usr/share/man/man3/ldap_matchingrule2str.3
/usr/share/man/man3/ldap_matchingrule_free.3
/usr/share/man/man3/ldap_memalloc.3
/usr/share/man/man3/ldap_memcalloc.3
/usr/share/man/man3/ldap_memfree.3
/usr/share/man/man3/ldap_memory.3
/usr/share/man/man3/ldap_memrealloc.3
/usr/share/man/man3/ldap_memvfree.3
/usr/share/man/man3/ldap_modify.3
/usr/share/man/man3/ldap_modify_ext.3
/usr/share/man/man3/ldap_modify_ext_s.3
/usr/share/man/man3/ldap_modify_s.3
/usr/share/man/man3/ldap_modrdn.3
/usr/share/man/man3/ldap_modrdn2.3
/usr/share/man/man3/ldap_modrdn2_s.3
/usr/share/man/man3/ldap_modrdn_s.3
/usr/share/man/man3/ldap_mods_free.3
/usr/share/man/man3/ldap_msgfree.3
/usr/share/man/man3/ldap_msgid.3
/usr/share/man/man3/ldap_msgtype.3
/usr/share/man/man3/ldap_next_attribute.3
/usr/share/man/man3/ldap_next_entry.3
/usr/share/man/man3/ldap_next_message.3
/usr/share/man/man3/ldap_next_reference.3
/usr/share/man/man3/ldap_objectclass2name.3
/usr/share/man/man3/ldap_objectclass2str.3
/usr/share/man/man3/ldap_objectclass_free.3
/usr/share/man/man3/ldap_open.3
/usr/share/man/man3/ldap_parse_extended_result.3
/usr/share/man/man3/ldap_parse_intermediate.3
/usr/share/man/man3/ldap_parse_reference.3
/usr/share/man/man3/ldap_parse_result.3
/usr/share/man/man3/ldap_parse_sasl_bind_result.3
/usr/share/man/man3/ldap_parse_sort_control.3
/usr/share/man/man3/ldap_parse_vlv_control.3
/usr/share/man/man3/ldap_perror.3
/usr/share/man/man3/ldap_rename.3
/usr/share/man/man3/ldap_rename_s.3
/usr/share/man/man3/ldap_result.3
/usr/share/man/man3/ldap_result2error.3
/usr/share/man/man3/ldap_sasl_bind.3
/usr/share/man/man3/ldap_sasl_bind_s.3
/usr/share/man/man3/ldap_schema.3
/usr/share/man/man3/ldap_scherr2str.3
/usr/share/man/man3/ldap_search.3
/usr/share/man/man3/ldap_search_ext.3
/usr/share/man/man3/ldap_search_ext_s.3
/usr/share/man/man3/ldap_search_s.3
/usr/share/man/man3/ldap_search_st.3
/usr/share/man/man3/ldap_set_option.3
/usr/share/man/man3/ldap_set_rebind_proc.3
/usr/share/man/man3/ldap_set_urllist_proc.3
/usr/share/man/man3/ldap_simple_bind.3
/usr/share/man/man3/ldap_simple_bind_s.3
/usr/share/man/man3/ldap_sort.3
/usr/share/man/man3/ldap_sort_entries.3
/usr/share/man/man3/ldap_sort_strcasecmp.3
/usr/share/man/man3/ldap_sort_values.3
/usr/share/man/man3/ldap_start_tls.3
/usr/share/man/man3/ldap_start_tls_s.3
/usr/share/man/man3/ldap_str2attributetype.3
/usr/share/man/man3/ldap_str2dn.3
/usr/share/man/man3/ldap_str2matchingrule.3
/usr/share/man/man3/ldap_str2objectclass.3
/usr/share/man/man3/ldap_str2syntax.3
/usr/share/man/man3/ldap_strdup.3
/usr/share/man/man3/ldap_sync.3
/usr/share/man/man3/ldap_syntax2name.3
/usr/share/man/man3/ldap_syntax2str.3
/usr/share/man/man3/ldap_syntax_free.3
/usr/share/man/man3/ldap_tls.3
/usr/share/man/man3/ldap_tls_inplace.3
/usr/share/man/man3/ldap_unbind.3
/usr/share/man/man3/ldap_unbind_ext.3
/usr/share/man/man3/ldap_unbind_ext_s.3
/usr/share/man/man3/ldap_unbind_s.3
/usr/share/man/man3/ldap_url.3
/usr/share/man/man3/ldap_url_parse.3
/usr/share/man/man3/ldap_value_free.3
/usr/share/man/man3/ldap_value_free_len.3

%files extras
%defattr(-,root,root,-)
/usr/libexec/openldap/back_perl.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblber.so.2
/usr/lib64/liblber.so.2.0.200
/usr/lib64/libldap.so.2
/usr/lib64/libldap.so.2.0.200

%files libexec
%defattr(-,root,root,-)
/usr/libexec/openldap/accesslog.so
/usr/libexec/openldap/accesslog.so.2
/usr/libexec/openldap/accesslog.so.2.0.200
/usr/libexec/openldap/auditlog.so
/usr/libexec/openldap/auditlog.so.2
/usr/libexec/openldap/auditlog.so.2.0.200
/usr/libexec/openldap/autoca.so
/usr/libexec/openldap/autoca.so.2
/usr/libexec/openldap/autoca.so.2.0.200
/usr/libexec/openldap/back_asyncmeta.so
/usr/libexec/openldap/back_asyncmeta.so.2
/usr/libexec/openldap/back_asyncmeta.so.2.0.200
/usr/libexec/openldap/back_dnssrv.so
/usr/libexec/openldap/back_dnssrv.so.2
/usr/libexec/openldap/back_dnssrv.so.2.0.200
/usr/libexec/openldap/back_ldap.so
/usr/libexec/openldap/back_ldap.so.2
/usr/libexec/openldap/back_ldap.so.2.0.200
/usr/libexec/openldap/back_mdb.so
/usr/libexec/openldap/back_mdb.so.2
/usr/libexec/openldap/back_mdb.so.2.0.200
/usr/libexec/openldap/back_meta.so
/usr/libexec/openldap/back_meta.so.2
/usr/libexec/openldap/back_meta.so.2.0.200
/usr/libexec/openldap/back_null.so
/usr/libexec/openldap/back_null.so.2
/usr/libexec/openldap/back_null.so.2.0.200
/usr/libexec/openldap/back_passwd.so
/usr/libexec/openldap/back_passwd.so.2
/usr/libexec/openldap/back_passwd.so.2.0.200
/usr/libexec/openldap/back_perl.so.2
/usr/libexec/openldap/back_perl.so.2.0.200
/usr/libexec/openldap/back_relay.so
/usr/libexec/openldap/back_relay.so.2
/usr/libexec/openldap/back_relay.so.2.0.200
/usr/libexec/openldap/back_sock.so
/usr/libexec/openldap/back_sock.so.2
/usr/libexec/openldap/back_sock.so.2.0.200
/usr/libexec/openldap/collect.so
/usr/libexec/openldap/collect.so.2
/usr/libexec/openldap/collect.so.2.0.200
/usr/libexec/openldap/constraint.so
/usr/libexec/openldap/constraint.so.2
/usr/libexec/openldap/constraint.so.2.0.200
/usr/libexec/openldap/dds.so
/usr/libexec/openldap/dds.so.2
/usr/libexec/openldap/dds.so.2.0.200
/usr/libexec/openldap/deref.so
/usr/libexec/openldap/deref.so.2
/usr/libexec/openldap/deref.so.2.0.200
/usr/libexec/openldap/dyngroup.so
/usr/libexec/openldap/dyngroup.so.2
/usr/libexec/openldap/dyngroup.so.2.0.200
/usr/libexec/openldap/dynlist.so
/usr/libexec/openldap/dynlist.so.2
/usr/libexec/openldap/dynlist.so.2.0.200
/usr/libexec/openldap/homedir.so
/usr/libexec/openldap/homedir.so.2
/usr/libexec/openldap/homedir.so.2.0.200
/usr/libexec/openldap/memberof.so
/usr/libexec/openldap/memberof.so.2
/usr/libexec/openldap/memberof.so.2.0.200
/usr/libexec/openldap/otp.so
/usr/libexec/openldap/otp.so.2
/usr/libexec/openldap/otp.so.2.0.200
/usr/libexec/openldap/pcache.so
/usr/libexec/openldap/pcache.so.2
/usr/libexec/openldap/pcache.so.2.0.200
/usr/libexec/openldap/ppolicy.so
/usr/libexec/openldap/ppolicy.so.2
/usr/libexec/openldap/ppolicy.so.2.0.200
/usr/libexec/openldap/refint.so
/usr/libexec/openldap/refint.so.2
/usr/libexec/openldap/refint.so.2.0.200
/usr/libexec/openldap/remoteauth.so
/usr/libexec/openldap/remoteauth.so.2
/usr/libexec/openldap/remoteauth.so.2.0.200
/usr/libexec/openldap/retcode.so
/usr/libexec/openldap/retcode.so.2
/usr/libexec/openldap/retcode.so.2.0.200
/usr/libexec/openldap/rwm.so
/usr/libexec/openldap/rwm.so.2
/usr/libexec/openldap/rwm.so.2.0.200
/usr/libexec/openldap/seqmod.so
/usr/libexec/openldap/seqmod.so.2
/usr/libexec/openldap/seqmod.so.2.0.200
/usr/libexec/openldap/sssvlv.so
/usr/libexec/openldap/sssvlv.so.2
/usr/libexec/openldap/sssvlv.so.2.0.200
/usr/libexec/openldap/syncprov.so
/usr/libexec/openldap/syncprov.so.2
/usr/libexec/openldap/syncprov.so.2.0.200
/usr/libexec/openldap/translucent.so
/usr/libexec/openldap/translucent.so.2
/usr/libexec/openldap/translucent.so.2.0.200
/usr/libexec/openldap/unique.so
/usr/libexec/openldap/unique.so.2
/usr/libexec/openldap/unique.so.2.0.200
/usr/libexec/openldap/valsort.so
/usr/libexec/openldap/valsort.so.2
/usr/libexec/openldap/valsort.so.2.0.200
/usr/libexec/slapd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openldap/09fc2e9f527fcb0d594bc658d21e42d3a5124b83
/usr/share/package-licenses/openldap/0da054d8429802e25641decec43d4fbc1fbe4f2f
/usr/share/package-licenses/openldap/7578422c24f1c556f2a5884294bdf7a545a53a64
/usr/share/package-licenses/openldap/7d003e7541a517109ed166c1db227c0f21ca3db6
/usr/share/package-licenses/openldap/bc06cbdf781c87d2df2fe385214f936d010dd2a2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ldapadd.1
/usr/share/man/man1/ldapcompare.1
/usr/share/man/man1/ldapdelete.1
/usr/share/man/man1/ldapexop.1
/usr/share/man/man1/ldapmodify.1
/usr/share/man/man1/ldapmodrdn.1
/usr/share/man/man1/ldappasswd.1
/usr/share/man/man1/ldapsearch.1
/usr/share/man/man1/ldapurl.1
/usr/share/man/man1/ldapvc.1
/usr/share/man/man1/ldapwhoami.1
/usr/share/man/man5/ldap.conf.5
/usr/share/man/man5/ldif.5
/usr/share/man/man5/lloadd.conf.5
/usr/share/man/man5/slapd-asyncmeta.5
/usr/share/man/man5/slapd-config.5
/usr/share/man/man5/slapd-dnssrv.5
/usr/share/man/man5/slapd-ldap.5
/usr/share/man/man5/slapd-ldif.5
/usr/share/man/man5/slapd-mdb.5
/usr/share/man/man5/slapd-meta.5
/usr/share/man/man5/slapd-monitor.5
/usr/share/man/man5/slapd-null.5
/usr/share/man/man5/slapd-passwd.5
/usr/share/man/man5/slapd-perl.5
/usr/share/man/man5/slapd-relay.5
/usr/share/man/man5/slapd-sock.5
/usr/share/man/man5/slapd-sql.5
/usr/share/man/man5/slapd-wt.5
/usr/share/man/man5/slapd.access.5
/usr/share/man/man5/slapd.backends.5
/usr/share/man/man5/slapd.conf.5
/usr/share/man/man5/slapd.overlays.5
/usr/share/man/man5/slapd.plugin.5
/usr/share/man/man5/slapo-accesslog.5
/usr/share/man/man5/slapo-auditlog.5
/usr/share/man/man5/slapo-autoca.5
/usr/share/man/man5/slapo-chain.5
/usr/share/man/man5/slapo-collect.5
/usr/share/man/man5/slapo-constraint.5
/usr/share/man/man5/slapo-dds.5
/usr/share/man/man5/slapo-deref.5
/usr/share/man/man5/slapo-dyngroup.5
/usr/share/man/man5/slapo-dynlist.5
/usr/share/man/man5/slapo-homedir.5
/usr/share/man/man5/slapo-memberof.5
/usr/share/man/man5/slapo-otp.5
/usr/share/man/man5/slapo-pbind.5
/usr/share/man/man5/slapo-pcache.5
/usr/share/man/man5/slapo-ppolicy.5
/usr/share/man/man5/slapo-refint.5
/usr/share/man/man5/slapo-remoteauth.5
/usr/share/man/man5/slapo-retcode.5
/usr/share/man/man5/slapo-rwm.5
/usr/share/man/man5/slapo-sock.5
/usr/share/man/man5/slapo-sssvlv.5
/usr/share/man/man5/slapo-syncprov.5
/usr/share/man/man5/slapo-translucent.5
/usr/share/man/man5/slapo-unique.5
/usr/share/man/man5/slapo-valsort.5
/usr/share/man/man5/slappw-argon2.5
/usr/share/man/man8/lloadd.8
/usr/share/man/man8/slapacl.8
/usr/share/man/man8/slapadd.8
/usr/share/man/man8/slapauth.8
/usr/share/man/man8/slapcat.8
/usr/share/man/man8/slapd.8
/usr/share/man/man8/slapdn.8
/usr/share/man/man8/slapindex.8
/usr/share/man/man8/slapmodify.8
/usr/share/man/man8/slappasswd.8
/usr/share/man/man8/slapschema.8
/usr/share/man/man8/slaptest.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/slapd.service
