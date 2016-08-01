package com.crontab.cvsInfo;

import java.sql.Connection;
import java.sql.PreparedStatement;

import com.crontab.util.ConnectionPool;

public class ConnectionResturant {
	public static void deleteResturant() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();

			String sql = "delete from sl_resturant";
			
			pstmt = con.prepareStatement(sql);
			pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(pstmt != null) {
				pstmt.close();
			}
			if (con != null) {
				con.close();
			}
		}
	}
	
	public static void insertDaumResturant() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//honbap_daum.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void insertNaverResturant() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//honbap_naver.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}
