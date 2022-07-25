from datetime import datetime
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

USER_STATUS = {
    'ACTIVE'  : 'ACTIVE' # 정상
    , 'STOP'  : 'STOP' # 정지(탈퇴)
    , 'PAUSE' : 'PAUSE' # 계정 휴면
    , 'BAN'   : 'BAN' # 계정 정지
}

ROLES = {
    'ROLE_NORMAL'     : 'NORMAL' # 일반 사용자
    , 'ROLE_MANAGER'  : 'MANAGER' # 일반 관리자
    , 'ROLE_SUPER'    : 'SUPER' # 슈퍼 관리자
}

# 사용자 정보 관리 클래스
class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        
        if not username : # 이메일이 없다면
            raise ValueError('이메일은 필수 요소입니다.')

        if not password : # 패스워드가 없다면
            raise ValueError('패스워드는 필수 요소입니다.')
        
        # 이메일 주소를 소문자로 변환하는 과정을 거친 뒤에 저장한다.
        username = self.normalize_email(username) 
        
        # 사용자 모델 객체를 생성한다.
        user = self.model(
            username           = username
            , is_active     = extra_fields.get('is_active')
        )

        # 사용자 패스워드는 Django에서 제공해주는 해시화 과정(SHA 256)을 거쳐서 저장한다.
        user.set_password(password)

        # 실제로 DB에 사용자 정보를 저장한다.
        user.save(using=self._db)

        # 기본적으로 모든 사용자는 일반사용자 권한을 갖게된다.
        self.create_auth(user, ROLES.get('ROLE_NORMAL', 'NORMAL'))

        # 스탭 권한을 부여할지 확인 후 MANAGER 권한을 부여한다.
        if extra_fields.get('is_staff') is True :
            self.create_auth(user, ROLES.get('ROLE_MANAGER', 'MANAGER'))

        # 슈퍼 관리자 권한을 부여할지 확인 후 SUPER 권한을 부여한다.
        if extra_fields.get('is_superuser') is True :
            self.create_auth(user, ROLES.get('ROLE_SUPER', 'SUPER')) 

        return user
    

    # 일반 사용자 생성
    def create_user(self, username, password=None, **extra_fields): 
        extra_fields['is_active'] = False
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        
        return self._create_user(username, password, **extra_fields)

    # 스탭 사용자 생성
    def create_staff(self, username, password=None, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = False
        
        return self._create_user(username, password, **extra_fields)

    # 슈퍼 관리자 생성
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(username, password, **extra_fields)

    # 권한 정보 등록
    def create_auth( self, user, role=ROLES.get('ROLE_NORMAL', 'NORMAL')):
        role_obj = Auth(
            user = user,
            role = role
        )

        role_obj.save(using=self.db)

        return role_obj


# 사용자 계정 테이블 모델
class User(AbstractBaseUser):
    id           = models.BigAutoField(primary_key=True)
    username        = models.EmailField(max_length=254, unique=True) # 이메일 주소
    secret       = models.UUIDField(default=uuid.uuid4) # 사용자 서명용 비밀키
    status       = models.CharField(max_length=10, default=USER_STATUS.get('ACTIVE', 'ACTIVE')) # 사용자 현재 상태
    is_active    = models.BooleanField(default=False) # 계정 활성화 여부
    created_at   = models.DateTimeField(auto_now_add=True) # 계정 생성일
    updated_at   = models.DateTimeField(auto_now=True) # 계정 수정일
    
    objects = UserManager() # 사용자 정보를 관리하는 클래스는 지정한다.

    USERNAME_FIELD = 'username' # 사용자 이름으로 사용될 필드의 이름을 지정한다.

    # 사용자 PK 값을 가져오기위한 함수
    def get_id(self):
        return self.id
    

# 권한 테이블 모델
class Auth(models.Model):
    user = models.ForeignKey(User, related_name='auths', on_delete=models.CASCADE)
    role = models.CharField(max_length=30, default=ROLES.get('ROLE_NORMAL', 'NORMAL'))
