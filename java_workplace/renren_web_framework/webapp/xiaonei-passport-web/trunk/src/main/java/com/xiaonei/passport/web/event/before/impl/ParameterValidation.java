package com.xiaonei.passport.web.event.before.impl;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Service;

import com.xiaonei.passport.constants.LoginStatusCode;
import com.xiaonei.passport.web.event.before.IBeforeLoginListern;
import com.xiaonei.passport.web.model.PassportForm;
import com.xiaonei.passport.web.validate.PassportFormValidator;
@Service
public class ParameterValidation implements IBeforeLoginListern{

	@Override
	public LoginStatusCode process(HttpServletRequest request,
			HttpServletResponse response, PassportForm pForm) {
		 LoginStatusCode code=PassportFormValidator.getInstance().validate(request, pForm, true);
		 return code;
	}

}
